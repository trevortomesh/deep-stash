import os
import sys
import json
import shutil
from datetime import datetime
import time
try:
    from tqdm import tqdm
except ImportError:
    print("⚠️ tqdm not installed. Progress bars will be disabled.")
    def tqdm(x, *a, **kw): return x

VERBOSE = False

def init():
    """Initialize DeepStash by setting the root directory for stashed files."""
    # Prompt the user for a directory to use as the DeepStash root
    path = input("📁 Enter deepstash directory path: ").strip()
    if path.endswith(".ds"):
        print("❌ Invalid path. Please choose a directory that does not end with '.ds'.")
        sys.exit(1)
    if not os.path.isdir(path):
        print("❗ That’s not a valid directory.")
        sys.exit(1)
    # Save the root directory path in a config file
    config = {"root": os.path.abspath(path)}
    with open(os.path.expanduser("~/.dsconfig.json"), "w") as f:
        json.dump(config, f)
    print(f"✅ Deepstash directory set to {config['root']}")

def load_config():
    """Load the DeepStash configuration from the user's home directory."""
    config_path = os.path.expanduser("~/.dsconfig.json")
    if not os.path.exists(config_path):
        print("❗ Deepstash not initialized. Please run: ds --init")
        sys.exit(1)
    # Read and return the JSON config data
    with open(config_path, "r") as f:
        return json.load(f)

def get_unique_path(path):
    """Generate a unique file or directory path by appending an index if needed."""
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    i = 1
    # Increment index until a non-existing path is found
    while True:
        new_path = f"{base}_{i}{ext}"
        if not os.path.exists(new_path):
            return new_path
        i += 1

def deepstash_item(target, config):
    """Move a file or directory into the DeepStash directory and create a ghost file."""
    if not os.path.exists(target):
        print(f"❌ {target} does not exist.")
        return

    # Determine the base name for the target to store in stash
    base_name = os.path.basename(os.path.abspath(target))
    # Get a unique destination path inside the stash root
    dest = get_unique_path(os.path.join(config["root"], base_name))

    print(f"🔄 Stashing: {target}")

    try:
        # Ensure the stash destination is writable
        if not os.access(config["root"], os.W_OK):
            raise PermissionError(f"Stash directory '{config['root']}' is not writable.")

        if os.path.isdir(target):
            print("📁 Copying directory...")
            # Gather all files in the directory tree first
            all_files = []
            for root, dirs, files in os.walk(target):
                for file in files:
                    all_files.append(os.path.join(root, file))
            # Copy files with a single progress bar
            for src_file in tqdm(all_files, desc="📦 Progress", unit="file"):
                rel_path = os.path.relpath(src_file, target)
                dst_file = os.path.join(dest, rel_path)
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                try:
                    shutil.copy2(src_file, dst_file)
                except FileNotFoundError:
                    print(f"⚠️ Skipping missing file: {src_file}")
                    continue
                except PermissionError as e:
                    print(f"⚠️ Permission denied copying {src_file}. Skipping. Details: {e}")
                    continue
            # Remove the original directory after copying
            shutil.rmtree(target)
        else:
            print("📄 Copying file...")
            # Copy the file in chunks to show a gradual progress bar
            total_size = os.path.getsize(target)
            chunk_size = 1024 * 1024  # 1 MiB per chunk
            with open(target, "rb") as fsrc, open(dest, "wb") as fdst:
                with tqdm(total=total_size, unit="B", unit_scale=True, desc="📦 Progress") as pbar:
                    while True:
                        chunk = fsrc.read(chunk_size)
                        if not chunk:
                            break
                        fdst.write(chunk)
                        pbar.update(len(chunk))
            os.remove(target)
    except PermissionError as e:
        # Determine if the issue is with the stash directory or the target
        if not os.access(config["root"], os.W_OK):
            print(f"❌ Permission denied: Cannot write to stash directory '{config['root']}'.")
        else:
            print(f"❌ Permission denied while accessing '{target}'. Please check file permissions.\nDetails: {e}")
        return

    # Create a ghost file recording original path, stash path, type, and timestamp
    ghost = {
        "original": os.path.abspath(target),
        "deep": dest,
        "type": "dir" if os.path.isdir(dest) else "file",
        "timestamp": datetime.now().isoformat()
    }
    ghost_path = os.path.abspath(target) + ".ds"
    # Write the ghost metadata to a .ds file alongside the original location
    with open(ghost_path, "w") as f:
        json.dump(ghost, f)
    print(f"📦 Stashed: {target} → {dest}")

def safe_copytree(src, dst, max_errors_per_dir=5):
    total_skipped = 0
    errors = []
    for root, dirs, files in os.walk(src):
        rel_root = os.path.relpath(root, src)
        # Early skip for directories full of unreadable .ds files
        if all(name.endswith(".ds") for name in files) and files:
            unreadable_ds = 0
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    with open(file_path, "rb"):
                        pass
                except Exception:
                    unreadable_ds += 1
            if unreadable_ds == len(files):
                print(f"🚫 Skipping directory '{rel_root}' — all files are unreadable .ds files.")
                continue
        error_count = 0
        skip_count = 0
        first_skip = None
        skip_messages = []
        for name in files:
            src_file = os.path.join(root, name)
            rel_path = os.path.relpath(src_file, src)
            dst_file = os.path.join(dst, rel_path)
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            try:
                shutil.copy2(src_file, dst_file)
                error_count = 0  # reset on success
            except Exception as e:
                errors.append((src_file, dst_file, str(e)))
                error_count += 1
                skip_count += 1
                total_skipped += 1
                if VERBOSE:
                    print(f"⚠️ Skipping {src_file}: {e}")
                if skip_count == 1:
                    first_skip = src_file
                if error_count >= max_errors_per_dir:
                    print(f"🚫 Too many errors in directory '{rel_root}'. Skipping the rest of this directory.")
                    break
    if total_skipped > 0:
        print(f"\n⚠️ Total files skipped during copy: {total_skipped}\n")
    return errors

def restore(ghost_file):
    """Restore a stashed file or directory using its .ds ghost metadata file."""
    if not os.path.exists(ghost_file):
        print("❌ .ds file not found.")
        return

    # Load ghost metadata from the .ds file
    with open(ghost_file, "r") as f:
        ghost = json.load(f)

    # Backward compatibility: convert old format to new format
    if "deep_stash_path" in ghost and "original_path" in ghost and "deep" not in ghost and "original" not in ghost:
        ghost["deep"] = ghost.get("deep_stash_path")
        ghost["original"] = ghost.get("original_path")
        if "type" in ghost and ghost["type"] == "folder":
            ghost["type"] = "dir"
        elif "type" in ghost and ghost["type"] == "file":
            ghost["type"] = "file"
        print("🔁 Converted old .ds format to new format.")

    # Ensure all required keys are present
    required_keys = ["original", "deep", "type"]
    if not all(k in ghost for k in required_keys):
        print(f"⚠️ Invalid .ds file '{ghost_file}': missing required keys. Attempting auto-fix...")

        # Attempt to infer missing values only
        if "original" not in ghost:
            ghost["original"] = ghost_file.replace(".ds", "")
            print(f"🔧 Inferred 'original' as {ghost['original']}")
        if "deep" not in ghost:
            print("❌ Missing 'deep' (stash path) and cannot infer. Skipping.")
            return
        if "type" not in ghost:
            ghost["type"] = "dir" if os.path.isdir(ghost.get("deep", "")) else "file"
            print(f"🔧 Inferred 'type' as {ghost['type']}")

        # Validate again
        if not all(k in ghost for k in required_keys):
            print("❌ Auto-fix failed. Skipping file.")
            return
        else:
            # Save corrected ghost file
            with open(ghost_file, "w") as f:
                json.dump(ghost, f, indent=2)
            print(f"✅ Auto-fix successful. .ds file '{ghost_file}' has been updated.")

    # Validate that the stash location exists
    if not os.path.exists(ghost["deep"]):
        print(f"❌ Cannot restore because the stashed item at '{ghost['deep']}' does not exist.")
        print("ℹ️ You may need to reconnect the external drive or adjust permissions.")
        return

    if ghost["type"] == "dir":
        # Copy the stashed directory back to the original location, merging if needed
        safe_copytree(ghost["deep"], ghost["original"])
        # Remove the stashed directory
        shutil.rmtree(ghost["deep"], ignore_errors=True)
    else:
        if os.path.isdir(ghost["deep"]):
            print(f"❌ Error: Stashed item at '{ghost['deep']}' is a directory, but marked as type 'file'. Skipping.")
            return
        print(f"🔄 Restoring: {ghost['deep']} → {ghost['original']}")
        print("📄 Restoring file with progress...")
        # Ensure the destination directory exists
        os.makedirs(os.path.dirname(ghost["original"]), exist_ok=True)
        # Copy the file in chunks to show a gradual progress bar
        total_size = os.path.getsize(ghost["deep"])
        chunk_size = 1024 * 1024  # 1 MiB per chunk
        try:
            with open(ghost["deep"], "rb") as fsrc, open(ghost["original"], "wb") as fdst:
                with tqdm(total=total_size, unit="B", unit_scale=True, desc="♻️ Progress") as pbar:
                    while True:
                        try:
                            chunk = fsrc.read(chunk_size)
                        except OSError as e:
                            print(f"❌ Failed to read from '{ghost['deep']}': {e}. Skipping file.")
                            return
                        if not chunk:
                            break
                        fdst.write(chunk)
                        pbar.update(len(chunk))
        except OSError as e:
            print(f"❌ Cannot open one of the files for copying: {e}. Skipping.")
            return
        # Remove the stashed file
        os.remove(ghost["deep"])

    # Remove the ghost metadata file after restoration
    os.remove(ghost_file)
    print(f"♻️ Restored: {ghost['original']}")

def main():
    """Parse command-line arguments and execute the appropriate DeepStash action."""
    global VERBOSE
    args = sys.argv[1:]

    if "--verbose" in args:
        VERBOSE = True
        args.remove("--verbose")

    # Display help information if requested
    if args and args[0] in ("--help", "-h"):
        print("""📘 DeepStash Command Help:

  ds --init
    Initialize DeepStash by setting the root directory for stashed files.

  ds <file_or_folder> [!<pattern> ...]
    Move the specified file or folder into the stash and leave behind a .ds ghost file.
    You can exclude files or folders by prefixing patterns with '!', e.g., '!.png' (quoted) to skip all .png files.

  ds <file_or_folder>.ds [!<pattern> ...]
    Restore the specified item using its .ds metadata file.
    Use exclusion patterns to skip certain restores, e.g., !.log to avoid restoring .log files.

  ds --help or ds -h
    Show this usage information.

Examples:
  ds --init
  ds mynotes.txt
  ds old_project/
  ds mynotes.txt.ds
  ds photos/ '!.raw' '!.tmp'
  ds backup.db.ds '!.bak'

Advanced Options:
  --verbose
    Show detailed messages for each skipped file.

Automatic Skipping:
  If too many files in a directory fail to copy, DeepStash will automatically skip the rest of that directory.
  If all files in a directory are unreadable `.ds` files, that directory will be skipped without prompt.
""")
        return

    # Show usage info if no arguments provided
    if not args:
        print("ℹ️ Usage: ds --init | ds <file_or_folder> | ds <file_or_folder>.ds")
        print("Use --help for more information.")
        return

    # Initialize stash root directory
    if args[0] == "--init":
        init()
        return

    # Load configuration for stash root directory
    config = load_config()

    # Handle exclusion patterns like !.png, !.jpg, etc.
    exclude_patterns = [arg[1:] for arg in args if arg.startswith("!")]
    args = [arg for arg in args if not arg.startswith("!")]
    if exclude_patterns:
        args = [t for t in args if not any(t.endswith(p) for p in exclude_patterns)]

    if all(t.endswith(".ds") for t in args):
        for t in args:
            restore(t)
    elif all(not t.endswith(".ds") for t in args):
        for t in args:
            deepstash_item(t, config)
    else:
        print("❌ Mixed operation detected. Please run restore and stash operations separately.")
        sys.exit(1)

if __name__ == "__main__":
    main()

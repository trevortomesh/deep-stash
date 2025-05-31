import os
import sys
import json
import shutil
from datetime import datetime

def init():
    """Initialize DeepStash by setting the root directory for stashed files."""
    # Prompt the user for a directory to use as the DeepStash root
    path = input("📁 Enter deepstash directory path: ").strip()
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

    try:
        # Ensure the stash destination is writable
        if not os.access(config["root"], os.W_OK):
            raise PermissionError(f"Stash directory '{config['root']}' is not writable.")

        if os.path.isdir(target):
            shutil.copytree(target, dest)
            shutil.rmtree(target)
        else:
            shutil.copy2(target, dest)
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

def restore(ghost_file):
    """Restore a stashed file or directory using its .ds ghost metadata file."""
    if not os.path.exists(ghost_file):
        print("❌ .ds file not found.")
        return

    # Load ghost metadata from the .ds file
    with open(ghost_file, "r") as f:
        ghost = json.load(f)

    if ghost["type"] == "dir":
        # Copy the stashed directory back to the original location, merging if needed
        shutil.copytree(ghost["deep"], ghost["original"], dirs_exist_ok=True)
        # Remove the stashed directory
        shutil.rmtree(ghost["deep"], ignore_errors=True)
    else:
        # Copy the stashed file back to the original location
        shutil.copy2(ghost["deep"], ghost["original"])
        # Remove the stashed file
        os.remove(ghost["deep"])

    # Remove the ghost metadata file after restoration
    os.remove(ghost_file)
    print(f"♻️ Restored: {ghost['original']}")

def main():
    """Parse command-line arguments and execute the appropriate DeepStash action."""
    args = sys.argv[1:]

    # Display help information if requested
    if args and args[0] in ("--help", "-h"):
        print("""📘 DeepStash Command Help:

    ds --init
        Initialize DeepStash by setting the root directory for stashed files.

    ds <file_or_folder>
        Move the specified file or folder into the stash and leave behind a .ds ghost file.

    ds <file_or_folder>.ds
        Restore the specified item using its .ds metadata file.

    Examples:
        ds --init
        ds mynotes.txt
        ds old_project/
        ds mynotes.txt.ds
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
    # Process each argument: restore if .ds file, otherwise stash the item
    for t in args:
        if t.endswith(".ds"):
            restore(t)
        else:
            deepstash_item(t, config)

if __name__ == "__main__":
    main()

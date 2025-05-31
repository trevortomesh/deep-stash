# DeepStash
![img.png](img.png)
DeepStash is a command-line utility for stashing away files and folders into a designated directory, leaving behind `.ds` metadata files for easy restoration. It’s useful for clearing workspace clutter while retaining a simple path to recover archived content.

## Features
- Initialize a designated stash directory
- Move files or directories into the stash with a `.ds` metadata file left behind
- Restore items to their original location using `.ds` files
- Automatically handles name collisions by generating unique paths
- Provides clear error messages for missing files or permission issues

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/deepstash.git
cd deepstash
pip install .
```

## Usage

```bash
ds --init                   # Configure your stash directory
ds notes.txt                # Stash the file and leave behind a .ds file
ds notes.txt.ds             # Restore the file from the stash
```

## Help

```bash
ds --help
```

Displays usage instructions.

## Example

```bash
$ ds --init
Enter deepstash directory path: /Volumes/Archive
Deepstash directory set to /Volumes/Archive

$ ds report.pdf
Stashed: report.pdf → /Volumes/Archive/report.pdf

$ ls
 report.pdf.ds

$ ds report.pdf.ds
Restored: /Users/yourname/Desktop/report.pdf
```

## License
MIT License
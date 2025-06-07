<p align="center">
  <img src="logo.png" alt="DeepStash logo" width="300"/>
</p>

<p align="center">
  <em>Part of the <a href="https://github.com/trevortomesh/stash">Stash Ecosystem</a> — tools for clean digital minimalism and controlled file flow.</em>
</p>

<p align="center">
  <img alt="Python 3.6+" src="https://img.shields.io/badge/Python-3.6+-blue?logo=python&logoColor=white&style=flat-square"/>
  <img alt="Vibe-Coded" src="https://img.shields.io/badge/Vibe%20Coded-%F0%9F%92%8C-purple?style=flat-square"/>
  <a href="#-dedication">
    <img alt="Fearfully Coded" src="https://img.shields.io/badge/🕊️Fearfully%20Coded-blue?style=flat-square"/>
  </a>
</p>

# 🧳 DeepStash

**DeepStash** is a command-line tool for safely moving files off your system while keeping your file structure intact.

It was born out of necessity — my MacBook Air kept running out of space, but I didn’t want to delete or misplace anything. DeepStash lets you move files to an external location while leaving behind a `.ds` file that remembers where the original lived. One command restores it when you need it.

----
## 🧠 Philosophy

People are relational creatures — we understand things by how they connect to everything else. Your file structure isn’t just convenience; it’s cognitive scaffolding.

But sometimes, files pile up. Drives bloat. Systems slow down.

**DeepSTASH** is the middle path: move the file, keep the context. A `.ds` file is left in place as a note — a breadcrumb to its new home — so your mental model stays untouched.

----
## 🔍 What It Does

- 📁 Moves files or folders to a custom stash directory  
- 📝 Leaves behind a `.ds` file with all the metadata needed to restore  
- 🧭 Restores files to the exact same path with one command  
- 🧠 Prevents overwrites by generating unique names when needed  
- 🚫 Friendly errors if something’s missing or inaccessible  
- 📦 Progress bars when copying files or directories  
- ♻️ Progress bars when restoring files or directories  
- 🛠️ Automatically repairs broken `.ds` metadata files  
- ⚠️ Clear, graceful error messages when stash location is missing or type mismatches  

----
## 🧪 Example

```bash
$ ds --init
📁 Enter deepstash directory path: /Volumes/Archive
✅ Deepstash directory set to /Volumes/Archive

$ ds FinalPaper.pdf
📦 Stashed: FinalPaper.pdf → /Volumes/Archive/FinalPaper.pdf

$ ls
FinalPaper.pdf.ds

$ ds FinalPaper.pdf.ds
♻️ Restored: /Users/user/Documents/FinalPaper.pdf
```

----
## ⚙️ Usage

```bash
ds --init                   # Set your stash directory
ds <file_or_folder> [!'pattern' ...]   
  Move the specified file or folder into the stash and leave behind a .ds ghost file.
  You can exclude files or folders by prefixing patterns with '!', e.g., '!.png' to skip all .png files.

ds <file_or_folder>.ds [!'pattern' ...]
  Restore the specified item using its .ds metadata file.
  Use exclusion patterns to skip certain restores, e.g., '!.log' to avoid restoring .log files.

ds --help or ds -h
  Show this usage information.

Examples:
  ds --init
  ds mynotes.txt
  ds old_project/
  ds mynotes.txt.ds
  ds photos/ '!.raw' '!.tmp'
  ds backup.db.ds '!.bak'
```

----
## 📄 `.ds` File Format

Each `.ds` file is a simple JSON document that stores stash metadata:

```json
{
  "original": "/Users/user/Documents/Projects/deep.txt",
  "deep": "/Volumes/StorageDrive/deepstash/deep.txt",
  "type": "file"
}
```

### Fields:
- `original` – original path before stashing  
- `deep` – location where the item was moved  
- `type` – either `"file"` or `"dir"`  

These metadata files allow DeepStash to reverse the stash operation with confidence and precision.

----
## 🛠️ Commands Summary

| Command              | Description                            |
|----------------------|----------------------------------------|
| `ds --init`          | Set the stash location                 |
| `ds <item>`          | Stash the item                         |
| `ds <item>.ds`       | Restore the item                       |
| `ds --help`          | Show usage info                        |
| `pip install .`      | Install from source locally            |

----
## 🛡️ Error Handling & Auto-Fix

- If a `.ds` file is missing keys, DeepStash attempts to auto-repair it and confirms success with a “✅ Auto-fix successful…” message.  
- If the stash path (`deep`) no longer exists, DeepStash prints:  
  ❌ Cannot restore because the stashed item at '…' does not exist.  
  ℹ️ You may need to reconnect the external drive or adjust permissions.  
- If a `.ds` record’s `type` is “file” but actually points to a directory, DeepStash prints:  
  ❌ Error: Stashed item at '…' is a directory, but marked as type 'file'. Skipping.  

----
## 🚀 Install

```bash
git clone https://github.com/YOUR_USERNAME/deepstash.git
cd deepstash
pip install .
```

Or from within any local project directory:

```bash
pip install .
```

----
## 🤖 Note

This tool was created using **vibe coding** — describing what I wanted to an AI assistant, refining the results through iteration. No detailed plan — just intuition, adaptation, and execution.

----
## 🕊️ Dedication

This project is dedicated to the Lord.

All logic, structure, and order — including the very foundations of programming — reflect the perfection of His design. May this tool, in its small way, point toward the beauty and coherence He has written into the fabric of creation.

> **"I praise you, for I am fearfully and wonderfully made.  
> Wonderful are your works; my soul knows it very well."**  
> — Psalm 139:14

**Soli Deo Gloria.**

----
## 📄 License

Licensed under the [MIT License](LICENSE).
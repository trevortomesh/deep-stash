<p align="center">
  <img src="logo.png" alt="DeepStash logo" width="300"/>
</p>

<p align="center">
  <img alt="Python 3.6+" src="https://img.shields.io/badge/Python-3.6+-blue?logo=python&logoColor=white&style=flat-square"/>
  <img alt="Vibe-Coded" src="https://img.shields.io/badge/Vibe%20Coded-%F0%9F%92%8C-purple?style=flat-square"/>
  <a href="#-dedication">
<img alt="Fearfully Coded" src="https://img.shields.io/badge/Fearfully%20Coded-✝️-blue?style=flat-square"/>
</a>
</p>

# 🧳 DeepStash

**DeepStash** is a command-line tool for safely moving files off your system while keeping your file structure intact.

It was born out of necessity — my MacBook Air kept running out of space, but I didn’t want to delete or misplace anything. DeepStash lets you move files to an external location while leaving behind a `.ds` file that remembers where the original lived. One command restores it when you need it.

---

## 🧠 Philosophy

People are relational creatures — we understand things by how they connect to everything else. Your file structure isn’t just convenience; it’s cognitive scaffolding.

But sometimes, files pile up. Drives bloat. Systems slow down.

**DeepStash** is the middle path: move the file, keep the context. A `.ds` file is left in place as a note — a breadcrumb to its new home — so your mental model stays untouched.

---

## 🔍 What It Does

- 📁 Moves files or folders to a custom stash directory  
- 📝 Leaves behind a `.ds` file with all the metadata needed to restore  
- 🧭 Restores files to the exact same path with one command  
- 🧠 Prevents overwrites by generating unique names when needed  
- 🚫 Friendly errors if something’s missing or inaccessible  

---

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

---

## ⚙️ Usage

```bash
ds --init                   # Set your stash directory
ds my-folder                # Stash and replace with .ds file
ds my-folder.ds             # Restore it later
```

You can stash multiple items at once:

```bash
ds *.mp4
```

---

## 📄 `.ds` File Format

Each `.ds` file is a simple JSON document that stores stash metadata:

```json
{
  "original_path": "/Users/user/Documents/Projects/deep.txt",
  "deep_stash_path": "/Volumes/StorageDrive/deepstash/deep.txt",
  "size": 2048,
  "modified_at": "2025-05-31T14:22:18.164030"
}
```

### Fields:
- `original_path` – Where the file was before stashing  
- `deep_stash_path` – Where it was moved  
- `size` – Size in bytes  
- `modified_at` – Last modified timestamp (ISO 8601)  

These metadata files allow DeepStash to reverse the stash operation with confidence and precision.

---

## 🛠️ Commands Summary

| Command | Description |
|---------|-------------|
| `ds --init` | Set the stash location |
| `ds <item>` | Stash the item |
| `ds <item>.ds` | Restore the item |
| `ds --help` | Show usage info |
| `pip install .` | Install from source locally |

---

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

---

## 🤖 Note

This tool was created using **vibe coding** — describing what I wanted to an AI assistant, refining the results through iteration. No detailed plan — just intuition, adaptation, and execution.

---

## 🙏 Dedication

This project is dedicated to the Lord.

All logic, structure, and order — including the very foundations of programming — reflect the perfection of His design. May this tool, in its small way, point toward the beauty and coherence He has written into the fabric of creation.

> **"I praise you, for I am fearfully and wonderfully made.  
> Wonderful are your works; my soul knows it very well."**  
> — Psalm 139:14

**Soli Deo Gloria.**

---

## 📄 License

Licensed under the [MIT License](LICENSE).

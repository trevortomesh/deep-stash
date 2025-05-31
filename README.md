<p align="center">
  <img src="logo.png" alt="DeepStash logo" width="300"/>
</p>

<p align="center">
  <img alt="Python 3.6+" src="https://img.shields.io/badge/Python-3.6+-blue?logo=python&logoColor=white&style=flat-square"/>
  <img alt="Vibe-Coded" src="https://img.shields.io/badge/Vibe%20Coded-%F0%9F%92%8C-purple?style=flat-square"/>
  <a href="#-dedication">
    <img alt="Proverbs 9:10" src="https://img.shields.io/badge/Proverbs%209%3A10-%22Fear%20of%20the%20Lord%22-lightgrey?style=flat-square"/>
  </a>
</p>

# 🧳 DeepStash

**DeepStash** is a simple command-line tool that helps you move files and folders off your local machine without breaking your workspace.

It was borne out of necessity — my MacBook Air kept running out of space, but I didn’t want to delete anything or lose track of where things belonged. DeepStash lets you offload files to an external drive (or anywhere else) while leaving behind a small `.ds` file that remembers where it came from. When you need it again, one command brings it back.

---

## 🧠 Philosophy

People are relational creatures — we understand things by how they’re situated in relation to other things. That’s why file structure matters. The way you organize your folders, the exact placement of a note, a project, or a reference file — it reflects how your mind maps your work.

But sometimes, the weight of those files becomes too much. Drives fill up. Machines slow down. **DeepStash** offers a compromise: keep your structure, but offload the weight. You stash a file somewhere else, but leave behind a `.ds` marker — a note to your future self saying, *“Here’s where I put it.”*

---

## 🔍 What It Does

- Moves files or folders to a stash directory of your choice  
- Leaves behind a `.ds` metadata file that records where the item was stashed  
- Lets you restore any item back to its original location later  
- Handles name collisions safely by creating unique destination paths  
- Gives clear feedback if something goes wrong (missing files, permission issues, etc.)  

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
ds my-folder                # Move and replace with a .ds file
ds my-folder.ds             # Restore it back
```

You can stash multiple files or folders at once:

```bash
ds *.zip
```

---

## 📄 `.ds` File Format

When you stash something, DeepStash replaces it with a `.ds` file — a small JSON file that records where the original item went. This file allows DeepStash to bring it back to the exact spot later.

Example:

```json
{
  "original_path": "/Users/user/Documents/Projects/deep.txt",
  "deep_stash_path": "/Volumes/StorageDrive/deepstash/deep.txt",
  "size": 2048,
  "modified_at": "2025-05-31T14:22:18.164030"
}
```

### Fields:

- **`original_path`** – The full path to where the file or folder originally lived  
- **`deep_stash_path`** – The destination path in your stash directory  
- **`size`** – File size in bytes at the time it was stashed  
- **`modified_at`** – Timestamp of the last modification (ISO 8601 format)  

These metadata files are portable, editable, and safe to version-control if needed. DeepStash uses them to reverse the stash operation with precision.

---

## 🛠️ Commands Summary

| Command | Description |
|---------|-------------|
| `ds --init` | Set the destination stash directory |
| `ds <item>` | Stash a file or folder |
| `ds <item>.ds` | Restore it |
| `ds --help` | Show a helpful summary |
| `pip install .` | Install locally from source |

---

## 🚀 Install

```bash
git clone https://github.com/YOUR_USERNAME/deepstash.git
cd deepstash
pip install .
```

Or install from any folder containing the source:

```bash
pip install .
```

---

## 🤖 Note

This project was built using **vibe coding** — describing what I wanted to an AI assistant and refining the result through fast iterations. No line-by-line plan — just vibes and necessity.

---

## 🙏 Dedication

This project is dedicated to the Lord.

All logic, structure, and order — including the very foundations of programming — reflect the perfection of His design. May this tool, in its small way, point toward the beauty and coherence He has written into the fabric of creation.

> **"The fear of the Lord is the beginning of wisdom, and knowledge of the Holy One is understanding."**  
> — Proverbs 9:10

**Soli Deo Gloria.**

---

## 📄 License

Licensed under the [MIT License](LICENSE).
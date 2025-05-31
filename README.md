<p align="center">
  <img src="logo.png" alt="DeepStash logo" width="300"/>
</p>

<p align="center">
  <img alt="Python 3.6+" src="https://img.shields.io/badge/Python-3.6+-blue?logo=python&logoColor=white&style=flat-square"/>
  <img alt="Vibe-Coded" src="https://img.shields.io/badge/Vibe%20Coded-%F0%9F%92%8C-purple?style=flat-square"/>
</p>

# 🧳 DeepStash

**DeepStash** is a simple command-line tool that helps you move files and folders off your local machine without breaking your workspace.

It was borne out of necessity — my MacBook Air kept running out of space, but I didn’t want to delete anything or lose track of where things belonged. DeepStash lets you offload files to an external drive (or anywhere else) while leaving behind a small `.ds` file that remembers where it came from. When you need it again, one command brings it back.

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
♻️ Restored: /Users/you/Documents/FinalPaper.pdf
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

## 📄 License

Licensed under the [MIT License](LICENSE).
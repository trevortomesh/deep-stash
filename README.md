<p align="center">
  <img src="logo.png" alt="DeepStash logo" width="300"/>
</p>

# 🧳 DeepStash

**DeepStash** is a command-line utility for moving files and folders to an external or backup location — while leaving behind `.ds` metadata files so they can be restored to the exact same place. It's not about tidying up your workspace — it's about keeping everything *where it belongs* without using up your drive.

---

## ✨ Features

- 🗂️ **Designate a stash directory** with `--init`  
- 📥 **Stash anything** — files, folders, backup dumps, side quests  
- ♻️ **Restore items** via simple `.ds` metadata files  
- 🔄 **Name collision protection** with automatic unique paths  
- 🔐 **Permission-aware** with clear and friendly error messages  

---

## 🔧 Commands at a Glance

| Command | Description |
|---------|-------------|
| `ds --init` | Set your personal stash directory |
| `ds file_or_folder` | Stash a file or directory, leaving a `.ds` placeholder |
| `ds file_or_folder.ds` | Restore a stashed item back to its original location |
| `ds --help` | Show usage instructions |
| `pip install .` | Install DeepStash globally from source |

---

## 🚀 Installation

Clone and install locally:

```bash
git clone https://github.com/YOUR_USERNAME/deepstash.git
cd deepstash
pip install .
```

Or install directly from any folder containing the source:

```bash
pip install .
```

---

## ⚙️ Usage

```bash
ds --init                   # Set your stash directory
ds thesis_draft.docx        # Stash the file, leave a .ds tag
ds thesis_draft.docx.ds     # Restore it exactly where it came from
```

---

## 💡 Sample Session

```bash
$ ds --init
📁 Enter deepstash directory path: /Volumes/Archive
✅ Deepstash directory set to /Volumes/Archive

$ ds mixtape.mp3
📦 Stashed: mixtape.mp3 → /Volumes/Archive/mixtape.mp3

$ ls
 mixtape.mp3.ds

$ ds mixtape.mp3.ds
♻️ Restored: /Users/you/Music/mixtape.mp3
```

---

## 🤖 Note

This utility was built using a method known as **vibe coding** — describing what you want to an AI assistant and refining the results through iteration. No line-by-line planning — just vibes and fast feedback.

---

## 📄 License

Licensed under the [MIT License](LICENSE).
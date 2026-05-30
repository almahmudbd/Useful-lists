# 📂 Useful Lists

**A curated archive of handy tools, synced scripts, and intelligently categorized bookmark collections.**  
The purpose of this repository is to keep all useful digital resources in one place for easy access, automated processing, and backup.

---

## 📜 Synced Markdown Lists

These files are automatically synced from personal Gists every hour using GitHub Actions:

- 🔗 [useful-script-cms-links.md](useful-script-cms-links.md) — A list of useful scripts and CMS-related links.
- 📁 [server-scripts-list.md](server-scripts-list.md) — Handy server-managing scripts and tools collection.
- 🧩 [browser-extension-list.md](browser-extension-list.md) — Favorite browser extensions and productivity tools.
- 🧪 [browser-userscript-list.md](browser-userscript-list.md) — Curated collection of user scripts for browsers.

## 📑 Generated Bookmark Collections

These markdown files are automatically generated from the HTML bookmark export stored in the folder.

- 🏠 [general-collection.md](general-collection.md) — General tools, blogs, and collection.
- 💻 [tech-and-pros.md](tech-and-pros.md) — Technical resources, forums, and developer tools.
- 🌍 [browser-and-servers.md](browser-and-servers.md) — Browser-related tools, VPNs, and server/hosting lists.
- 🎨 [graphic-and-media.md](graphic-and-media.md) — Design assets, stock media, and editor tools.
- 🤖 [ai-collection.md](ai-collection.md) — Some nice AI-related tools and generative platforms.


---
## 📑 Collected Lists

- 🧠 [**New-Ai-Tools.md**](New-Ai-Tools\README.md) — A Huge collection of Ai Tools that found on internet.

-


---

### ⚙️ Automation & Scripts (notes for automation)

The repository uses GitHub Actions to maintain up-to-date data.

### Workflow Details
[![Sync Gist Files](https://github.com/almahmudbd/Useful-lists/actions/workflows/main.yml/badge.svg)](https://github.com/almahmudbd/Useful-lists/actions/workflows/main.yml)

- **Sync Logic**: Every hour, the workflow fetches raw Gist data using `cURL` and commits changes if updates are found.
- **Bookmark Processing**: The collections are generated using a custom Python script.

### Local Rebuild
To manually rebuild the bookmark collections from the latest HTML export:
```bash
python .github/workflows/process_bookmarks.py
```

**pyScript Features**
- Smart Detection: Automatically finds the newest Netscape-style HTML bookmark export (`booky_backup*.html`) file.
- Exclusion Filters: Automatically skips `Download Portal`, `imp:Bookmarks`, and links containing "red" or "risk" keywords.
- AI Collection: Intelligently groups AI-related folders into a dedicated file.
- Regex Logic: Uses whole-word matching to ensure high accuracy in categorization.

---
*Maintained by [almahmudbd](https://github.com/almahmudbd)*

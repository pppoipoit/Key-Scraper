# 💻 LaptopKey Scraper - Elite Edition v2

> 🚀 Elite desktop tool for scraping laptop keyboard images and auto-organizing them by brand & key type.

---

## ✨ Features

- ⚡ **Parallel scraping** — up to 4 URLs at once via `ThreadPoolExecutor`
- 🌙 **Custom Dark UI** — modern dashboard built with Tkinter + Custom PIL Widgets
- 📁 **Auto-folder organization** — brand detection + Korean folder structure (Layout / LARGER / REGULAR / SMALLER)
- 📊 **Live feedback** — gradient progress bar + scrollable log panel
- 📦 **Distributable** — PyInstaller `--onedir` build + Inno Setup installer

---

## 🛠️ Tech Stack

| Tech | Role |
|------|------|
| 🐍 Python | Core language |
| 🖥️ Tkinter | Desktop GUI framework |
| 🎨 Custom PIL Widgets | Gradient cards, rounded buttons, progress bar (Pillow) |
| 🍲 BeautifulSoup4 | HTML parsing |
| 🌐 Requests | HTTP downloading |
| 📦 PyInstaller | `--onedir` executable build |
| 💿 Inno Setup | Windows installer (`Key_Scraper_Setup.exe`) |

---

## 📂 Project Structure

```text
├── main.py              # Entry point — 980x600 window
├── app.py               # UI + ThreadPoolExecutor orchestration
├── scraper_core.py      # Scraping / download logic (no UI deps)
├── gradient_widgets.py  # Custom PIL-rendered widgets
├── theme.py             # Colors, fonts, sizes (single source of truth)
├── requirements.txt     # requests, beautifulsoup4, Pillow
├── Create Installer.iss # Inno Setup script (relative paths)
├── icon.ico             # App icon
```

---

## 🚀 Getting Started

For developers who want to run from source:

```bash
# 1. Clone the repo
git clone https://github.com/pppoipoit/Key-Scraper.git
cd Key-Scraper

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python main.py
```

> 🪟 Requires Windows + Python 3.8+

---

## 📖 How to Use

1. 📋 Paste 1–4 product page URLs (one per line)
2. 📁 Click **Select Destination Folder**
3. ▶️ Click **START EXTRACTION**
4. ✅ Images are saved auto-organized by brand & key type

---

## 🏗️ Build

```bash
# Onedir build (recommended)
python -m PyInstaller --noconsole --onedir --icon=icon.ico --name Key_Scraper main.py

# Then open Create Installer.iss in Inno Setup to compile Key_Scraper_Setup.exe
```

---

## 📜 License

MIT License — Copyright (c) 2026 pppoipoit x DRKMTTR Studio
See [LICENSE](LICENSE) for details.

---

## 🏢 Credits

- 👑 Owner: **DRKMTTR Studio**
- 💻 Portfolio: **pppoipoit**
- 🤖 Built with Elite Dark UI concept

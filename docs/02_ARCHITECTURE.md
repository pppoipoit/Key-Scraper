# Technical Architecture

## System Overview

**Verified**: LaptopKey Scraper - Elite Edition v2 (version 2.0.0) is a desktop GUI application for Windows that scrapes keyboard images from websites and saves them organized by brand and key type.

**Publisher**: DRKMTTR Studio (from Create Installer.iss)

---

## Tech Stack — Verified

| Component | Technology | Source |
|-----------|------------|--------|
| Language | Python 3.x | All `.py` files |
| GUI Framework | tkinter (standard library) | app.py, main.py imports |
| HTTP Client | requests | scraper_core.py line 14 |
| HTML Parser | beautifulsoup4 | scraper_core.py line 15 |
| Image Processing | Pillow (PIL) | gradient_widgets.py, requirements.txt |
| Build Tool | PyInstaller | README.txt section 3 |
| Installer | Inno Setup | Create Installer.iss |

### Dependencies (exact — from requirements.txt)
```
requests
beautifulsoup4
Pillow
```

## Repository Structure — Verified

```
Key Scraper/
├── main.py                 # Entry point — creates window (980x600), sets title "LaptopKey Scraper - Elite Edition v2", loads icon.ico
├── app.py                  # UI composition, event handling, ThreadPoolExecutor for parallel scraping (MAX_PARALLEL_URLS=4)
├── scraper_core.py         # Scraping/download logic — no UI dependencies, standalone-testable
├── gradient_widgets.py     # Custom tkinter widgets using PIL for gradient, rounded corners, shadows
├── theme.py                # Single source of truth for colors, fonts, sizes
├── icon.ico                # App icon (pink-purple gradient theme)
├── Logo_BK.ico             # Alternate icon file present in repo
├── requirements.txt        # Dependencies: requests, beautifulsoup4, Pillow
├── Create Installer.iss    # Inno Setup script for Key_Scraper_Setup.exe
├── README.txt              # Original documentation (English/Thai mix) by Santa Claude
├── dist/                   # Build output (Key_Scraper.exe in onedir/, Key_Scraper_Setup.exe in installer/)
├── LICENSE                 # MIT License (Copyright (c) 2026 pppoipoit x DRKMTTR Studio) — portfolio-ready open-source license
├── .gitignore               # Excludes dist/, build/, *.exe, Python cache, venv/, IDE/OS junk — keeps Clean Slate history free of build artifacts
└── docs/                   # Project documentation
```

## Module Dependency Graph — Verified

```
main.py
  └── imports: theme, app.App
       └── app.py imports: theme, scraper_core (as core), gradient_widgets
            ├── theme.py — constants only, no imports
            ├── scraper_core.py — standalone logic, imports: os, requests, bs4, urllib.parse
            └── gradient_widgets.py — imports: tkinter, PIL (Image, ImageDraw, ImageTk, ImageFilter)
```

**Key design principle**: `scraper_core.py` has zero tkinter imports — it can be tested independently of the UI.

---

## หลักการออกแบบที่สำคัญ

1. **แยก UI กับ logic**: app.py ทำหน้าตา, scraper_core.py ทำงานจริง ไม่พึ่ง tkinter
2. **Theme เป็นแหล่งข้อมูลเดียว**: แก้ theme.py ที่เดียว เรื่อยๆ
3. **Thread safety**: background thread ห้ามแตะ tkinter widget โดยตรง ต้องใช้ `root.after()` อัปเดต UI
4. **อนุรักษ์พฤติกรรมเดิม**: โฟลเดอร์, ชื่อแบรนด์, logic การดาวน์โหลด ห้ามแก้

## UI Architecture — Verified

### Layout Structure (from app.py _build_ui)
- **Window**: 980×600, non-resizable (theme.py: WINDOW_WIDTH=980, WINDOW_HEIGHT=600, root.resizable(False, False))
- **Background**: `#11132A` (theme.py: BG_APP)
- **Header**: App title + berry gradient badge (46×46)
- **Left panel**: Ocean gradient card (300×300) — URL input (multi-line Text with scrollbar) + folder selection
- **Right panel**: Mint gradient card (590×300) — Scrollable log Text widget
- **Action row**: START EXTRACTION button (berry gradient), path display

### Custom Widgets (gradient_widgets.py)
- **GradientPanel**: Rounded rectangle with gradient fill + shadow (PIL-rendered, displayed on tkinter Canvas)
- **GradientButton**: Interactive button with hover state, disabled state, click handler — all PIL-rendered
- **GradientProgressBar**: Horizontal gradient bar showing progress as fraction (0.0–1.0), no percentage text

### Theme Colors (theme.py — verified)
| Variable | Value | Usage |
|----------|-------|-------|
| BG_APP | #11132A | Window background |
| BG_PANEL | #1A1D3A | Card/panel background |
| BG_PANEL_LIGHT | #222648 | Inner panel background |
| TEXT_TITLE | #F5F6FA | Main title (white-blue) |
| TEXT_BODY | #C7CBE8 | General text |
| TEXT_MUTED | #7E84B3 | Secondary text |
| GRADIENT_SUNSET | #FACC15 → #FB7185 | Yellow → pink (98.5% card) |
| GRADIENT_OCEAN | #60A5FA → #2563EB | Blue → navy (2,481 card) |
| GRADIENT_MINT | #34D399 → #0E7490 | Mint → teal (31,124 card, progress bar) |
| GRADIENT_BERRY | #F472B6 → #9333EA | Pink → purple (main button, $2,125 card) |

### Fonts (theme.py — verified)
- Font family: Segoe UI (except log: Consolas)
- Title: Segoe UI 20 bold
- Button: Segoe UI 11 bold
- Log: Consolas 9

## Scraping Pipeline — Verified from scraper_core.py

### Per-URL Flow
```
fetch_page(url) → BeautifulSoup
  ↓
extract_keyboard_image_url(soup) → absolute URL of keyboard image (div.keyboar_wrap > img)
  ↓
get_detail_rows(soup) → list of div.detail_row (excluding head_row)
  ↓
For each row:
  process_row(row, ...) → model_name or None
    1. Find div.f_box → extract model_name text
    2. get_brand_name(model_name) → brand folder name
    3. Create 4 brand folders under base_dir
    4. Find all img tags in row
    5. Download: img[0] → [REGULAR KEY], img[1] → [LARGER KEYS], img[2] → [SMALLER KEYS]
    6. Download keyboard_img_url → [Layout]
```

### Brand Detection (get_brand_name — verified logic)
Extracts leading alphabetic prefix from model name, uppercase, then matches:

| Prefix | Brand Folder |
|--------|-------------|
| AC* | Acer |
| AS* | ASUS |
| MS* | MSI |
| SG* | SAMSUNG |
| D* | DELL |
| H* | HP |
| L* | Lenovo |
| T* | TOSHIBA |
| A* | Apple |
| other | Others |

**Note**: This is prefix-based and may misclassify unusual model names. This is the original logic preserved exactly.

### Image Download (download_image — verified)
- Stream download with `requests.get(stream=True)`
- 1024-byte chunks written to file
- Extension guessed from URL (last segment after `.` before `?`)
- Falls back to `.jpg` if extension > 4 chars or empty
- Headers: `User-Agent: Mozilla/5.0`

## Folder Structure — Verified (exact Korean names from scraper_core.py)

```
<destination_folder>/
├── รูปตัวอย่างแผง Keyboard [Layout]/
│   └── <Brand>/
│       └── <Model>.jpg (or .png, etc.)
├── รูปตัวอย่าง Lugs, Hinge [LARGER KEYS]/
│   └── <Brand>/
│       └── <Model>.jpg
├── รูปตัวอย่าง Lugs, Hinge [REGULAR KEY]/
│   └── <Brand>/
│       └── <Model>.jpg
└── รูปตัวอย่าง Lugs, Hinge [SMALLER KEYS]/
    └── <Brand>/
        └── <Model>.jpg
```

**These folder names must not be modified** — this is ADR-002, explicitly preserved for compatibility.

---

## Threading Model — Verified from app.py

### Architecture
- **Main thread**: Runs tkinter event loop, owns all UI widgets
- **Background thread**: `threading.Thread(target=self.process_scraping, daemon=True)` spawned on button click
- **Parallel workers**: `ThreadPoolExecutor(max_workers=min(4, total_urls))` inside background thread

### Thread Safety Rules (verified in code)
1. UI values (URL text, folder path) **must be read on main thread** before spawning background work
2. Background thread **must not** call `self.url_text.get()` or `self.path_entry.get()` directly — causes `RuntimeError: main thread is not in main loop`
3. All UI updates from background thread **must** go through `root.after(0, callback)`:
   - `safe_log()` → appends to log Text widget
   - `safe_set_progress()` → updates progress bar
   - `safe_toggle_controls()` → enables/disables buttons and inputs
4. A `threading.Lock()` protects shared counters (completed_urls, total_models)

### Known Bug Fixed
A thread-safety bug was discovered and fixed during testing: reading UI widget values from the background thread caused RuntimeError on some Python versions. The fix was to read all UI values on the main thread before starting the background thread.

## Database / Storage — Verified

**No database. No persistent storage.** All data is transient:
- URLs: entered by user each session, stored only in the Text widget
- Downloaded images: saved to user-selected folder on disk (file system only)
- Log: in-memory Text widget, not persisted to file
- No config files, no .env, no SQLite, no registry entries

---

## Authentication / Authorization — Verified

**None.** Single-user desktop application. No login, no user accounts, no API keys.

---

## External Integration — Verified

- **HTTP requests only**: To URLs entered by the user
- **No API keys** in code or configuration
- **Target sites**: Expected HTML structure includes `div.keyboar_wrap`, `div.detail_row`, `div.f_box`, and `img` tags within detail rows
- **No other external services**

---

## Environment Variables — Verified

- **None required** to run the application
- **No .env file** in repository
- `PYTHONPATH` may be needed if running from outside project root

## Build & Distribution — Verified

### PyInstaller Build (README.txt section 3 — verified)
```bash
# Recommended: onedir (faster startup, better for Inno Setup)
python -m PyInstaller --noconsole --onedir --icon=icon.ico main.py

# With custom name
python -m PyInstaller --noconsole --onedir --icon=icon.ico --name "Key_Scraper" main.py
```

Output: `dist\Key_Scraper\` (contains Key_Scraper.exe + _internal/ folder with bundled dependencies and icon.ico)

### Inno Setup Installer (Create Installer.iss — verified)
- **AppName**: Key Scraper
- **AppVersion**: 2.0.0
- **AppId**: {C78F9B64-D1E4-42E3-BCE7-9E4571A2E394}
- **Publisher**: DRKMTTR Studio
- **Output**: Key_Scraper_Setup.exe (LZMA compression, solid compression enabled)
- **Install location**: {autopf}\Key Scraper (Program Files)
- **Options**: Modern wizard style, desktop icon option (unchecked by default), admin privileges required
- **Source path in script**: D:\Google Drive\[Shop] DRKMTTR Studio\[สมศรี Agent]\Key Scraper 2.0\ (local path — needs updating for other machines)

### Existing Build Artifacts (verified on disk)
- `dist\onedir\Key Scraper 2.0\Key_Scraper.exe` (~7.8 MB)

## Known Limitations — Verified from Code

1. **Thread safety**: tkinter widgets must only be accessed from main thread
2. **Target site dependency**: Scraping relies on specific HTML structure (`div.keyboar_wrap`, `div.detail_row`, `div.f_box`); breaks if site changes
3. **Brand detection**: Prefix-based matching may misclassify unusual model names
4. **No retry**: Failed image downloads are logged but not retried
5. **No rate limiting**: Requests sent as fast as ThreadPoolExecutor allows (max 4 concurrent)
6. **No progress percentage**: Progress bar shows fraction of URLs completed, not per-image progress
7. **Fixed window size**: 980×600, non-resizable
8. **Windows icon**: icon.ico may not display on Linux/macOS
9. **No automated tests**: Testing is manual only
10. **No log file**: Logs are in-memory only, lost on close

---

## Architecture Decisions — Reference

See `docs/04_DECISIONS.md` for recorded decisions:
- **ADR-001**: Parallel multi-URL scraping (Implemented)
- **ADR-002**: Preserve exact folder structure and naming (Accepted)
- **ADR-003**: Custom gradient UI via PIL (Implemented)
- **ADR-004**: PyInstaller --onedir + Inno Setup (Implemented)
- **ADR-005**: MIT License & Clean Slate Portfolio (Accepted)

---

## Last Updated

2026-09-15 — Populated from repository source code inspection
- `dist\installer\Key_Scraper_Setup.exe` (~29.3 MB)
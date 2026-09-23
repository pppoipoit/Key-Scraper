# Project Commands

## Prerequisites — Verified

- **Operating System**: Windows (application is Windows-specific due to icon.ico and Inno Setup)
- **Python**: 3.x (code uses f-strings, tkinter — compatible with Python 3.6+)
- **Build tools**: PyInstaller, Inno Setup (for creating distributable .exe)

---

## Verify Installation

### Check Python version
```bash
python --version
```

### Check installed packages
```bash
pip list
```
**Expected packages** (from requirements.txt — verified on disk):
- requests
- beautifulsoup4
- Pillow

---

## Install Dependencies — Verified Command

```bash
pip install -r requirements.txt
```

**requirements.txt content** (exact — verified on disk):
```
requests
beautifulsoup4
Pillow
```

---

## Run Application — Verified

### Development mode (from source)
```bash
python main.py
```

**What happens** (verified from main.py and app.py):
1. `main.py` creates tkinter root window titled "LaptopKey Scraper - Elite Edition v2"
2. Window size: 980×600, non-resizable, background #11132A
3. icon.ico is loaded for title bar icon (if present and on Windows)
4. `App(root)` builds the full UI
5. `root.mainloop()` starts the event loop

### Expected behavior on launch
- Dark dashboard-style window appears
- Left panel: URL input (multi-line) + folder selection button
- Right panel: Scrollable log area
- Bottom: START EXTRACTION button (disabled until folder selected)

---

## Build Distributable — Verified Commands

### Build onedir .exe (recommended — from README.txt)
```bash
python -m PyInstaller --noconsole --onedir --icon=icon.ico main.py
```
Output: `dist\main\` (or `dist\Key_Scraper\` if `--name "Key_Scraper"` is used)

### Build with custom name
```bash
python -m PyInstaller --noconsole --onedir --icon=icon.ico --name "Key_Scraper" main.py
```
Output: `dist\Key_Scraper\` containing:
- `Key_Scraper.exe` (main executable)
- `_internal\` (bundled Python runtime + dependencies + icon.ico)

### Build onefile .exe (single file, slower startup)
```bash
python -m PyInstaller --noconsole --onefile --icon=icon.ico main.py
```
Output: `dist\main.exe` (or `dist\Key_Scraper.exe` with `--name`)

### Verify existing build artifacts (on disk — verified)
- `dist\onedir\Key Scraper 2.0\Key_Scraper.exe` — 7,798,521 bytes (~7.8 MB)
- `dist\installer\Key_Scraper_Setup.exe` — 29,311,454 bytes (~29.3 MB)

## Manual Testing — Verified Steps

Since there are no automated tests, perform these manual tests:

### Test 1: Application Launch
1. Run `python main.py`
2. Verify: Window opens with title "LaptopKey Scraper - Elite Edition v2"
3. Verify: Dark background (#11132A), gradient cards visible
4. Verify: START EXTRACTION button is disabled

### Test 2: Folder Selection
1. Click "Select Destination Folder" button
2. Choose an empty folder
3. Verify: Folder path appears in the path display area
4. Verify: START EXTRACTION button becomes enabled

## Run lint

**สถานะปัจจุบัน:** ไม่มี linter ตั้งค่าไว้  
**คำแนะนำ:** สามารถเพิ่ม flake8 หรือ pylint ได้ในอนาคตหากต้องการ

## Run typecheck

**สถานะปัจจุบัน:** ไม่มี type checking ตั้งค่าไว้  
**คำแนะนำ:** โค้ดไม่มี type hints เพิ่มเติม ปัจจุบันเป็น Python แบบไดนามิก

## Create Installer — Verified

### Using Inno Setup
Open `Create Installer.iss` in Inno Setup Compiler and click "Compile".

**Installer settings** (verified from Create Installer.iss):
- AppName: Key Scraper
- AppVersion: 2.0.0
- Publisher: DRKMTTR Studio
- Output: Key_Scraper_Setup.exe
- Compression: LZMA with solid compression
- Wizard style: Modern
- Default install: {autopf}\Key Scraper (Program Files)
- Desktop icon: Optional (unchecked by default)
- Privileges: Admin required
- Post-install: Launch Key_Scraper.exe (skip if silent)

**⚠️ Important**: The Inno Setup script contains hardcoded local paths:
```
D:\Google Drive\[Shop] DRKMTTR Studio\[สมศรี Agent]\Key Scraper 2.0\
```
These paths must be updated to match the actual build output location on your machine before compiling.

### Test 3: Single URL Scraping
1. Enter one valid URL in the URL text area (one URL per line)
2. Ensure destination folder is selected
3. Click START EXTRACTION
4. Verify: Button changes to "PROCESSING..." and disables
5. Verify: Progress bar moves
6. Verify: Log area shows messages (e.g., "Spying on website now: <url>")
7. Verify: When complete, messagebox shows success/failure
8. Verify: Destination folder contains 4 subfolders with Korean names:
   - `รูปตัวอย่างแผง Keyboard [Layout]`
   - `รูปตัวอย่าง Lugs, Hinge [LARGER KEYS]`
   - `รูปตัวอย่าง Lugs, Hinge [REGULAR KEY]`
   - `รูปตัวอย่าง Lugs, Hinge [SMALLER KEYS]`
9. Verify: Each subfolder contains brand subfolders with downloaded images

### Test 4: Multi-URL Parallel Scraping
1. Enter 2-4 URLs in the URL text area (one per line)
2. Ensure destination folder is selected
3. Click START EXTRACTION
4. Verify: Progress bar shows completion across all URLs
5. Verify: Log shows messages for each URL
6. Verify: All images from all URLs are saved correctly

### Test 5: Error Handling
1. Enter an invalid URL (e.g., "not-a-url")
2. Click START EXTRACTION
3. Verify: Warning messagebox appears "Cannot open web! Check your URL again, Boss!"

### Test 6: Empty URL List
1. Clear all URLs from the text area
2. Click START EXTRACTION
3. Verify: Warning messagebox appears "No URL? Want me to download from heaven or what?!"

### Test 7: No Destination Folder
1. Clear the destination folder path
2. Click START EXTRACTION
3. Verify: Warning messagebox appears "Choose destination folder first!"

## No Commands For

### Database
**None** — this application does not use a database.

### Seed/sample data
**None needed** — users enter their own URLs each session.

### Environment setup
No special environment variables are required. No `.env` file exists in the repository.

### Linting
No linter is configured. To add one:
```bash
pip install flake8
flake8 *.py
```

### Type checking
No type checker is configured. The codebase uses no type hints.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Window opens blank/white | Missing dependencies or corrupted files | Run `pip install -r requirements.txt` |
| START button does nothing | Error occurring silently | Check console output if running from command line |
| "Cannot open web!" error | Invalid URL or no internet | Verify URL is correct and internet connection works |
| No images in destination folder | Website doesn't have expected HTML structure | Verify target page has `div.keyboar_wrap`, `div.detail_row`, `div.f_box`, and `img` tags |
| App freezes/unresponsive | Code modifying UI from background thread | Check that no changes were made to threading code |
| Log messages in English | Log messages are hardcoded in source code | Edit app.py or scraper_core.py to change language |

---

## Last Updated

2026-09-15 — Populated from repository source code inspection
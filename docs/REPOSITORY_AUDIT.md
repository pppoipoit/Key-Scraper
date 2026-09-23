

# Repository Audit — LaptopKey Scraper - Elite Edition v2

**Audit date**: 2026-09-15  
**Auditor**: AI inspection of source code and configuration files  
**Purpose**: Document what exists in the repository, what is verified, what is inferred, and what needs owner confirmation.

---

## Repository Overview

| Attribute | Value | Verification |
|-----------|-------|-------------|
| Project name | LaptopKey Scraper - Elite Edition v2 | Verified: main.py line 33, README.txt line 2 |
| Version | 2.0.0 | Verified: Create Installer.iss line 7 |
| Publisher | DRKMTTR Studio | Verified: Create Installer.iss line 8 |
| App ID | {C78F9B64-D1E4-42E3-BCE7-9E4571A2E394} | Verified: Create Installer.iss line 5 |
| Original author | Santa Claude (ซานต้าคลอดด์ 🎀) | Verified: README.txt line 4 |
| Intended recipient | Tokenmee (เจ้านาย) | Verified: README.txt line 5 |
| Platform | Windows | Verified: .ico icon, Inno Setup |
| Type | Desktop GUI application | Verified: main.py creates tkinter window |

---

## File Inventory — Verified on Disk

### Source Code (6 files, ~44 KB total)

| File | Size | Purpose |
|------|------|---------|
| main.py | 1,609 B | Entry point: creates window, sets icon, starts App |
| app.py | 15,051 B | UI composition, event handling, ThreadPoolExecutor |
| scraper_core.py | 8,110 B | Scraping/download logic, no UI dependencies |
| gradient_widgets.py | 10,630 B | Custom PIL-rendered gradient/rounded widgets |
| theme.py | 2,667 B | Colors, fonts, sizes — single source of truth |
| Create Installer.iss | 1,660 B | Inno Setup script for installer |

### Configuration & Data (3 files)

| File | Size | Purpose |
|------|------|---------|
| requirements.txt | 31 B | Dependencies: requests, beautifulsoup4, Pillow |
| icon.ico | 35,054 B | App icon (pink-purple gradient) |
| Logo_BK.ico | 36,968 B | Alternate icon file (not referenced in code) |

### Build Artifacts (2 files, ~37 MB)

| File | Size | Location |
|------|------|----------|
| Key_Scraper.exe | ~7.8 MB | dist/onedir/Key Scraper 2.0/ |
| Key_Scraper_Setup.exe | ~29.3 MB | dist/installer/ |

---

## Verified Technical Details

### Dependencies (from requirements.txt)
```
requests
beautifulsoup4
Pillow
```

### UI Specifications

| Property | Value | Source |
|----------|-------|--------|
| Window size | 980×600, non-resizable | theme.py, main.py |
| Background | #11132A | theme.py |
| Font | Segoe UI (log: Consolas) | theme.py |
| Title | "LaptopKey Scraper - Elite Edition v2" | main.py |

### Scraping Specifications

| Property | Value | Source |
|----------|-------|--------|
| Max parallel URLs | 4 | app.py: MAX_PARALLEL_URLS |
| Keyboard image | div.keyboar_wrap > img | scraper_core.py |
| Model rows | div.detail_row (no head_row) | scraper_core.py |
| Model name | div.f_box text | scraper_core.py |
| Download order | regular, larger, smaller, layout | scraper_core.py |
| Chunk size | 1024 bytes | scraper_core.py |

### Brand Detection (get_brand_name)

| Prefix | Brand |
|--------|-------|
| AC | Acer |
| AS | ASUS |
| MS | MSI |
| SG | SAMSUNG |
| D | DELL |
| H | HP |
| L | Lenovo |
| T | TOSHIBA |
| A | Apple |
| other | Others |

### Folder Names (must not be modified — ADR-002)

1. `รูปตัวอย่างแผง Keyboard [Layout]`
2. `รูปตัวอย่าง Lugs, Hinge [LARGER KEYS]`
3. `รูปตัวอย่าง Lugs, Hinge [REGULAR KEY]`
4. `รูปตัวอย่าง Lugs, Hinge [SMALLER KEYS]`

---

## Verified Build System

### PyInstaller Command
```bash
python -m PyInstaller --noconsole --onedir --icon=icon.ico main.py
```

### Inno Setup Details
- AppName: Key Scraper
- AppVersion: 2.0.0
- Publisher: DRKMTTR Studio
- Compression: LZMA with solid compression
- Admin privileges required

### ⚠️ Hardcoded Paths in Create Installer.iss
```
D:\Google Drive\[Shop] DRKMTTR Studio\[สมศรี Agent]\Key Scraper 2.0\
```
These paths must be updated before compiling on a different machine.

---

## Items Requiring Owner Confirmation

### 🔴 High Priority
1. **Inno Setup hardcoded paths** — Cannot rebuild installer without updating
2. **Logo_BK.ico purpose** — Exists but not referenced in code
3. **Target website(s)** — Need to know which sites the app scrapes
4. **Whether automated tests are wanted** — Currently none exist

### 🟡 Medium Priority
5. Whether folder structure can ever change (ADR-002 says "do not modify")
6. Whether 4-folder layout is correct for all use cases
7. Whether multi-language support is needed
8. Is "DRKMTTR Studio" the correct publisher name?

### 🟢 Low Priority
9. Theme color origins (referenced from "Dark Dashboard" image)
10. Whether window should be resizable
11. Scrollbar sufficiency on URL and log panels

---

## Documentation Completeness

### ✅ Fully Populated
- `docs/02_ARCHITECTURE.md` — Updated with verified content
- `docs/PROJECT_COMMANDS.md` — Updated with verified content
- `docs/HANDOFF.md` — Updated with verified content

### 📝 Needs Work
- `docs/QA_CHECKLIST.md` — Template
- `docs/GLOSSARY.md` — Template
- `docs/CHANGELOG.md` — Template
- `docs/OPEN_QUESTIONS.md` — Has questions
- `docs/workflows/*.md` — 6 workflow files
- Owner manuals (5 files)

---

## Security Audit

### ✅ No Secrets Found
- No `.env` file
- No API keys, passwords, tokens in source code
- No hardcoded credentials
- Create Installer.iss contains only local paths

### ⚠️ Notes
- Create Installer.iss paths reveal Google Drive folder structure
- Logo_BK.ico present but unused

---

## Repository Health

| Aspect | Status |
|--------|--------|
| Code organization | ✅ Good |
| Thread safety | ✅ Fixed (bug documented) |
| Dependencies | ✅ Minimal (3 runtime) |
| Build system | ✅ Functional |
| Documentation | ⚠️ Partial (many templates remain) |
| Testing | ❌ Missing |
| Security | ✅ Good |

---

## Last Updated

2026-09-15 — Created from thorough source code inspection

| Attribute | Value | Verification |
|-----------|-------|-------------|
| Project name | LaptopKey Scraper - Elite Edition v2 | Verified: main.py line 33, README.txt line 2 |
| Version | 2.0.0 | Verified: Create Installer.iss line 7 |
| Publisher | DRKMTTR Studio | Verified: Create Installer.iss line 8 |
| App ID | {C78F9B64-D1E4-42E3-BCE7-9E4571A2E394} | Verified: Create Installer.iss line 5 |
| Original author | Santa Claude (ซานต้าคลอดด์ 🎀) | Verified: README.txt line 4 |
| Intended recipient | Tokenmee (เจ้านาย) | Verified: README.txt line 5 |
| Platform | Windows | Verified: .ico icon, Inno Setup |
| Type | Desktop GUI application | Verified: main.py creates tkinter window |

---

## File Inventory — Verified on Disk

### Source Code (6 files, ~44 KB total)

| File | Size | Purpose |
|------|------|---------|
| main.py | 1,609 B | Entry point: creates window, sets icon, starts App |
| app.py | 15,051 B | UI composition, event handling, ThreadPoolExecutor |
| scraper_core.py | 8,110 B | Scraping/download logic, no UI dependencies |
| gradient_widgets.py | 10,630 B | Custom PIL-rendered gradient/rounded widgets |
| theme.py | 2,667 B | Colors, fonts, sizes — single source of truth |
| Create Installer.iss | 1,660 B | Inno Setup script for installer |

### Configuration & Data (3 files)

| File | Size | Purpose |
|------|------|---------|
| requirements.txt | 31 B | Dependencies: requests, beautifulsoup4, Pillow |
| icon.ico | 35,054 B | App icon (pink-purple gradient) |
| Logo_BK.ico | 36,968 B | Alternate icon file (not referenced in code) |

### Build Artifacts (2 files, ~37 MB)

| File | Size | Location |
|------|------|----------|
| Key_Scraper.exe | ~7.8 MB | dist/onedir/Key Scraper 2.0/ |
| Key_Scraper_Setup.exe | ~29.3 MB | dist/installer/ |

---

## Verified Technical Details

### Dependencies (from requirements.txt)
```
requests
beautifulsoup4
Pillow
```

### UI Specifications

| Property | Value | Source |
|----------|-------|--------|
| Window size | 980×600, non-resizable | theme.py, main.py |
| Background | #11132A | theme.py |
| Font | Segoe UI (log: Consolas) | theme.py |
| Title | "LaptopKey Scraper - Elite Edition v2" | main.py |

### Scraping Specifications

| Property | Value | Source |
|----------|-------|--------|
| Max parallel URLs | 4 | app.py: MAX_PARALLEL_URLS |
| Keyboard image | div.keyboar_wrap > img | scraper_core.py |
| Model rows | div.detail_row (no head_row) | scraper_core.py |
| Model name | div.f_box text | scraper_core.py |
| Download order | regular, larger, smaller, layout | scraper_core.py |
| Chunk size | 1024 bytes | scraper_core.py |

### Brand Detection (get_brand_name)

| Prefix | Brand |
|--------|-------|
| AC | Acer |
| AS | ASUS |
| MS | MSI |
| SG | SAMSUNG |
| D | DELL |
| H | HP |
| L | Lenovo |
| T | TOSHIBA |
| A | Apple |
| other | Others |

### Folder Names (must not be modified — ADR-002)

1. `รูปตัวอย่างแผง Keyboard [Layout]`
2. `รูปตัวอย่าง Lugs, Hinge [LARGER KEYS]`
3. `รูปตัวอย่าง Lugs, Hinge [REGULAR KEY]`
4. `รูปตัวอย่าง Lugs, Hinge [SMALLER KEYS]`

---

## Verified Build System

### PyInstaller Command
```bash
python -m PyInstaller --noconsole --onedir --icon=icon.ico main.py
```

### Inno Setup Details
- AppName: Key Scraper
- AppVersion: 2.0.0
- Publisher: DRKMTTR Studio
- Compression: LZMA with solid compression
- Admin privileges required

### ⚠️ Hardcoded Paths in Create Installer.iss
```
D:\Google Drive\[Shop] DRKMTTR Studio\[สมศรี Agent]\Key Scraper 2.0\
```
These paths must be updated before compiling on a different machine.

---

## Items Requiring Owner Confirmation

### 🔴 High Priority
1. **Inno Setup hardcoded paths** — Cannot rebuild installer without updating
2. **Logo_BK.ico purpose** — Exists but not referenced in code
3. **Target website(s)** — Need to know which sites the app scrapes
4. **Whether automated tests are wanted** — Currently none exist

### 🟡 Medium Priority
5. Whether folder structure can ever change (ADR-002 says "do not modify")
6. Whether 4-folder layout is correct for all use cases
7. Whether multi-language support is needed
8. Is "DRKMTTR Studio" the correct publisher name?

### 🟢 Low Priority
9. Theme color origins (referenced from "Dark Dashboard" image)
10. Whether window should be resizable
11. Scrollbar sufficiency on URL and log panels

---

## Documentation Completeness

### ✅ Fully Populated
- `docs/02_ARCHITECTURE.md` — Updated with verified content
- `docs/PROJECT_COMMANDS.md` — Updated with verified content
- `docs/HANDOFF.md` — Updated with verified content

### 📝 Needs Work
- `docs/QA_CHECKLIST.md` — Template
- `docs/GLOSSARY.md` — Template
- `docs/CHANGELOG.md` — Template
- `docs/OPEN_QUESTIONS.md` — Has questions
- `docs/workflows/*.md` — 6 workflow files
- Owner manuals (5 files)

---

## Security Audit

### ✅ No Secrets Found
- No `.env` file
- No API keys, passwords, tokens in source code
- No hardcoded credentials
- Create Installer.iss contains only local paths

### ⚠️ Notes
- Create Installer.iss paths reveal Google Drive folder structure
- Logo_BK.ico present but unused

---

## Repository Health

| Aspect | Status |
|--------|--------|
| Code organization | ✅ Good |
| Thread safety | ✅ Fixed (bug documented) |
| Dependencies | ✅ Minimal (3 runtime) |
| Build system | ✅ Functional |
| Documentation | ⚠️ Partial (many templates remain) |
| Testing | ❌ Missing |
| Security | ✅ Good |

---

## Last Updated

2026-09-15 — Created from thorough source code inspection
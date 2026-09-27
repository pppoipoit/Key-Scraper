# 🎉 LaptopKey Scraper — Elite Edition v2.1.0

## Production Ready Release

**Commit:** `726ad3f`
**Release Date:** 2026-09-28
**Status:** ✅ Closed — Production Verified

This release marks the project as **complete and production-ready** after comprehensive hardening, testing, and verification across all target Windows versions.

---

### 🚀 What's New in v2.1.0

#### 🛡️ Two-Layer Retry Mechanism
- **Page-level retry:** `fetch_page()` retries up to 3 times (2-second delay) on network failures and HTTP 5xx errors
- **Image-level retry:** `download_image()` retries up to 3 times on individual image download failures
- **Smart retry policy:** Fails immediately on HTTP 4xx client errors — no wasted attempts on unrecoverable failures
- **Thread-safe:** All retries happen in background worker threads, UI stays fully responsive

#### 🧪 Automated Test Suite (26 tests)
- **26 tests running offline in ~0.035s** using only Python's stdlib `unittest`
- Covers:
  - Brand detection mapping (AC→Acer, AS→ASUS, MS→MSI, SG→SAMSUNG, D→DELL, H→HP, L→Lenovo, T→TOSHIBA, A→Apple, unknown→Others) — enforces **ADR-002**
  - Korean folder name preservation (Layout / LARGER KEYS / REGULAR KEY / SMALLER KEYS)
  - Both page-level and image-level retry logic (success, exhaustion, no-retry-on-404, no-retry-on-non-network-error)
  - URL joining, header-row filtering, and all core pure functions
- **Run command:** `python -m unittest discover tests`
- Tests actively catch regressions in ADR-002 rules — any future change that breaks folder naming or brand logic will be caught automatically

#### 💻 Windows Compatibility — Owner Verified
- **Single Python 3.8.x build supports Windows 7, 10, and 11**
- Installer rebuilt on 2026-09-28 using Python 3.8.10 — verified running on actual Windows 7 machine by the owner
- `Pillow<=9.5.0` pinned to preserve Win7 compatibility
- ⚠️ **Important:** Any exe built with Python 3.9+ will fail on Windows 7 with `api-ms-win-core-path-l1-1-0.dll is missing`. This release's installer was built correctly with Python 3.8.

#### 🏠 GitHub Portfolio & Licensing
- **Clean Slate operation:** Repository scrubbed of all build artifacts, hardcoded local paths, and IDE junk
- **MIT License** (Copyright © 2026 pppoipoit x DRKMTTR Studio)
- Professional README with tech stack, features, and getting-started guide
- 23+ documentation files covering architecture, decisions, workflows, and owner manuals

#### 📦 Installer
- **Inno Setup installer included as release asset** (freshly built 2026-09-28)
- Clean relative paths in `Create Installer.iss` — can be recompiled on any machine
- Installs to `{autopf}\Key Scraper` with optional desktop shortcut
- Note: supersedes v2.0.0's "binaries not hosted" statement — the Windows 7-verified installer is attached to this release.

---

### 🏗️ Architecture Decisions (Recorded)

| ADR | Title | Status |
|-----|-------|--------|
| ADR-001 | Parallel multi-URL scraping (max 4 concurrent) | Implemented |
| ADR-002 | Preserve exact Korean folder structure & brand logic | Accepted (enforced by tests) |
| ADR-003 | Custom gradient UI via PIL | Implemented |
| ADR-004 | PyInstaller --onedir + Inno Setup | Implemented |
| ADR-005 | MIT License & Clean Slate Portfolio | Accepted |
| ADR-006 | Single Build for All Windows Versions | Accepted |

---

### 🎯 Open Questions Status (Final)

| ID | Question | Status |
|----|----------|--------|
| OQ-001 | Target website | ✅ Answered: `laptopkey.com` |
| OQ-002 | Configurable parallel URLs | ✅ Answered: NO |
| OQ-003 | Persistent log file | ✅ Answered: NO |
| OQ-004 | Export URL list | ✅ Answered: NO |
| OQ-005 | macOS/Linux support | ✅ Answered: NO |
| OQ-006 | Automated tests | ✅ Implemented (26 tests) |
| OQ-007 | Alternative brand detection | ⏸️ Deferred (prefix-based acceptable) |
| OQ-008 | Retry on failure | ✅ Implemented (2 layers) |

---

### 🛠️ How to Build from Source

```bash
pip install -r requirements.txt
python -m PyInstaller --noconsole --onedir --icon=icon.ico --name "Key_Scraper" main.py
```

Or use the included installer for a one-click setup.

### 🧪 How to Run Tests

```bash
python -m unittest discover tests
```

Expected output: `Ran 26 tests in ~0.03s — OK`

---

### 🙏 Credits

**© 2026 pppoipoit x DRKMTTR Studio**

Built with AI-assisted development workflow (Cline on VS Code).

---

**Project Status: CLOSED — Production Ready** ✅

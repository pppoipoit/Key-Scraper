# Changelog

ประวัติการเปลี่ยนแปลงทั้งหมดของ LaptopKey Scraper - Elite Edition
รูปแบบ: [Semantic Versioning](https://semver.org/lang/th/)

## [2.1.0] - 2026-09-28

### 🎉 Production Ready Release — **Windows 7 owner-verified**

This release marks the project as **Production Ready**, **closed**, and **verified working on Windows 7** by the owner on 2026-09-28.

- **Release published publicly via gh CLI with attached Windows 7-verified installer** (11,365,375 bytes).

#### 🔧 Fixed — Windows 7 compatibility (owner-verified)
- **The distributed exe was rebuilt with Python 3.8.10.** The previously distributed build failed on Windows 7 with `api-ms-win-core-path-l1-1-0.dll is missing`. Root cause confirmed by static PE import analysis, not guessed: the old bundle shipped **`python313.dll`**, which imports `api-ms-win-core-path-l1-1-0.dll` — an API set Windows 7 does not provide. (The old bundle also shipped `cryptography\_rust.pyd`, importing `api-ms-win-core-synch-l1-2-0.dll` — a second Win7 blocker — plus `numpy` and `lxml`, none of which are in `requirements.txt`.)
- **Rebuilt artifact:** `dist\Key_Scraper\Key_Scraper.exe` (2,599,618 bytes) built with Python **3.8.10** + PyInstaller 6.22.3. Bundles `python38.dll`; a scan of all 31 `.exe`/`.dll`/`.pyd` files found **zero** post-Win7 API-set imports. `python -m unittest discover tests` → `Ran 26 tests — OK`.
- **Rebuilt installer:** `dist\installer\Key_Scraper_Setup.exe` (11,365,375 bytes) built with Inno Setup 7.0.1-beta. `Create Installer.iss` line 28 was repointed from the 3.13 build to the 3.8 build, so the installer can no longer silently repackage a Windows 7-broken artifact. Verified: silent install (exit 0), only `python38.dll` installed, app launched, installer itself imports no post-Win7 API set.
- **PyInstaller 6.22.3 confirmed usable for Windows 7 targets.** Its "runs in Windows 8 and newer" note refers to the *build* machine, not the destination; the 6.22.3 Windows bootloader itself imports no post-Win7 API sets. No dependency downgrade was needed.
- **✅ Owner verification (2026-09-28):** the rebuilt exe was run on a real Windows 7 PC and launched **without** the `api-ms-win-core-path-l1-1-0.dll` error.

#### ⚠️ Deprecated
- **All pre-2026-09-28 build artifacts, including the old `dist\installer\Key_Scraper_Setup.exe` (29,311,454 bytes) and `dist\onedir\Key Scraper 2.0\`.** They are Python 3.13 builds and are **not** Windows 7 compatible. Only the rebuilt `dist\Key_Scraper\` supports Windows 7.

#### ⚠️ Build rule (must not be forgotten)
- **The build MUST be performed with Python 3.8.x.** A build made with Python 3.9+ will not run on Windows 7. See `docs/WINDOWS_COMPATIBILITY.md` for the warning box and the 5-second `python38.dll` vs `python313.dll` check.

#### 📖 Documentation
- `docs/WINDOWS_COMPATIBILITY.md`: critical warning box, 5-second check, verified-build record, evidence table for the old failure.
- `docs/HANDOFF.md`: status set to Closed (v2.1.0), Win7 verification row added, known limitations updated to owner-verified.
- `docs/OPEN_QUESTIONS.md`: OQ-006 / OQ-008 Implemented, **OQ-007 now Deferred** (owner decision 2026-09-28).
- `docs/CURRENT_TASK.md`: project marked **CLOSED**.
- No `.py` source files were modified; no Korean folder names or ADR-002 logic touched.

#### Added
- **Retry Mechanism (2 layers):**
  - Page-level retry: `fetch_page()` now retries up to 3 times on network failures and HTTP 5xx errors
  - Image-level retry: `download_image()` retries up to 3 times on download failures
  - Smart retry: Fails immediately on HTTP 4xx (no point retrying client errors)
  - 2-second delay between retry attempts (`DOWNLOAD_RETRY_DELAY_SECONDS = 2`, `DOWNLOAD_MAX_RETRIES = 3` — one shared constant pair for both layers)
- **Automated Test Suite (26 tests):**
  - Full test coverage for brand detection logic (ADR-002 compliance)
  - Test coverage for retry mechanisms (both page and image level)
  - Test coverage for Korean folder names preservation
  - All tests run offline in <0.1s using `unittest` (no external dependencies)
  - Run command: `python -m unittest discover tests`
  - Verified: `Ran 26 tests in 0.087s — OK` (Python 3.8.10, all HTTP calls mocked)
- **GitHub Portfolio Setup:**
  - Clean Slate operation: Removed all build artifacts and local paths from git history
  - MIT License (Copyright 2026 pppoipoit x DRKMTTR Studio)
  - Professional README.md with tech stack and features
  - Comprehensive documentation (22 files in `docs/` including 5 owner manuals, plus 6 workflow guides and 7 rule files in `.clinerules/`)
- **Windows Compatibility:**
  - Single build supports Windows 7, 10, and 11
  - Python 3.8.x requirement documented
  - Pillow<=9.5.0 pinned for Windows 7 compatibility

#### Changed
- Simplified build: Removed separate Win7/Win10 scripts (`build_win7.bat`, `build_win10.bat`, `requirements-win7.txt`, `requirements-win10.txt`), unified to a single build approach
- Documentation truth: Stale claims about hardcoded local paths removed from `docs/PROJECT_COMMANDS.md`, `docs/REPOSITORY_AUDIT.md`, `docs/HANDOFF.md`, `docs/02_ARCHITECTURE.md`
- ADR-005: MIT License & Clean Slate Portfolio (Accepted)
- ADR-006: Single Build for All Windows Versions (Accepted)

#### Fixed
- Documentation claimed `Create Installer.iss` used hardcoded local paths — it actually uses clean relative paths (`dist\installer`, `dist\onedir\Key Scraper 2.0\*`); the false warnings were removed
- Thread-safety bug (fixed in the original code before v2.0.0, now formally recorded in `docs/02_ARCHITECTURE.md` and `docs/HANDOFF.md`)

#### Technical Details
- 26 automated tests covering core logic
- Retry logic isolated to background worker threads (UI never freezes)
- All ADR-002 rules enforced by automated tests
- Zero UI changes — `app.py`, `main.py`, `gradient_widgets.py`, `theme.py` untouched since the v2.0.0 clean slate (verified via `git diff 49c344d..HEAD`)

#### Known Limitations Carried Into This Release
These are pre-existing and remain open — they are not regressions from v2.1.0:
- `ISSUE-001` (`docs/KNOWN_ISSUES.md`): `main.py` uses `os.path.dirname(os.path.abspath(__file__))` instead of a `get_base_path()` / `sys._MEIPASS` check, so the window icon may not resolve when running from a PyInstaller bundle
- `ISSUE-002` (`docs/KNOWN_ISSUES.md`): `app.py` still uses `left_w, right_w = 300, 590` (log panel wider than URL panel) rather than the `590, 300` layout described in the audit
- `ISSUE-003`: both `icon.ico` and `Logo_BK.ico` are present; `Logo_BK.ico` is unreferenced
- UI and threading behaviour are still verified manually — no automated coverage

---

**Previous release**: [2.0.1] - 2026-09-27 (single-build simplification) · [2.0.0] - 2026-09-23 (Clean Slate / portfolio-ready, commit `49c344d`)

---

## [2.0.1] - 2026-09-27

### Changed

- Simplified build: removed separate Win7/Win10 build scripts
- Single `requirements.txt` with `Pillow<=9.5.0` for universal Windows support
- Updated documentation to reflect single-build approach

### Removed

- `build_win7.bat`, `build_win10.bat`
- `requirements-win7.txt`, `requirements-win10.txt`

---


## [2.0.0] - 2026-06-23

(จาก README.txt — เป็นเวอร์ชันปัจจุบันใน repository)

### Added

- รองรับใส่ URL หลายอันพร้อมกัน (1 บรรทัด = 1 ลิงก์) ในช่อง TARGET URLs
- ระบบดูดข้อมูลพร้อมกันสูงสุด 4 URL (จะปรับได้ที่ MAX_PARALLEL_URLS ใน app.py)
- ช่อง Log และช่อง URL เลื่อนเมาส์ขึ้น-ลงได้ (มี scrollbar)
- แถบ progress bar แบบ gradient บอกว่าทำงานไปกี่ URL แล้ว
- UI ธีมเข้มสไตล์ dashboard ตามภาพตัวอย่าง (gradient + เงา + มุมโค้ง)
- ไอคอนที่ title bar (ใช้ icon.ico หรือเปลี่ยนเป็นไฟล์ของเจ้าของเองได้)
- icon.ico ไฟล์ไอคอน (โทนชมพู-ม่วงตามธีม)

### Fixed

- แก้บัค thread-safety ระหว่างเทสต์ (อ่านค่ากล่อง URL/destination ต้องทำที่ main thread เท่านั้น)

### Verified (จาก README.txt)

- Logic ดาวน์โหลด/แยกโฟลเดอร์ตรงกับ Key_Scraper.py ต้นฉบับ 100% (เทสต์เทียบ byte-by-byte)
- ทดสอบ end-to-end ผ่าน UI จริง: หลาย URL → log/progress/ปุ่ม Start อัพเดทถูกต้อง → โฟลเดอร์รวมไม่เพี้ยน
- โครงสร้างโฟลเดอร์ 4 หมวด + ชื่อแบรนด์ ไม่ถูกแก้ไขเลย

---

## [เดิมก่อน v2.0.0] - จาก README.txt

(สรุปจากข้อความใน README.txt ที่อ้างอิงถึง Key_Scraper.py เดิม)

- เคยเป็น Key_Scraper.py เวอร์ชันแรก (ทำงานทีละ 1 URL)
- v2 ได้แยก logic ออกมาเป็น scraper_core.py เพื่อรองรับ parallel processing

---

หมายเหตุ (แก้ไข 2026-09-27): ข้อความเดิมในไฟล์นี้ระบุว่า "ยังไม่มี Git tags" — **ไม่จริงแล้ว**
ตรวจสอบด้วย `git tag --list` และ `git ls-remote --tags origin` เมื่อ 2026-09-27 พบว่า tag `v2.0.0` มีอยู่จริง
และถูก push ไปที่ origin แล้ว (ชี้ไปที่ commit `b2288c6`) ส่วน GitHub CLI (`gh`) **มีติดตั้งอยู่** ที่
`C:\Program Files\GitHub CLI\gh.exe` — ข้อความเดิมที่ระบุว่าไม่ได้ติดตั้งจึงไม่ถูกต้อง

---

## [v2.0.0] — Clean Slate Release (2026-09-23, commit 49c344d)

**Fact**: Single root-commit history force-pushed to `origin main` (https://github.com/pppoipoit/Key-Scraper.git).
No source-code changes in this release — docs bookkeeping only (CURRENT_TASK, HANDOFF, CHANGELOG).

**Release status (verified 2026-09-27)**: tag `v2.0.0` **exists and is pushed to origin** (`git ls-remote --tags origin` → `b2288c6 refs/tags/v2.0.0`).
Whether a GitHub *Release page* (as opposed to the tag) has been published was **not verifiable** from this machine — `gh` is installed but no authenticated check was run in this task. Confirm at https://github.com/pppoipoit/Key-Scraper/releases

**Release notes for owner to paste** (title: ✨ Elite Edition v2.0.0 — Clean Slate & Portfolio Ready):

🎉 **Initial Public Release: Elite Edition v2.0.0**

This is the 'Clean Slate' release of the LaptopKey Scraper. The repository has been completely restructured for professional portfolio showcase.

**What's included in v2.0.0:**
- 🚀 Parallel multi-URL scraping engine (up to 4 concurrent threads via ThreadPoolExecutor)
- 🎨 Custom Dark UI with PIL-rendered gradient widgets
- 📂 Automated brand detection and Korean/English folder structuring
- 🛡️ Thread-safe UI architecture (root.after() pattern)
- 📦 Ready-to-build Inno Setup configuration (relative paths)

**Tech Stack:** Python 3.x | Tkinter | Pillow | BeautifulSoup4 | Requests | PyInstaller

*Note: Compiled binaries (.exe) are not hosted on GitHub to keep the repository clean. Build from source using PyInstaller.*

**© 2026 pppoipoit x DRKMTTR Studio**
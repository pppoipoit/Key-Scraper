# Current Task

## Task ID and title

TC-006 — Rebuild distributable exe with Python 3.8 for Windows 7 compatibility

## Status

**Completed** (2026-09-28) — exe rebuilt with Python 3.8.10 into `dist\Key_Scraper\`, root cause of the Windows 7 failure confirmed by static PE import analysis, docs updated (WINDOWS_COMPATIBILITY / HANDOFF / CHANGELOG), committed + pushed to main.

**Repository state**: no `.py` file was modified. The previously distributed artifact was a **Python 3.13** build (`python313.dll` imports `api-ms-win-core-path-l1-1-0.dll` — the exact error the owner reported on Windows 7). The fresh build bundles `python38.dll` and imports **zero** post-Win7 API sets across all 31 bundled binaries. Korean folder names and ADR-002 logic untouched.

**Validation actually run**: `python -m unittest discover tests` → `Ran 26 tests — OK` · launch smoke test → GUI alive after 8s · `python --version` → 3.8.10 · build log header `Python: 3.8.10`.

**Remaining manual step (owner)**: copy `dist\Key_Scraper\` to the Windows 7 PC and run it once. No physical Windows 7 machine was available for testing.

**Next task**: none queued — owner picks the next item (OQ-007 still needs owner input; see `docs/OPEN_QUESTIONS.md` and `docs/05_BACKLOG.md`).

---

## Previous task

TC-002 (follow-up) — Extend Retry Mechanism to `fetch_page()` in scraper_core.py

### Status

**Completed** (2026-09-27) — retry now covers image downloads **and** page fetching, 26 unit tests passing (`python -m unittest discover tests`), docs updated, committed + pushed to main.

**Repository state**: core scraping logic retries transient failures at both levels, and the pure core logic has automated test coverage. `app.py`, `main.py`, `gradient_widgets.py`, `theme.py` untouched (PM constraint).

**Next task**: none queued — owner picks the next item (OQ-007 still needs owner input; see `docs/OPEN_QUESTIONS.md` and `docs/05_BACKLOG.md`).

## Goal

Complete OQ-008 so that resilience is comprehensive: a temporary network problem while loading a product page must not cost the user the *entire page* of images. Previously only individual image downloads were retried — a hiccup during the initial page load skipped the whole URL.

## Scope

- `scraper_core.py`: `fetch_page()` body wrapped in a retry loop reusing `DOWNLOAD_MAX_RETRIES = 3` and `DOWNLOAD_RETRY_DELAY_SECONDS = 2` (same constants as `download_image()`)
  - Retries on `requests.exceptions.RequestException` (timeout / connection / DNS) and HTTP 5xx
  - HTTP 4xx and non-request exceptions fail immediately (retry cannot help)
  - `time.sleep()` inside the function is safe: the function only ever runs inside a `ThreadPoolExecutor` worker thread (`app.py` → `process_scraping`)
  - **Signature and return value unchanged** — still `(url, log_callback=None)` → `BeautifulSoup` or `None`; still a pure function with no UI dependency
  - User-facing message `"Cannot open web! Check your URL again, Boss!"` preserved
- `tests/test_scraper_core.py`: +7 tests (`TestFetchPageRetry`), 26 total, stdlib `unittest` + `unittest.mock` only (no new dependencies)
  - `requests.get` and `time.sleep` are mocked → tests run offline in ~0.04s
  - 4xx/5xx are simulated the way `requests` really behaves: the mock's `raise_for_status()` raises a real `requests.exceptions.HTTPError`
- docs: `OPEN_QUESTIONS.md` (OQ-008 now covers both page fetching and image downloads), `HANDOFF.md`, `CHANGELOG.md`, `CURRENT_TASK.md`, `PROJECT_COMMANDS.md`, `QA_CHECKLIST.md`

## Non-goals

- No changes to `app.py`, `main.py`, `gradient_widgets.py`, `theme.py`
- No changes to brand detection logic or Korean folder names (ADR-002)
- No changes to the position-based image download logic (`img[0]` = regular, `img[1]` = larger, `img[2]` = smaller — locked)
- No threading model changes; no tkinter import and no `root.after()` in `scraper_core.py` or `tests/`
- No new dependencies (stdlib `unittest` only)
- No new retry constants, no helper class, no refactor of other functions — the retry logic is isolated inside `fetch_page()`
- No change to `fetch_page()`'s signature or return type

## Acceptance criteria

- [x] `fetch_page()` retries up to 3 times (4 attempts total) with a 2-second wait on network errors and HTTP 5xx
- [x] HTTP 4xx (404 / 403 / 401) fails immediately with no retry and no sleep
- [x] Non-network errors fail immediately with no retry
- [x] Each retry is logged clearly as `Retry <n>/3 for <url> in 2s | <reason>`
- [x] After all retries are exhausted, `fetch_page()` returns `None` (does not raise), and the caller `process_single_url()` skips the URL as before
- [x] `fetch_page()` signature and return value unchanged (`BeautifulSoup` or `None`) — still pure
- [x] `download_image()` retry behaviour unchanged (19 pre-existing tests still pass)
- [x] `tests/test_scraper_core.py` extended with page-fetch retry tests; all HTTP calls mocked
- [x] `python -m unittest discover tests` passes (26 tests, offline)
- [x] OQ-008 notes that retry covers BOTH image downloads and page fetching
- [x] `docs/HANDOFF.md` (Current Product State + Recent changes) and `docs/CHANGELOG.md` ([Unreleased]) updated
- [x] Commit + push to `main` succeeds

## Flagged issues — RESOLVED / CLOSED (2026-09-27, Boss approved final docs polish)

- [x] **RESOLVED** — ADR numbering conflict: single-build decision recorded as **ADR-006** ("Single Build for All Windows Versions", Accepted) in docs/04_DECISIONS.md, docs/WINDOWS_COMPATIBILITY.md, docs/02_ARCHITECTURE.md, and docs/HANDOFF.md
- [x] **RESOLVED** — docs/CHANGELOG.md stale "separate builds" / deleted-files entries removed in the previous docs-cleanup commit
- [x] **RESOLVED** — hardcoded-path claims removed from docs/PROJECT_COMMANDS.md, docs/REPOSITORY_AUDIT.md, docs/HANDOFF.md, and docs/02_ARCHITECTURE.md (Create Installer.iss verified to use clean relative paths)
- [x] **RESOLVED** — docs/REPOSITORY_AUDIT.md accidental duplicate copy (former lines ~191–369) deleted; one clean copy remains

**No open documentation issues remain.**

## Validation results (2026-09-27)

- `python -m unittest discover tests -v` → **Ran 26 tests ... OK** (0.031s, offline) — 19 pre-existing + 7 new page-fetch retry tests
- `python -c "import scraper_core"` → OK (Python 3.8.10; deps installed with the documented `pip install -r requirements.txt`)
- Signature check → `fetch_page(url, log_callback=None)` unchanged; returns `BeautifulSoup` or `None`
- Lint / typecheck → **Not run** — none configured in this repository (see `docs/PROJECT_COMMANDS.md`)
- Manual UI test → **Not run in this session** — the retry runs in the background worker thread and changes no UI element; a manual re-check is suggested (steps in `docs/PROJECT_COMMANDS.md`)

## Owner approval

**Approved** — PM (Mo-Mo) and Boss approved TC-002 (retry + automated tests) on 2026-09-27, and Boss approved extending the retry to `fetch_page()` on 2026-09-27.

## Environment check result (2026-09-27)

- `python --version` → **Python 3.8.10** (Windows 7-compatible ✅)
- `pip list` → requests / beautifulsoup4 / Pillow were **NOT installed** on this machine (PyInstaller 6.22.3 present). Installed the already-declared dependencies with `pip install -r requirements.txt` so the test suite could import `scraper_core`. **No new dependency was added to `requirements.txt`.**

## Work log

### TC-002 (original — retry for image downloads)

- Read core docs (HANDOFF, CURRENT_TASK, DECISIONS, PROJECT_COMMANDS, QA_CHECKLIST, OPEN_QUESTIONS) per `.clinerules/00-core-workflow.md`
- Verified `download_image()` only ever runs inside the `ThreadPoolExecutor` worker (`app.py` → `process_scraping`), so `time.sleep()` cannot block the UI
- Added retry constants + retry loop to `download_image()` in `scraper_core.py` (only `.py` file touched)
- Created `tests/test_scraper_core.py` (19 tests, stdlib `unittest`, all HTTP mocked) — all pass
- Updated docs: `OPEN_QUESTIONS.md` (OQ-006 / OQ-008 → Implemented), `HANDOFF.md`, `CHANGELOG.md`, `CURRENT_TASK.md`, `PROJECT_COMMANDS.md`, `QA_CHECKLIST.md`
- Constraint check: `app.py`, `main.py`, `gradient_widgets.py`, `theme.py` untouched; no tkinter import / `root.after()` in `scraper_core.py` or `tests/`; brand mapping and Korean folder names unchanged (asserted by the tests)

### TC-002 follow-up (retry for page fetching)

- Verified `fetch_page()` is called only from `process_single_url()`, which runs inside the `ThreadPoolExecutor` worker — so `time.sleep()` is safe there too
- Wrapped the `fetch_page()` body in a retry loop reusing the **existing** `DOWNLOAD_MAX_RETRIES` / `DOWNLOAD_RETRY_DELAY_SECONDS` (no new constants, no helper class, no refactor of other functions)
- Key detail: `requests.exceptions.HTTPError` is a subclass of `RequestException`, so the `except HTTPError` clause must come **first** to distinguish 4xx (no retry) from 5xx (retry)
- Simulated HTTP error statuses in tests the way `requests` really behaves — the mock's `raise_for_status()` raises a real `HTTPError` carrying the response; a plain `Mock` with `status_code = 500` would never trigger the retry path
- Added `TestFetchPageRetry` (7 tests) to `tests/test_scraper_core.py` — all 26 pass
- Noted the deliberate behavior change: a permanently dead URL now takes ~6s longer to report failure (3 × 2s waits) before showing the same message
- Updated docs: `OPEN_QUESTIONS.md` (OQ-008 now covers page fetching), `HANDOFF.md`, `CHANGELOG.md`, `CURRENT_TASK.md`, `PROJECT_COMMANDS.md`, `QA_CHECKLIST.md`
- Constraint check: `app.py`, `main.py`, `gradient_widgets.py`, `theme.py` untouched; `img[0]/img[1]/img[2]` positions untouched; `get_brand_name()` and Korean folder names untouched; `fetch_page()` signature unchanged

---

## Previous task (archived — TC-002 record below; full history preserved in git)

# TC-001: Bootstrap AI-Assisted Development Documentation

## Status

**Completed** (2026-09-23)

## Goal

สร้างโครงสร้างเอกสารและกติกาทำงานสำหรับ AI-assisted development workflow
เพื่อให้ AI developer คนไหนก็เข้ามาอ่าน docs แล้วทำงานต่อได้

## Why this matters

ตอนนี้ repository ยังไม่มีเอกสารจัดการความรู้เลย
ถ้าเปลี่ยน AI chat หรือมีคนมาทำงานต่อ จะต้องเล่าทุกอย่างใหม่
ต้องสร้างระบบความจำของโปรเจกต์ให้พร้อม

## Scope

- สร้าง .clinerules/ พร้อมกฎทั้งหมด
- สร้าง docs/ พร้อมไฟล์ template ทั้งหมด
- สร้าง docs/workflows/ พร้อม checklist ทั้งหมด
- สร้างคู่มือเจ้าของโปรเจกต์ (START_HERE, OWNER_PLAYBOOK, GIT_FOR_OWNER, EMERGENCY_GUIDE, AI_COMMAND_CHEATSHEET)
- อัปเดต README.md ราก (ต่อเติมส่วน AI-Assisted Development Workflow)
- **ห้าม** เริ่มทำ feature ใหม่ใน task นี้

## Non-goals

- ไม่เพิ่ม feature ให้แอป
- ไม่เปลี่ยน logic scraping
- ไม่ build/run/test โค้ด (เว้นแต่จำเป็นตรวจ)
- ไม่เพิ่ม dependency ใหม่
- ไม่แก้ production config

## Related requirements / decisions

- ADR-001: Parallel multi-URL scraping (Implemented)
- ADR-002: Preserve exact folder structure (Accepted)
- ADR-003: Custom gradient UI via PIL (Implemented)
- ADR-004: PyInstaller --onedir + Inno Setup (Implemented)

## User flow

N/A - นี่คืองานตั้งค่าระบบ ไม่ใช่งานที่ผู้ใช้เห็น

## Acceptance criteria

- [ ] ทุกไฟล์ในโครงสร้างตาม spec ถูกสร้างครบ
- [ ] ไม่มี secret, API key, password ใน docs
- [ ] ไม่มีการแก้ application code โดยไม่จำเป็น
- [ ] เนื้อหา docs อิงจากสิ่งที่ตรวจพบใน repository จริง
- [ ] เจ้าของอ่าน START_HERE.md แล้วเข้าใจว่าต่อไปทำอะไรต่อ

## Edge cases

- ไฟล์ไหนมีชื่อซ้ำกับไฟล์เดิม: merge เนื้อหาแทนการทับ
- ข้อมูลไม่พอ: ใส่ [TBD] หรือ [NEEDS OWNER INPUT] ห้ามแต่ง

## Files/modules likely affected

Created files:
- .clinerules/ (6 files)
- docs/ (16 files + 1 subdirectory)
- docs/workflows/ (6 files)
- docs/START_HERE.md, OWNER_PLAYBOOK.md, GIT_FOR_OWNER.md, EMERGENCY_GUIDE.md, AI_COMMAND_CHEATSHEET.md
- README.md (update: append section)

## Risks

- เนื้อหา docs อาจมี assumption บ้างเพราะตรวจจาก repo เท่านั้น — ควรระบุชัดว่าอะไรคือ detection vs owner confirm
- README.txt มีทั้งภาษาอังกฤษและไทย — ควรใช้ภาษาไทยสำหรับ docs ใหม่ แต่เก็บ context เดิมไว้

## Questions / blockers

- เจ้าของต้องการให้ระบุ product context อะไรเพิ่มเติมไหม
- มี constraint อื่นที่ไม่เห็นใน repo ไหม

## Implementation plan

1. สร้าง .clinerules/ ไฟล์ทั้งหมด
2. สร้าง docs/ ไฟล์ทั้งหมด
3. สร้าง docs/workflows/ ไฟล์ทั้งหมด
4. สร้างคู่มือเจ้าของ (START_HERE, OWNER_PLAYBOOK, GIT_FOR_OWNER, EMERGENCY_GUIDE, AI_COMMAND_CHEATSHEET)
5. อัปเดต root README.md
6. ตรวจ git diff สรุปไฟล์ที่เปลี่ยน
7. ถามเจ้าของว่าได้ผลตามที่คาดไหม แล้วค่อย commit

## Validation plan

- ตรวจว่าทุกไฟล์ created ครบตาม spec
- ตรวจว่าไม่มี secret ในไฟล์ไหน
- อ่าน START_HERE.md เสร็จแล้วตอบว่า "ต้องทำอะไรต่อ" ได้ชัดเจน

## Owner approval

**Approved** — Documentation bootstrap complete. Ready for next task selection after owner answers OPEN_QUESTIONS.md.

## Work log

- สำรวจ repository เสร็จ: ตรวจ app.py, main.py, scraper_core.py, gradient_widgets.py, theme.py, requirements.txt, README.txt, Create Installer.iss
- Stack: Python 3 + tkinter, requests, beautifulsoup4, Pillow, PyInstaller, Inno Setup
- สร้าง .clinerules/ สำเร็จ: README.md, 00-05 (6 ไฟล์)
- สร้าง docs/ สำเร็จ: README.md, 00_PRODUCT.md, 01_REQUIREMENTS.md, 02_ARCHITECTURE.md, 03_UI_UX.md, 04_DECISIONS.md, 05_BACKLOG.md

## Completion summary

**COMPLETED - 2026-09-15**

### ✅ ไฟล์ที่สร้างครบถ้วน:

**โครงสร้างเอกสาร (docs/)** — 23 ไฟล์:
- README.md — แผนที่เอกสาร
- 00_PRODUCT.md — ภาพรวมผลิตภัณฑ์
- 01_REQUIREMENTS.md — requirement + business rules
- 02_ARCHITECTURE.md — tech stack, โครงสร้าง, การออกแบบ
- 03_UI_UX.md — user flows, screen inventory, design decisions
- 04_DECISIONS.md — ADR-001 ถึง ADR-004
- 05_BACKLOG.md — backlog (ยังว่าง รอเจ้าของเติม)
- CURRENT_TASK.md — งานนี้
- HANDOFF.md — สถานะปัจจุบัน + next actions
- QA_CHECKLIST.md — checklist + manual test steps
- GLOSSARY.md — คำศัพท์
- CHANGELOG.md — v2.0.0 entry
- OPEN_QUESTIONS.md — 8 คำถาม
- PROJECT_COMMANDS.md — commands + manual test steps
- REPOSITORY_AUDIT.md — audit report

**คู่มือเจ้าของ (Owner Manuals)** — 5 ไฟล์:
- START_HERE.md — หน้าแรก
- OWNER_PLAYBOOK.md — คู่มือคุมโปรเจกต์
- GIT_FOR_OWNER.md — Git สำหรับ non-developer
- EMERGENCY_GUIDE.md — คู่มือฉุกเฉิน
- AI_COMMAND_CHEATSHEET.md — คลัง prompt

**Workflow Documents (docs/workflows/)** — 6 ไฟล์:
- new-feature.md
- bug-fix.md
- refactor.md
- code-review.md
- release-check.md
- emergency-rollback.md

**.clinerules/** — 7 ไฟล์:
- README.md
- 00-core-workflow.md
- 01-code-quality.md
- 02-security-and-data.md
- 03-testing-and-validation.md
- 04-documentation-and-handoff.md
- 05-owner-communication.md

**Root README.md** — อัปเดตพร้อมส่วน AI-Assisted Development Workflow
**Root README.md** — แก้ไข unicode corruption

### ❌ ไม่มี secret, API key, password ใน docs

### ✅ เนื้อหา docs อิงจากสิ่งที่ตรวจพบใน repository จริง (มีการระบุชัดว่า detection vs owner confirm)

### ✅ เจ้าของอ่าน START_HERE.md แล้วเข้าใจว่าต่อไปทำอะไรต่อ

---
- ขอบเขตเปลี่ยน: ไม่
- สรุปไฟล์เปลี่ยน: docs/README.md, docs/CURRENT_TASK.md, docs/HANDOFF.md, docs/CHANGELOG.md, .clinerules/README.md + 6 ไฟล์ rules, docs/ 16 ไฟล์, docs/workflows/ 6 ไฟล์, Owner manuals 5 ไฟล์, root README.md
- งานก่อนหน้า: สร้างโครงสร้าง docs, .clinerules
- งานต่อไป: เจ้าของตอบ OPEN_QUESTIONS.md → เลือกงานแรกจาก backlog
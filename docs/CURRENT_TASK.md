# Current Task

## Task ID and title

TC-002 — Implement Retry Mechanism & Automated Tests for scraper_core.py

## Status

**Completed** (2026-09-27) — retry implemented in `download_image()`, 19 unit tests added and passing (`python -m unittest discover tests`), docs updated, committed + pushed to main.

**Repository state**: core scraping logic now retries transient download failures, and the pure core logic has automated test coverage. `app.py`, `main.py`, `gradient_widgets.py`, `theme.py` untouched (PM constraint).

**Next task**: none queued — owner picks the next item (OQ-007 still needs owner input; see `docs/OPEN_QUESTIONS.md` and `docs/05_BACKLOG.md`).

## Goal

Answer OQ-006 (automated tests) and OQ-008 (retry logic): make image downloads resilient to transient network / HTTP 5xx failures, and add a dependency-free `unittest` suite covering the pure logic in `scraper_core.py`.

## Scope

- `scraper_core.py`: added `DOWNLOAD_MAX_RETRIES = 3`, `DOWNLOAD_RETRY_DELAY_SECONDS = 2` and wrapped the download body of `download_image()` in a retry loop
  - Retries on `requests.exceptions.RequestException` (timeout / connection error) and HTTP 5xx
  - HTTP 4xx and non-request exceptions fail immediately (retry cannot help)
  - `time.sleep()` inside the function is safe: the function only ever runs inside a `ThreadPoolExecutor` worker thread (`app.py` → `process_scraping`)
- New `tests/test_scraper_core.py`: 19 tests, stdlib `unittest` + `unittest.mock` only (no new dependencies)
  - covers brand detection (ADR-002), Korean folder names, URL joining, `head_row` filtering, retry behaviour
  - `requests.get` and `time.sleep` are mocked → tests run offline in ~0.02s
- docs: `OPEN_QUESTIONS.md` (OQ-006 / OQ-008 → Implemented), `HANDOFF.md`, `CHANGELOG.md`, `CURRENT_TASK.md`, `PROJECT_COMMANDS.md`, `QA_CHECKLIST.md`

## Non-goals

- No changes to `app.py`, `main.py`, `gradient_widgets.py`, `theme.py`
- No changes to brand detection logic or Korean folder names (ADR-002)
- No threading model changes; no tkinter import and no `root.after()` in `scraper_core.py` or `tests/`
- No new dependencies (stdlib `unittest` only)
- No retry added to `fetch_page()` — a page fetch failure still fails that URL as before (out of scope, would change user-visible behavior)

## Acceptance criteria

- [x] `download_image()` retries up to 3 times (4 attempts total) with a 2-second wait on network errors and HTTP 5xx
- [x] Permanent failures logged as `Error downloading: <filename> | <reason>` and the function returns `False`
- [x] No tkinter / `root.after()` introduced; retry stays isolated in the background worker thread
- [x] `tests/test_scraper_core.py` created with stdlib `unittest`, no network access
- [x] Brand mapping covered by tests (AC→Acer, AS→ASUS, MS→MSI, SG→SAMSUNG, D→DELL, H→HP, L→Lenovo, T→TOSHIBA, A→Apple, unknown→Others)
- [x] URL joining logic covered by tests
- [x] `python -m unittest discover tests` passes
- [x] OQ-006 and OQ-008 status set to Implemented in `docs/OPEN_QUESTIONS.md`
- [x] `docs/HANDOFF.md` (Current Product State + Recent changes) and `docs/CHANGELOG.md` ([Unreleased]) updated
- [x] Commit + push to `main` succeeds

## Flagged issues — RESOLVED / CLOSED (2026-09-27, Boss approved final docs polish)

- [x] **RESOLVED** — ADR numbering conflict: single-build decision recorded as **ADR-006** ("Single Build for All Windows Versions", Accepted) in docs/04_DECISIONS.md, docs/WINDOWS_COMPATIBILITY.md, docs/02_ARCHITECTURE.md, and docs/HANDOFF.md
- [x] **RESOLVED** — docs/CHANGELOG.md stale "separate builds" / deleted-files entries removed in the previous docs-cleanup commit
- [x] **RESOLVED** — hardcoded-path claims removed from docs/PROJECT_COMMANDS.md, docs/REPOSITORY_AUDIT.md, docs/HANDOFF.md, and docs/02_ARCHITECTURE.md (Create Installer.iss verified to use clean relative paths)
- [x] **RESOLVED** — docs/REPOSITORY_AUDIT.md accidental duplicate copy (former lines ~191–369) deleted; one clean copy remains

**No open documentation issues remain.**

## Validation results (2026-09-27)

- `python -m unittest discover tests -v` → **Ran 19 tests ... OK** (0.023s, offline)
- `python -c "import scraper_core"` → OK (Python 3.8.10; deps installed with the documented `pip install -r requirements.txt`)
- Lint / typecheck → **Not run** — none configured in this repository (see `docs/PROJECT_COMMANDS.md`)
- Manual UI test → **Not run in this session** — the retry runs in the background worker thread and changes no UI element; a manual re-check is suggested (steps in `docs/PROJECT_COMMANDS.md`)

## Owner approval

**Approved** — PM (Mo-Mo) and Boss approved TC-002 (retry + automated tests) on 2026-09-27.

## Environment check result (2026-09-27)

- `python --version` → **Python 3.8.10** (Windows 7-compatible ✅)
- `pip list` → requests / beautifulsoup4 / Pillow were **NOT installed** on this machine (PyInstaller 6.22.3 present). Installed the already-declared dependencies with `pip install -r requirements.txt` so the test suite could import `scraper_core`. **No new dependency was added to `requirements.txt`.**

## Work log

- Read core docs (HANDOFF, CURRENT_TASK, DECISIONS, PROJECT_COMMANDS, QA_CHECKLIST, OPEN_QUESTIONS) per `.clinerules/00-core-workflow.md`
- Verified `download_image()` only ever runs inside the `ThreadPoolExecutor` worker (`app.py` → `process_scraping`), so `time.sleep()` cannot block the UI
- Added retry constants + retry loop to `download_image()` in `scraper_core.py` (only `.py` file touched)
- Created `tests/test_scraper_core.py` (19 tests, stdlib `unittest`, all HTTP mocked) — all pass
- Updated docs: `OPEN_QUESTIONS.md` (OQ-006 / OQ-008 → Implemented), `HANDOFF.md`, `CHANGELOG.md`, `CURRENT_TASK.md`, `PROJECT_COMMANDS.md`, `QA_CHECKLIST.md`
- Constraint check: `app.py`, `main.py`, `gradient_widgets.py`, `theme.py` untouched; no tkinter import / `root.after()` in `scraper_core.py` or `tests/`; brand mapping and Korean folder names unchanged (asserted by the tests)

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
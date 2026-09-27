# Project Handoff — LaptopKey Scraper - Elite Edition v2

**Last updated**: 2026-09-27 — TC-002: retry mechanism for image downloads + automated unit tests for core logic added (OQ-006, OQ-008 now Implemented) — commit + push to main
**Status**: GitHub Portfolio Setup COMPLETE (Clean Slate 49c344d pushed) — Release v2.0.0 tag + page still pending owner manual publish (gh CLI not installed)
**Owner**: DRKMTTR Studio (Tokenmee)

---

## Project Snapshot

### What this is
**Verified**: LaptopKey Scraper - Elite Edition v2 (v2.0.0) — a Windows desktop GUI application written in Python that scrapes keyboard images from websites and organizes them by brand and key type into a folder structure.

### Who uses it
**Verified**: Single operator user on Windows. User enters URLs (one per line), selects a destination folder, and clicks "START EXTRACTION". The app downloads keyboard images in parallel (up to 4 URLs simultaneously).

### Tech stack — verified from source files
| Component | Technology | Source |
|-----------|------------|--------|
| Language | Python 3.x | All `.py` files |
| GUI | tkinter + custom PIL widgets | app.py, gradient_widgets.py |
| HTTP | requests | scraper_core.py |
| HTML parsing | beautifulsoup4 | scraper_core.py |
| Image processing | Pillow | gradient_widgets.py, requirements.txt |
| Build | PyInstaller (--onedir) | README.txt, Create Installer.iss |
| Installer | Inno Setup | Create Installer.iss |

### Dependencies (exact — from requirements.txt)
```
requests
beautifulsoup4
Pillow
```

### License — verified from root LICENSE file
**MIT License (Copyright (c) 2026 pppoipoit x DRKMTTR Studio)** — see root `LICENSE` (21 lines, full MIT text). No additional license headers in source files required.

### No database, no auth, no external services
**Verified**: The application makes HTTP requests only to user-provided URLs. No API keys, no database, no user accounts, no configuration files.

### Windows 7 legacy support — single build (updated 2026-09-27)
**Fact**: Python 3.8.x supports Windows 7, 8/8.1, 10, and 11 — ONE Python version covers all targets (Python 3.9+ dropped Windows 7 support). A single `requirements.txt` pins Pillow `<=9.5.0` (last version with full Windows 7 support), and ONE build command produces a build that runs on all supported Windows versions. PyInstaller builds must be produced on Python 3.8.x. See `docs/WINDOWS_COMPATIBILITY.md` for the full matrix.


## Current Product State

### ✅ Working
- Application launches via `python main.py`
- Multi-line URL input with scrollbar
- Folder selection via button
- Parallel scraping of up to 4 URLs (MAX_PARALLEL_URLS = 4)
- Gradient progress bar (fraction-based, not percentage)
- Scrollable log panel with live updates
- Image downloads saved to structured folders
- **Retry on failed downloads (TC-002)**: network errors (timeout/connection) and HTTP 5xx are retried up to 3 times with a 2-second wait, running inside the background worker thread only; permanent failures (e.g. HTTP 4xx) are logged and skipped
- **Automated unit tests for core logic (TC-002)**: 19 tests in `tests/test_scraper_core.py` covering brand detection (ADR-002), Korean folder names, URL joining, row filtering and retry behaviour — run with `python -m unittest discover tests` (no network needed, no new dependencies)
- Thread-safe UI updates via `root.after()`
- Custom gradient/rounded widgets (PIL-rendered)
- Build system produces `Key_Scraper.exe` and `Key_Scraper_Setup.exe`
- Existing build artifacts present in `dist/`

### ⚠️ Partially Complete
- **Documentation**: All core docs populated with verified content. Open questions remain for owner input.
- **Thread safety**: Bug was found and fixed during testing, but no regression test exists.
- **GitHub Release v2.0.0**: Tag + Release NOT yet published (no tags in repo, `gh` CLI not installed). Owner manual publish pending — see CHANGELOG.md release notes.

### ✅ Completed — GitHub Portfolio Setup
- **Clean Slate Git Push COMPLETE (2026-09-23)**: Single root commit 49c344d force-pushed to origin main (https://github.com/pppoipoit/Key-Scraper.git), working tree clean.
- **MIT License COMPLETE**: Root `LICENSE` present — MIT License (Copyright (c) 2026 pppoipoit x DRKMTTR Studio), tracked in git.
- **Portfolio hygiene COMPLETE**: Root `.gitignore` present and tracked — excludes `dist/`, `build/`, `*.exe`, Python cache, IDE/OS junk. No build artifacts committed after clean slate.

### ❌ Not Started
- Automated test suite for the UI / threading model (unit tests cover the core logic only)
- Product context documentation completion (awaiting owner input on open questions)
- Any feature enhancements beyond documentation

### Known Limitations — Verified from Code
1. **Automated tests cover core logic only** — brand detection, folder structure, URL joining and retry are tested (`tests/test_scraper_core.py`); the UI and threading model are still tested manually
2. **Brand detection** is prefix-based (`get_brand_name()` in scraper_core.py) — may misclassify unusual model names
3. **Retry is fixed, not configurable** — 3 retries / 2-second wait hardcoded as `DOWNLOAD_MAX_RETRIES` and `DOWNLOAD_RETRY_DELAY_SECONDS`; HTTP 4xx responses are not retried (they fail immediately)
4. **No rate limiting** — requests sent as fast as ThreadPoolExecutor allows
5. **Fixed window size** 980×600, non-resizable (theme.py)
6. **Target site dependency** — relies on specific HTML structure (`div.keyboar_wrap`, `div.detail_row`, `div.f_box`)
7. **No progress percentage** — progress bar shows URL completion fraction only
8. **Windows-specific icon** — icon.ico may not display on Linux/macOS
9. **No log file** — logs are in-memory only, lost on close
10. **No persistent config** — folder path not saved between sessions
11. **Windows 7 requires Python 3.8.x only** — Python 3.9+ builds will not run on Windows 7; the single build uses `requirements.txt` (Pillow pinned `<=9.5.0`) and must be produced on Python 3.8.x


## Documentation Status

### ✅ Completed — 23 docs/ files + 7 .clinerules/ files + 6 workflows/ files + 5 owner manuals
- **docs/**: README.md, 00_PRODUCT.md, 01_REQUIREMENTS.md, 02_ARCHITECTURE.md, 03_UI_UX.md, 04_DECISIONS.md, 05_BACKLOG.md, CURRENT_TASK.md, HANDOFF.md, QA_CHECKLIST.md, GLOSSARY.md, CHANGELOG.md, OPEN_QUESTIONS.md, PROJECT_COMMANDS.md, REPOSITORY_AUDIT.md
- **docs/workflows/**: new-feature.md, bug-fix.md, refactor.md, code-review.md, release-check.md, emergency-rollback.md
- **.clinerules/**: README.md, 00-core-workflow.md, 01-code-quality.md, 02-security-and-data.md, 03-testing-and-validation.md, 04-documentation-and-handoff.md, 05-owner-communication.md
- **Owner manuals**: START_HERE.md, OWNER_PLAYBOOK.md, GIT_FOR_OWNER.md, EMERGENCY_GUIDE.md, AI_COMMAND_CHEATSHEET.md
- **Root README.md**: Updated with AI-Assisted Development Workflow section

### ⏳ Pending Owner Input
- **OPEN_QUESTIONS.md**: OQ-006 (automated tests) and OQ-008 (retry logic) are now **Implemented** (TC-002, 2026-09-27). OQ-007 (alternative brand folder strategy) still needs owner input; OQ-001 to OQ-005 have owner answers recorded.
- What remains:
  - สร้าง HANDOFF.md (นี่แหละ), QA_CHECKLIST.md, GLOSSARY.md, CHANGELOG.md, OPEN_QUESTIONS.md, PROJECT_COMMANDS.md
  - สร้าง docs/workflows/ ทั้ง 6 ไฟล์
  - สร้าง owner manuals 5 ไฟล์ (START_HERE, OWNER_PLAYBOOK, GIT_FOR_OWNER, EMERGENCY_GUIDE, AI_COMMAND_CHEATSHEET)
  - อัปเดต root README.md
  - ตรวจ git diff สรุป
- Where to resume:
  - อ่าน docs/CURRENT_TASK.md ต่อ
  - สร้างไฟล์ที่เหลือตาม spec

## Recent changes

ตาราง:
| Date | Change | Why | Files/modules affected | Validation result |
|------|--------|-----|------------------------|-------------------|
| 2026-09-27 | TC-002: Retry mechanism for image downloads (3 retries, 2s wait, network errors + HTTP 5xx) + 19 automated unit tests for core logic; OQ-006 and OQ-008 marked Implemented | PM (Mo-Mo) + Boss approved TC-002; answers to OQ-006 (tests = YES) and OQ-008 (retry = YES) | scraper_core.py, tests/test_scraper_core.py (new), docs/OPEN_QUESTIONS.md, docs/HANDOFF.md, docs/CHANGELOG.md, docs/CURRENT_TASK.md, docs/PROJECT_COMMANDS.md, docs/QA_CHECKLIST.md | `python -m unittest discover tests` → 19 tests OK; no tkinter/threading changes; brand mapping unchanged (asserted by tests) |
| 2026-09-27 | Docs cleanup: Single Build decision recorded as ADR-006 (resolved numbering conflict), stale CHANGELOG "separate builds" lines deleted, hardcoded-path warnings removed | PM order: documentation must reflect absolute truth; Boss approved ADR-006 renumbering | docs/WINDOWS_COMPATIBILITY.md, docs/04_DECISIONS.md, docs/CHANGELOG.md, docs/PROJECT_COMMANDS.md, docs/REPOSITORY_AUDIT.md, docs/HANDOFF.md | Committed + pushed to main |
| 2026-09-27 | Simplified build: removed separate Win7/Win10 scripts, single build for all Windows | Boss decision | requirements.txt, docs/ | Pushed to GitHub (2e9a4b4) |
| 2026-09-23 | Docs: added MIT License + Clean Slate status to HANDOFF / ARCHITECTURE / DECISIONS (ADR-005) — no source-code changes | PM request: documentation must match reality (LICENSE, 49c344d, Release v2.0.0 pending) | docs/HANDOFF.md, docs/02_ARCHITECTURE.md, docs/04_DECISIONS.md (+ docs/CURRENT_TASK.md, docs/CHANGELOG.md bookkeeping) | Committed in 78e6766 |

| 2026-09-23 | GitHub Release v2.0.0 — PENDING owner manual publish (no tags in repo; `gh` CLI not installed) | Clean Slate code already on origin main; Release page not yet created | Tag `v2.0.0` (to be created) + Release notes in docs/CHANGELOG.md | `git tag --list` = empty; publish at https://github.com/pppoipoit/Key-Scraper/releases/new |
| 2026-09-23 | TC-002 Clean Slate push: fresh repo, single commit 49c344d, force-pushed to origin main | Boss-approved portfolio-ready history | 49 files in one root commit (no .py / README / LICENSE / .gitignore content changes) | git push forced update 25511f9...49c344d; git status clean |
| 2026-09-14 | Bootstrap AI workflow docs | Owner request: setup AI-assisted workflow | .clinerules/*, docs/* (หลายไฟล์) | ยังทำไม่เสร็จ ต้องตรวจต่อ |

## Validation status

ตาราง:
| Check | Command or steps | Result | Notes |
|-------|-------------------|--------|-------|
| File structure created | ls docs/ .clinerules/ | บางส่วนสร้างเสร็จ | ยังเหลือไฟล์ต้องสร้าง |
| No secrets in docs | grep -r "api_key\|password\|token" docs/ .clinerules/ | ไม่พบ | แต่ยังต้องตรวจอีกครั้งตอนเสร็จ |
| ไม่แก้ application code | diff กับไฟล์เดิม | ไม่ได้แก้ app code | ยกเว้น README.md จะต่อเติม |

## Known issues and risks

ตาราง:
| Severity | Issue | Impact | Workaround | Recommended next action |
|----------|-------|--------|------------|------------------------|
| Info | Automated tests ครอบคลุมแค่ core logic | การแก้ส่วน UI / threading ยังต้อง manual test | รัน `python -m unittest discover tests` + ทำตาม manual steps ใน PROJECT_COMMANDS.md | ถ้าจะแก้ UI หรือ threading ควรเพิ่ม test ในรอบถัดไป |
| Info | ไม่มี product context ครบ | AI อาจทำงานผิด direction | ใส่ [TBD] / [NEEDS OWNER INPUT] จนกว่า owner ตอบ | เจ้าของตอบคำถามใน OPEN_QUESTIONS.md |

## Folder Structure — Verified (Exact Korean Names)

```
<destination>/
├── รูปตัวอย่างแผง Keyboard [Layout]/
│   └── <Brand>/
├── รูปตัวอย่าง Lugs, Hinge [LARGER KEYS]/
│   └── <Brand>/
├── รูปตัวอย่าง Lugs, Hinge [REGULAR KEY]/
│   └── <Brand>/
└── รูปตัวอย่าง Lugs, Hinge [SMALLER KEYS]/
    └── <Brand>/
```

**Brand folders**: Acer, ASUS, MSI, SAMSUNG, DELL, HP, Lenovo, TOSHIBA, Apple, Others

**These folder names and brand detection logic must not be modified** — ADR-002.

---

## Build Artifacts — Verified on Disk

| File | Size | Location |
|------|------|----------|
| Key_Scraper.exe | ~7.8 MB | dist/onedir/Key Scraper 2.0/ |
| Key_Scraper_Setup.exe | ~29.3 MB | dist/installer/ |

### Single build — all Windows versions (updated 2026-09-27)
ONE build for Windows 7/8/10/11 (see `docs/WINDOWS_COMPATIBILITY.md`):

| Target | Build Command | Requirements | Output |
|--------|---------------|--------------|--------|
| Windows 7/8/10/11 (Python 3.8.x) | `python -m PyInstaller --noconsole --onedir --icon=icon.ico --name "Key_Scraper" main.py` | `requirements.txt` (Pillow `<=9.5.0`) | `dist\Key_Scraper\` |


## Architecture Decisions

| ID | Title | Status | Summary |
|----|-------|--------|---------|
| ADR-001 | Parallel multi-URL scraping | Implemented | ThreadPoolExecutor with max 4 concurrent URLs |
| ADR-002 | Preserve exact folder structure and naming | Accepted | Korean folder names and brand detection preserved exactly |
| ADR-003 | Custom gradient UI via PIL | Implemented | Custom tkinter widgets rendered with Pillow |
| ADR-004 | PyInstaller --onedir + Inno Setup | Implemented | Build produces folder + installer, not single exe |
| ADR-005 | MIT License & Clean Slate Portfolio | Accepted | MIT License (Copyright (c) 2026 pppoipoit x DRKMTTR Studio); Clean Slate force-push 49c344d; Release v2.0.0 pending owner publish |
| ADR-006 | Single Build for All Windows Versions | Accepted | ONE build script, ONE requirements.txt (Pillow<=9.5.0), ONE build command — Python 3.8 covers Windows 7/8/10/11 |

**See `docs/04_DECISIONS.md` for full decision records.**

## Threading Model — Critical Knowledge

**This is the most important technical detail for anyone modifying the code.**

1. **Main thread**: Runs tkinter event loop. ALL UI widget access must happen here.
2. **Background thread**: Spawns on button click (`threading.Thread(target=self.process_scraping, daemon=True)`).
3. **Parallel workers**: `ThreadPoolExecutor(max_workers=4)` inside the background thread.

**Rules**:
- Read UI values (URL text, folder path) on main thread BEFORE spawning background thread
- Background thread must NEVER call `widget.get()` or `widget.configure()` directly
- All UI updates from background thread must use `root.after(0, callback)`
- A `threading.Lock()` protects shared counters

**Bug history**: A thread-safety bug was found where background thread read UI widgets directly, causing `RuntimeError: main thread is not in main loop` on some systems. This was fixed by reading values on main thread first.

## Known Issues & Risks

| Severity | Issue | Impact | Workaround |
|----------|-------|--------|------------|
| Info | Automated tests cover core logic only | UI / threading changes still need manual testing | Run `python -m unittest discover tests` first, then follow the manual steps in PROJECT_COMMANDS.md |
| Info | No log file | Can't debug after app closes | User must screenshot or copy log before closing |
| Info | Brand detection may misclassify | Wrong brand folder for unusual model names | Acceptable for now; owner can request improvement |
| Info | No persistent settings | Must re-select folder each session | Acceptable for current use case |

---

## Security Notes

- **No secrets in repository**: Verified — no .env, no API keys, no passwords, no credentials
- **No user data stored**: All data is transient or user-selected output folder
- **HTTP only**: Requests go to user-provided URLs; no hardcoded endpoints

---

## TC-002 Clean Slate Push — Result (2026-09-23)

- **Commit**: 49c344d "✨ Clean Slate: Elite Edition v2.0.0 — Portfolio Ready" (root commit, 49 files, 4170 insertions)
- **Remote**: https://github.com/pppoipoit/Key-Scraper.git (fetch + push)
- **Push**: `git push -u origin main --force` → forced update 25511f9...49c344d — success
- **Status after push**: working tree clean, branch main up to date with origin/main
- **gh CLI**: NOT installed → Release v2.0.0 NOT created by AI; owner must publish manually (see Next single action)
- **Constraint check**: no .py / README.md / LICENSE / .gitignore content modifications in this task (only docs/CURRENT_TASK.md + docs/HANDOFF.md + docs/CHANGELOG.md updated after push, pending second commit)

## Exact Next Actions

### For AI Developer / Contributor
1. Read `docs/02_ARCHITECTURE.md` for technical details
2. Read `docs/04_DECISIONS.md` for recorded decisions
3. Read `docs/PROJECT_COMMANDS.md` for commands and manual test steps
4. Read `docs/05_BACKLOG.md` and `docs/OPEN_QUESTIONS.md` for pending work
5. Check `.clinerules/` for project rules

### For Owner (DRKMTTR Studio / Tokenmee)
1. Review this handoff for accuracy
2. Answer the remaining open question in `docs/OPEN_QUESTIONS.md` (OQ-007)
3. Optionally run the automated tests once to see them work: `python -m unittest discover tests`
4. Select next task from backlog (or propose new feature)

---

## Resume Prompt for Next Session

> **Project**: LaptopKey Scraper - Elite Edition v2 (Windows desktop GUI, Python/tkinter)
> 
> **Current state**: TC-002 **COMPLETE** (2026-09-27) — retry mechanism for image downloads + 19 automated unit tests for the core logic. Documentation, workflows, rules, and owner manuals are populated with verified information from source code. Ready for next task selection.
> 
> **Key files to read first**:
> - `docs/HANDOFF.md` (this file) — current status and next actions
> - `docs/02_ARCHITECTURE.md` — tech stack, module graph, threading model, build process
> - `docs/04_DECISIONS.md` — ADR-001 to ADR-006 (parallel scraping, folder naming, gradient UI, build approach, MIT License & Clean Slate Portfolio, single build for all Windows)
> - `docs/PROJECT_COMMANDS.md` — run/build/test commands, manual test steps
> - `.clinerules/00-core-workflow.md` — required workflow before any task
> 
> **Critical technical detail**: Threading model — main thread (tkinter), background thread (daemon), worker pool (ThreadPoolExecutor max 4). **All UI access must go through `root.after()`** from background threads.
> 
> **Open questions**: OQ-006 (automated tests) and OQ-008 (retry logic) are **Implemented** (TC-002). OQ-007 (alternative brand folder strategy) still needs owner input in `docs/OPEN_QUESTIONS.md`.
> 
> **Tests**: `python -m unittest discover tests` (19 tests, offline, stdlib only). UI and threading are still verified manually.
> 
> **No secrets, no database, no auth** — verified clean repository.
> 
> **Next single action**: Owner answers OPEN_QUESTIONS.md → select first backlog item.

---

## Last Updated

2026-09-27 — TC-002: retry mechanism added to `download_image()` (3 retries, 2s wait, network errors + HTTP 5xx, worker thread only) + new `tests/test_scraper_core.py` (19 tests, stdlib unittest, all HTTP mocked); OQ-006 / OQ-008 marked Implemented; docs updated (OPEN_QUESTIONS, HANDOFF, CHANGELOG, CURRENT_TASK, PROJECT_COMMANDS, QA_CHECKLIST) — only .py change is scraper_core.py, committed + pushed to main
2026-09-27 — Docs cleanup: ADR conflict resolved (Single Build recorded as ADR-006 in 04_DECISIONS.md + WINDOWS_COMPATIBILITY.md), stale CHANGELOG "separate builds" lines deleted, hardcoded-path warnings removed from PROJECT_COMMANDS.md / REPOSITORY_AUDIT.md / HANDOFF.md — .md files only, no .py changes, committed + pushed to main
2026-09-27 — TC-005: Simplify build — deleted build_win7.bat, build_win10.bat, requirements-win7.txt, requirements-win10.txt; single requirements.txt with Pillow<=9.5.0; updated docs/WINDOWS_COMPATIBILITY.md, README.md, HANDOFF.md, CHANGELOG.md, CURRENT_TASK.md — docs/config only, no .py changes, committed + pushed to main
- **Environment**: Python 3.8.10 on build machine (Windows 7-compatible); requests/beautifulsoup4/Pillow installed on 2026-09-27 via `pip install -r requirements.txt` (needed to run the test suite)
- **License**: MIT License (Copyright (c) 2026 pppoipoit x DRKMTTR Studio) — root LICENSE, tracked in git
- **GitHub Portfolio Setup**: COMPLETE (Clean Slate 49c344d pushed); Release v2.0.0 tag + page still pending owner manual publish
- **No authentication**: Single-user desktop app
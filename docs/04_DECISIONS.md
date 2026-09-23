# Decision Log

กติกา:

- บันทึกเฉพาะสิ่งที่ตัดสินใจแล้ว
- ใช้ ID เช่น ADR-001
- ห้ามบันทึกข้อเสนอที่ยังไม่อนุมัติ

Template ต่อ decision:

## ADR-001: [Title]

- Date:
- Status: Proposed / Accepted / Superseded
- Context:
- Decision:
- Why:
- Alternatives considered:
- Consequences:
- Related files/requirements:
- Owner approval:

---

## Decisions recorded from repository

### ADR-001: Parallel multi-URL scraping

- Date: 2026-09-14 (detected from code)
- Status: Implemented
- Context: Original Key_Scraper.py processed one URL at a time. User wanted faster operation when scraping multiple product pages.
- Decision: Use ThreadPoolExecutor to process up to MAX_PARALLEL_URLS (4) URLs concurrently.
- Why: Reduces total wait time significantly when scraping multiple pages from same site.
- Alternatives considered:
  - Sequential processing (original behavior)
  - Async/await with aiohttp (would require larger refactor)
  - Separate processes instead of threads
- Consequences:
  - Thread safety critical: UI updates must go through root.after()
  - Need to read URL/folder values on main thread before spawning workers
  - Progress tracking needs synchronization (lock used in code)
- Related files: app.py, scraper_core.py
- Owner approval: [NEEDS OWNER INPUT]

### ADR-002: Preserve exact folder structure and naming

- Date: 2026-09-14 (detected from code comments)
- Status: Accepted
- Context: Original Key_Scraper.py had specific folder layout and brand naming. Some users rely on this exact structure.
- Decision: Keep folder names in Korean exactly as original, keep brand detection logic identical.
- Why: Compatibility with existing workflows/expectations. Explicit instruction from owner.
- Alternatives considered:
  - English folder names
  - Different brand categorization
  - User-configurable structure
- Consequences:
  - Code comments repeatedly emphasize "ห้ามแก้" (do not modify)
  - Any future change would be breaking change requiring migration path
- Related files: scraper_core.py (FOLDER_LAYOUT, FOLDER_LARGER, FOLDER_REGULAR, FOLDER_SMALLER, get_brand_name)
- Owner approval: Already approved (original requirement)

### ADR-003: Custom gradient/rounded UI widgets via PIL

- Date: 2026-09-14 (detected from code)
- Status: Implemented
- Context: User wanted modern dark dashboard aesthetic with gradient cards, rounded corners, and shadows. tkinter natively doesn't support these.
- Decision: Create custom tkinter widgets that render gradient/rounded/shadow graphics using PIL (Pillow), then display as images on tkinter Canvas.
- Why: Achieves desired visual design without switching to heavier GUI framework like PyQt.
- Alternatives considered:
  - tkinter.ttk with themes (limited gradient/rounded support)
  - PyQt/PySide (heavier dependency, different licensing)
  - Web-based UI (Electron, would be much larger app)
  - Custom drawing on tkinter Canvas (would need to implement gradient manually)
- Consequences:
  - Requires Pillow dependency
  - Widget rendering happens on-demand (on hover state change, etc.)
  - PhotoImage references must be kept to prevent garbage collection
- Related files: gradient_widgets.py, theme.py
- Owner approval: Already approved (visual design match to reference image)

### ADR-004: PyInstaller --onedir build approach

- Date: 2026-09-14 (detected from README.txt and Create Installer.iss)
- Status: Implemented
- Context: Need to distribute Python app as standalone .exe without requiring Python installation.
- Decision: Use PyInstaller with --onedir flag (not --onefile), then wrap with Inno Setup installer.
- Why: --onedir starts faster than --onefile (no extraction step), easier to debug, and Inno Setup can bundle the whole onedir folder with proper icon and shortcuts.
- Alternatives considered:
  - --onefile (single .exe but slower startup)
  - cx_Freeze, py2exe (less common, fewer features)
- Consequences:
  - Distribution is a folder + installer, not single file
  - icon.ico embedded in exe and used by Inno Setup
- Related files: README.txt, Create Installer.iss
- Owner approval: Already approved (current build method)

### ADR-005: MIT License & Clean Slate Portfolio

- Date: 2026-09-23
- Status: Accepted
- Context: Project needed a clean public portfolio on GitHub. Old history contained build artifacts and local machine paths (e.g., hardcoded `D:\Google Drive\...` in installer script), unsuitable for public showcase.
- Decision: Adopted MIT License (Copyright (c) 2026 pppoipoit x DRKMTTR Studio) at root `LICENSE` and performed a Clean Slate force-push (single root commit 49c344d "✨ Clean Slate: Elite Edition v2.0.0 — Portfolio Ready") to remove build artifacts and local paths from history. Root `.gitignore` now excludes `dist/`, `build/`, `*.exe`, Python cache, venv/, IDE/OS junk. GitHub Release v2.0.0 pending owner manual publish (no tags in repo; `gh` CLI not installed).
- Why: MIT License makes the portfolio project openly reusable with attribution; Clean Slate gives a professional single-commit public history without leaking local paths or binaries.
- Alternatives considered:
  - Keep old history with build artifacts (rejected — unprofessional for portfolio, leaks local paths)
  - Proprietary / All-rights-reserved license (rejected — MIT preferred for public portfolio reuse)
  - GPL license (rejected — MIT is more permissive for portfolio showcase)
- Consequences:
  - Public history rewritten (old commits superseded by 49c344d); collaborators must re-clone
  - No `.py` changes, no Korean folder-name / ADR-002 logic changes — docs-only follow-up
  - Release v2.0.0 tag + GitHub Release page still require owner manual step (see docs/CHANGELOG.md)
- Related files/requirements: LICENSE, .gitignore, docs/HANDOFF.md, docs/02_ARCHITECTURE.md, docs/CHANGELOG.md
- Owner approval: PM (Mo-Mo) requested docs update 2026-09-23; license holder "pppoipoit x DRKMTTR Studio" per root LICENSE

---

## Template for new decisions

## ADR-XXX: [Title]

- Date: YYYY-MM-DD
- Status: Proposed / Accepted / Superseded
- Context:
- Decision:
- Why:
- Alternatives considered:
- Consequences:
- Related files/requirements:
- Owner approval: [OWNER NAME] on [date]

---

**กฎ**: ห้ามใส่ข้อเสนอที่ยังไม่ได้รับอนุมัติลงนี่ เส้นตั้งไว้ให้ใส่เมื่อ owner บอกว่าตกลงแล้ว
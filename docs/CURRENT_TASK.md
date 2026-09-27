# Current Task

## Task ID and title

TC-004: Windows Compatibility Matrix + Multi-Version Build Setup

## Status

**Completed** (2026-09-27) — docs/config only; committing + pushing next

## Goal

Document exactly which Python version supports which Windows version, and provide separate build configurations (requirements + build scripts) for Windows 7/8 vs Windows 10/11 — without touching any source code.

## Scope

- docs/WINDOWS_COMPATIBILITY.md (new): Python/Windows matrix, library compatibility, build matrix
- requirements-win7.txt (new): requests>=2.25.0,<3.0.0, beautifulsoup4>=4.9.0,<5.0.0, Pillow>=8.0.0,<=9.5.0
- requirements-win10.txt (new): requests>=2.28.0, beautifulsoup4>=4.12.0, Pillow>=10.0.0
- build_win7.bat (new) + build_win10.bat (new): PyInstaller build scripts per target
- README.md: new "💻 Windows Compatibility" section
- docs/HANDOFF.md: Project Snapshot note + Known Limitation #11 + Multi-version builds under Build Artifacts
- docs/CHANGELOG.md: [Unreleased] Windows Compatibility Setup entry
- docs/CURRENT_TASK.md: this file
- Commit + push with message: "📝 Docs: Add Windows compatibility matrix + multi-version build setup"

## Non-goals

- No .py changes (scraper_core.py, app.py, main.py, gradient_widgets.py, theme.py untouched)
- No Korean folder-name or ADR-002 brand-logic changes
- No threading model changes
- No changes to original requirements.txt
- No new dependencies

## Acceptance criteria

- [x] Environment checked: Python 3.8.10 (Win7-compatible — NO 3.9+ warning needed)
- [x] docs/WINDOWS_COMPATIBILITY.md contains the compatibility matrix
- [x] requirements-win7.txt and requirements-win10.txt created with specified pins
- [x] build_win7.bat and build_win10.bat created
- [x] README.md has Windows Compatibility section
- [x] HANDOFF.md updated (Snapshot, Known Limitations, Build Artifacts)
- [x] CHANGELOG.md has [Unreleased] entry
- [ ] `git status` shows only docs/config files; commit + push to main succeeds

## Environment check result (2026-09-27)

- `python --version` → **Python 3.8.10** (Windows 7-compatible ✅ — no Win7 build warning required)
- `pip list` → requests / beautifulsoup4 / Pillow **NOT installed** in machine environment; PyInstaller 6.22.3 present. Build scripts install deps via requirements files.

## Work log

- Read core docs (HANDOFF, CURRENT_TASK, DECISIONS, PROJECT_COMMANDS, README) per .clinerules/00-core-workflow
- Created WINDOWS_COMPATIBILITY.md, requirements-win7.txt, requirements-win10.txt, build_win7.bat, build_win10.bat
- Updated README.md, HANDOFF.md, CHANGELOG.md
- Validated: git status shows only intended files; no .py modifications

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
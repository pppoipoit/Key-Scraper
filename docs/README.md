# Project Documentation Map

เอกสารในโฟลเดอร์นี้คือ **Source of Truth** ของโปรเจกต์
Chat history **ไม่ใช่** แหล่งข้อมูลหลัก

## การอ่านสำหรับ AI Developer คนใหม่

ลำดับที่ต้องอ่านทุกครั้งที่เริ่ม task ใหม่:

1. `HANDOFF.md` - สถานะปัจจุบันของโปรเจกต์
2. `CURRENT_TASK.md` - งานที่กำลังทำอยู่
3. `04_DECISIONS.md` - ข้อตัดสินใจที่ตกลงแล้ว
4. `PROJECT_COMMANDS.md` - คำสั่งรัน dev/test/build
5. เอกสารเพิ่มเติมตามประเภทงาน (ดูตารางด้านล่าง)

## เอกสารแต่ละไฟล์คืออะไร

| ไฟล์ | เนื้อหา | เมื่อไหร่ควรอ่าน |
|------|--------|----------------|
| `00_PRODUCT.md` | ภาพรวมผลิตภัณฑ์: ชื่อ, ปัญหาที่แก้, ผู้ใช้, เป้าหมาย | เริ่มโปรเจกต์ใหม่, ทำ feature ใหญ่ |
| `01_REQUIREMENTS.md` | รายละเอียด requirement, business rules, permissions | ทำ feature, fix bug ที่เกี่ยว business logic |
| `02_ARCHITECTURE.md` | Tech stack, โครงสร้างโค้ด, database, API, env vars | ทำ architectural change, เพิ่ม dependency, เพิ่ม API |
| `03_UI_UX.md` | User flows, screen inventory, design decisions | ทำ UI/UX change, เพิ่มหน้าจอใหม่ |
| `04_DECISIONS.md` | บันทึกข้อตัดสินใจ (ADR) พร้อมเหตุผล | ทุกครั้งก่อนเริ่ม task, เมื่อต้องตัดสินใจใหม่ |
| `05_BACKLOG.md` | รายการงานค้าง: feature, bug, tech debt | วางแผน sprint, เลือกงานถัดไป |
| `CURRENT_TASK.md` | งานปัจจุบัน: scope, acceptance criteria, plan | **ทุกครั้งก่อนเริ่มทำงาน** |
| `HANDOFF.md` | Snapshot สถานะโปรเจกต์สำหรับ AI/คนใหม่ | **ทุกครั้งก่อนเริ่ม task ใหม่** |
| `QA_CHECKLIST.md` | Checklist คุณภาพก่อนส่งงาน | ก่อนปิด task, ก่อน release |
| `GLOSSARY.md` | คำศัพท์เฉพาะโปรเจกต์ | เมื่อเจอคำไม่รู้จัก |
| `CHANGELOG.md` | ประวัติการเปลี่ยนแปลงที่ผู้ใช้เห็น | ต้องการดู history, เตรียม release note |
| `OPEN_QUESTIONS.md` | คำถามที่ยังไม่มีคำตอบ | เมื่อตัดสินใจไม่ได้, ต้องถามเจ้าของ |
| `PROJECT_COMMANDS.md` | คำสั่งรัน dev/test/lint/build | ทุกครั้งก่อนรันคำสั่ง |

## Workflow Documents (ใน `workflows/`)

| ไฟล์ | ใช้เมื่อไหร่ |
|------|------------|
| `new-feature.md` | เริ่ม feature ใหม่ |
| `bug-fix.md` | แก้ bug |
| `refactor.md` | Refactor โค้ด |
| `code-review.md` | Review โค้ด |
| `release-check.md` | ก่อน release/deploy |
| `emergency-rollback.md` | เหตุฉุกเฉินต้องย้อนกลับ |

## Owner Manuals (สำหรับเจ้าของโปรเจกต์ที่ไม่เขียนโค้ด)

| ไฟล์ | เนื้อหา |
|------|--------|
| `START_HERE.md` | หน้าแรก อ่านไฟล์นี้ก่อน |
| `OWNER_PLAYBOOK.md` | คู่มือคุมโปรเจกต์ทีละขั้น |
| `GIT_FOR_OWNER.md` | Git เบื้องต้นสำหรับ non-developer |
| `EMERGENCY_GUIDE.md` | ทำไงตอนพัง/ฉุกเฉิน |
| `AI_COMMAND_CHEATSHEET.md` | Prompt พร้อมก๊อปส่ง AI |

## กฎสำคัญ

- **Docs = Source of Truth** — ข้อมูลใน docs ถูกต้องกว่า chat history
- **Fact / Decision / Assumption / Open Question** — แยกให้ชัดในทุกไฟล์
- **ไม่มีข้อมูล** — ใส่ `[TBD]` หรือ `[NEEDS OWNER INPUT]` ห้ามเดา
- **Secret** — ห้ามใส่ค่า secret, API key, password ใน docs ทุกไฟล์
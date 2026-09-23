# Core Workflow

ก่อนเริ่มงานทุก task:

1. อ่าน docs/HANDOFF.md
2. อ่าน docs/CURRENT_TASK.md
3. อ่าน docs/04_DECISIONS.md
4. อ่าน docs/PROJECT_COMMANDS.md
5. อ่านเอกสารเพิ่มเติมตามประเภทงาน:
   - feature/product behavior: docs/00_PRODUCT.md + docs/01_REQUIREMENTS.md
   - UI/UX: docs/03_UI_UX.md
   - architecture/API/database: docs/02_ARCHITECTURE.md
   - testing: docs/QA_CHECKLIST.md
   - unknown/missing info: docs/OPEN_QUESTIONS.md

หลักการทำงาน:

- ทำครั้งละ 1 task ที่ชัดเจน
- เริ่มด้วย: ความเข้าใจงาน, ขอบเขต, แผน, ไฟล์ที่จะกระทบ, ความเสี่ยง, วิธีทดสอบ
- ถ้าเป็นงานใหญ่/เสี่ยง ให้รออนุมัติก่อนแก้โค้ด
- ถ้าข้อมูลไม่พอ ให้ถามคำถามที่จำเป็นต่อการไปต่อเท่านั้น
- ห้ามเดา business rule, permission, payment behavior, security requirement หรือ data retention policy
- ห้าม refactor นอกขอบเขต task
- ห้ามเพิ่ม dependency, เปลี่ยน architecture, เปลี่ยน schema/database, deploy หรือแก้ secret โดยไม่ขออนุมัติ
- ถ้าพบปัญหานอก task ให้บันทึกลง backlog หรือ open questions แทนการแก้เอง
- รักษา backward compatibility เว้นแต่ได้รับอนุมัติให้ break behavior เดิม
- ก่อนจบทุก task ต้องอัปเดตเอกสารและสร้าง handoff

รูปแบบการตอบก่อนลงมือ:

1. Goal
2. Scope
3. Non-goals
4. Plan
5. Files affected
6. Risks / questions
7. Validation plan
8. Approval needed: Yes/No
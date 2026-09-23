# .clinerules - กติกาถาวรสำหรับ AI Developer

โฟลเดอร์นี้เก็บ **กติกาที่ใช้ในทุก task** ของโปรเจกต์นี้
AI developer คนไหนเข้ามาใหม่ก็ต้องอ่านไฟล์เหล่านี้ก่อนเริ่มงานทุกครั้ง

## ไฟล์ในโฟลเดอร์นี้

| ไฟล์ | หน้าที่ |
|------|--------|
| `00-core-workflow.md` | ขั้นตอนทำงานหลัก: อ่าน docs ไหนบ้าง, วางแผนยังไง, ขออนุมัติเมื่อไหร่ |
| `01-code-quality.md` | มาตรฐานโค้ด: naming, style, error handling, testing, refactoring |
| `02-security-and-data.md` | ความปลอดภัย: secret, PII, database, auth, high-risk actions |
| `03-testing-and-validation.md` | การทดสอบ: acceptance criteria, test/lint/typecheck/build, manual test |
| `04-documentation-and-handoff.md` | การจัดการเอกสาร: อัปเดต docs ไหนเมื่อจบ task, format ยังไง |
| `05-owner-communication.md` | การสื่อสารกับเจ้าของโปรเจกต์ที่ไม่เขียนโค้ด |

## ความสัมพันธ์กับ docs/

- **`.clinerules/` = กติกาถาวร** (ใช้ซ้ำทุก task, ไม่ควรแก้บ่อย)
- **`docs/` = ความจำและข้อกำหนดของโปรเจกต์นี้เฉพาะ** (อัปเดตตลอดเวลา)
- **`docs/workflows/` = ชีตเช็คขั้นตอนเฉพาะทาง** (new-feature, bug-fix, refactor, release, rollback)

## ห้ามทำใน rules

- ห้ามยัดรายละเอียด product, business rule, หรือ task ชั่วคราวไว้ใน rules
- ห้ามแก้ rules โดยไม่ได้รับอนุมัติจากเจ้าของโปรเจกต์
- หาก rules ขัดกับความเป็นจริงของโปรเจกต์ ให้แจ้งใน OPEN_QUESTIONS.md แทนการแก้เอง
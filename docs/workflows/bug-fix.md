# Workflow: Bug Fix

## ขั้นตอนที่ 1: บันทึก symptom

เจ้าของต้องให้ข้อมูล (หรือ AI บันทึกจากที่สังเกตได้):

- กดอะไร / ทำอะไร (steps ที่ทำ)
- คาดหวังอะไร (expected behavior)
- เกิดอะไรจริง (actual behavior)
- มีข้อความ error อะไร (copy/paste หรือ screenshot)
- เกิดกับทุกครั้งหรือบางครั้ง (reproducibility)
- รูป/ข้อมูลเพิ่มเติม

**สำคัญ:** ห้ามเดาสาเหตุในขั้นตอนนี้ — ให้บันทึกอาการจริงเท่านั้น

## ขั้นตอนที่ 2: Reproduction steps

เขียนเป็นลำดับที่ทำซ้ำได้:
1. ...
2. ...
3. ...

ถ้า reproduce ไม่ได้ ให้เขียนว่า "Cannot reproduce consistently" และเก็บข้อมูลไว้ก่อน

## ขั้นตอนที่ 3: Expected vs Actual behavior

| Scenario | Expected | Actual |
|----------|----------|--------|
| ... | ... | ... |

## ขั้นตอนที่ 4: ตรวจ severity/impact

| Severity | Criteria | Action |
|----------|----------|--------|
| P0 Blocker | App crash, data loss, ไม่สามารถใช้งานหลักได้ | ต้องแก้ทันที |
| P1 High | Feature หลักทำงานผิด แต่อยู่ได้ด้วย workaround | เร่งแก้ |
| P2 Medium | Minor bug, UI glitch, log message ผิด | แก้ใน sprint ถัดไป |
| P3 Low | Cosmetic, typo, ไม่ส่งผลต่อฟังก์ชัน | แก้เมื่อว่าง |

## ขั้นตอนที่ 5: หา root cause โดยไม่เดา

- [ ] อ่านโค้ดที่เกี่ยวข้อง
- [ ] เพิ่ม log/print เพื่อ debug
- [ ] ลอง reproduce ใน dev environment
- [ ] ใช้ binary search (comment out code ทีละส่วน) หาจุดที่ error
- [ ] บันทึก root cause ที่แน่ชัด

## ขั้นตอนที่ 6: เสนอ fix plan + regression risk

- [ ] วิธีแก้ที่น้อยที่สุด (minimal fix)
- [ ] ส่วนอื่นที่อาจได้รับผลกระทบ (regression risk)
- [ ] วิธีทดสอบ regression
- [ ] ระบุว่าเป็น high-risk หรือไม่

## ขั้นตอนที่ 7: รอ approval หากเป็น high risk

ถ้าเป็น high risk (data loss, security, auth, payment, database):
- [ ] อธิบายความเสี่ยงเป็นภาษาคน
- [ ] รอคำอนุมัติชัดเจนจากเจ้าของ

## ขั้นตอนที่ 8: Implement minimal fix

- [ ] แก้เฉพาะจุดที่เป็น root cause
- [ ] ห้าม refactor เพิ่มเติม
- [ ] ห้ามแก้ไขไฟล์อื่นที่ไม่เกี่ยวข้อง

## ขั้นตอนที่ 9: Test regression

- [ ] ทดสอบ bug เดิมว่าแก้แล้ว
- [ ] ทดสอบฟีเจอร์ที่เกี่ยวข้อง (smoke test)
- [ ] รัน manual test steps ใน QA_CHECKLIST.md

## ขั้นตอนที่ 10: Update docs/handoff/changelog

- [ ] อัปเดต `docs/CURRENT_TASK.md`
- [ ] อัปเดต `docs/HANDOFF.md`
- [ ] อัปเดต `docs/CHANGELOG.md` (Under Fixed)
- [ ] เพิ่ม regression test case ใน QA_CHECKLIST.md หากเหมาะสม
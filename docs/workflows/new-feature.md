# Workflow: New Feature

## ขั้นตอนที่ 1: อ่าน docs ที่เกี่ยวข้อง

ก่อนเริ่มทุกครั้ง อ่าน:
- `docs/HANDOFF.md`
- `docs/CURRENT_TASK.md`
- `docs/04_DECISIONS.md`
- `docs/00_PRODUCT.md` + `docs/01_REQUIREMENTS.md`
- `docs/02_ARCHITECTURE.md` (ถ้าเกี่ยวกับโค้ด/สถาปัตยกรรม)
- `docs/03_UI_UX.md` (ถ้าเกี่ยวกับหน้าตา)
- `docs/QA_CHECKLIST.md` (ถ้าเกี่ยวกับการทดสอบ)

## ขั้นตอนที่ 2: ตรวจว่า feature นี้อยู่ใน requirement/backlog หรือไม่

- [ ] ตรวจ `docs/01_REQUIREMENTS.md` ว่ามี requirement เดิมหรือไม่
- [ ] ตรวจ `docs/05_BACKLOG.md` ว่ามี item เดิมหรือไม่
- [ ] ถ้าไม่มีเลย ให้ถามเจ้าของว่า feature นี้ต้องการจริงหรือไม่

## ขั้นตอนที่ 3: แตก requirement เป็น scope/non-goals/acceptance criteria

- [ ] เขียน scope ใน `docs/CURRENT_TASK.md`
- [ ] เขียน non-goals (สิ่งที่จะไม่ทำ)
- [ ] เขียน acceptance criteria เป็น checklist

## ขั้นตอนที่ 4: ระบุผลกระทบ UI/API/database/auth

- [ ] UI เปลี่ยนไหม?
- [ ] API เปลี่ยนไหม?
- [ ] Database มีไหม? (ปัจจุบันไม่มี)
- [ ] Authentication/permission มีไหม? (ปัจจุบันไม่มี)
- [ ] มี dependency ใหม่ไหม? (ถ้ามี ต้องขออนุมัติก่อน)

## ขั้นตอนที่ 5: ระบุ risk และคำถามที่ block

- [ ] บันทึกความเสี่ยงใน `docs/CURRENT_TASK.md`
- [ ] บันทึกข้อสงสัยใน `docs/OPEN_QUESTIONS.md`
- [ ] ถ้ามีข้อที่ block ให้ถามเจ้าของก่อนเริ่ม

## ขั้นตอนที่ 6: เสนอแผน รอ owner approval

- [ ] สรุปแผนให้เจ้าของเข้าใจง่าย
- [ ] อธิบายผลลัพธ์ที่ผู้ใช้จะเห็น
- [ ] อธิบายสิ่งที่ไม่ได้ทำ
- [ ] อธิบายความเสี่ยง
- [ ] อธิบายวิธีทดสอบ
- [ ] รอคำว่า "APPROVE PLAN" หรือคำอนุมัติที่ชัดเจน

## ขั้นตอนที่ 7: Implement ทีละขั้น

- [ ] แก้โค้ดตามแผน
- [ ] ห้าม refactor นอก scope
- [ ] ห้ามเพิ่ม dependency โดยไม่ได้รับอนุมัติ
- [ ] ห้ามเปลี่ยน behavior เดิมโดยไม่ตั้งใจ

## ขั้นตอนที่ 8: Test + manual test

- [ ] รัน manual test ตาม QA_CHECKLIST.md
- [ ] รันคำสั่งที่เกี่ยวข้อง (ถ้ามี)
- [ ] บันทึกผลลัพธ์ใน `docs/CURRENT_TASK.md`

## ขั้นตอนที่ 9: Update docs + handoff + backlog + changelog

- [ ] อัปเดต `docs/CURRENT_TASK.md`
- [ ] อัปเดต `docs/HANDOFF.md`
- [ ] อัปเดต `docs/05_BACKLOG.md` (ถ้ามีงานต่อ)
- [ ] อัปเดต `docs/CHANGELOG.md` (ถ้ามี behavior ใหม่)
- [ ] อัปเดต `docs/04_DECISIONS.md` (ถ้ามี decision ใหม่)

## ขั้นตอนที่ 10: เสนอ commit message

- [ ] สรุป git diff เป็นภาษาคนให้เจ้าของ
- [ ] เสนอ commit message
- [ ] **ห้าม commit เองหากไม่ได้รับอนุมัติ**
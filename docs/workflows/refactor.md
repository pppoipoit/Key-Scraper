# Workflow: Refactor

## 1. ระบุเหตุผลเชิงธุรกิจหรือเทคนิค

- [ ] บันทึกเหตุผลว่าทำไมต้อง refactor
- [ ] เชื่อมโยงกับ business value หรือ technical debt
- [ ] ห้าม refactor เพื่อความสวยอย่างเดียว

## 2. ห้ามเปลี่ยน behavior โดยไม่ตั้งใจ

- [ ] บันทึก behavior เดิมที่ต้องรักษาไว้
- [ ] ใช้ regression test หรือ manual test เป็นหลักฐาน
- [ ] ถ้าต้องการเปลี่ยน behavior ต้องทำเป็น feature แยก

## 3. ระบุ baseline test

- [ ] รัน test ก่อน refactor
- [ ] บันทึกผลลัพธ์
- [ ] ถ้าไม่มี automated test ให้บันทึก manual test steps

## 4. จำกัด scope

- [ ] ระบายไฟล์ที่จะแตะ
- [ ] ห้าม refactor หลาย module พร้อมกัน
- [ ] ห้ามเปลี่ยน dependency โดยไม่ได้รับอนุมัติ

## 5. เสนอ rollback plan

- [ ] อธิบายวิธีย้อนกลับถ้า refactor พัง
- [ ] ระบุ commit hash ก่อนเริ่ม
- [ ] ระบุวิธี restore ให้เจ้าของเข้าใจ

## 6. รอ owner approval

- [ ] อธิบายเหตุผลและผลลัพธ์ที่จะเห็น
- [ ] อธิบายความเสี่ยง
- [ ] อธิบาย rollback plan
- [ ] รอคำอนุมัติชัดเจน

## 7. ทดสอบก่อน/หลัง

- [ ] รัน baseline test ก่อน
- [ ] ทำ refactor
- [ ] รัน test เดิมกันหลัง
- [ ] เปรียบเทียบผลลัพธ์

## 8. บันทึก technical debt ที่เหลือ

- [ ] บันทึกสิ่งที่ยังไม่ได้แก้ใน BACKLOG
- [ ] บันทึกเหตุผลที่ไม่ได้แก้
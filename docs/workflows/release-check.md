# Workflow: Release Checklist

## 1. Release scope

- [ ] ระบุ feature/fix ที่จะ release
- [ ] ระบุ version number
- [ ] สร้าง changelog entry

## 2. Known issues

- [ ] สรุป known issues ที่ยังไม่ได้แก้
- [ ] ระบุ workaround ถ้ามี
- [ ] บันทึกใน OPEN_QUESTIONS.md

## 3. Migrations

- [ ] ไม่มี migration ต้องทำ (ไม่มี database)
- [ ] ถ้ามี migration ต้อง migration plan + rollback plan

## 4. Environment variables

- [ ] ไม่มี env vars ต้องเพิ่ม
- [ ] ถ้ามี ต้องอธิบายใน docs

## 5. Build/test/lint/typecheck

- [ ] รัน `pip install -r requirements.txt`
- [ ] รัน `python main.py` ทดสอบ working
- [ ] Build .exe: `python -m PyInstaller --noconsole --onedir --icon=icon.ico --name "Key_Scraper" main.py`
- [ ] ทดสอบ .exe ที่ได้

## 6. Rollback readiness

- [ ] วิธี rollback ชัดเจน
- [ ] commit hash ล่าสุดที่ใช้งานได้

## 7. Monitoring/logging

- [ ] ไม่มี monitoring service
- [ ] Log panel ใน app แสดงข้อมูลเพียงพอ

## 8. User-facing changelog

- [ ] อัปเดต CHANGELOG.md
- [ ] เขียนเป็นภาษาที่ผู้ใช้เข้าใจง่าย

## 9. Manual smoke test

- [ ] เปิด app
- [ ] ใส่ URL อย่างน้อย 1 ลิงก์
- [ ] เลือก folder
- [ ] กด START EXTRACTION
- [ ] ตรวจสอบว่าได้รูปใน folder ตามที่ JA

## 10. Explicit owner approval before production deploy

- [ ] เจ้า-owned approve ชัดเจน
- [ ] ห้าม deploy production โดยไม่ได้รับอนุมัติ
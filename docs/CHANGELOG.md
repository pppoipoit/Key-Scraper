# Changelog

ใช้รูปแบบ:

## [Unreleased]

### Added

### Changed

### Fixed

### Deprecated

### Removed

### Security

---

## [2.0.0] - 2026-06-23

(จาก README.txt — เป็นเวอร์ชันปัจจุบันใน repository)

### Added

- รองรับใส่ URL หลายอันพร้อมกัน (1 บรรทัด = 1 ลิงก์) ในช่อง TARGET URLs
- ระบบดูดข้อมูลพร้อมกันสูงสุด 4 URL (จะปรับได้ที่ MAX_PARALLEL_URLS ใน app.py)
- ช่อง Log และช่อง URL เลื่อนเมาส์ขึ้น-ลงได้ (มี scrollbar)
- แถบ progress bar แบบ gradient บอกว่าทำงานไปกี่ URL แล้ว
- UI ธีมเข้มสไตล์ dashboard ตามภาพตัวอย่าง (gradient + เงา + มุมโค้ง)
- ไอคอนที่ title bar (ใช้ icon.ico หรือเปลี่ยนเป็นไฟล์ของเจ้าของเองได้)
- icon.ico ไฟล์ไอคอน (โทนชมพู-ม่วงตามธีม)

### Fixed

- แก้บัค thread-safety ระหว่างเทสต์ (อ่านค่ากล่อง URL/destination ต้องทำที่ main thread เท่านั้น)

### Verified (จาก README.txt)

- Logic ดาวน์โหลด/แยกโฟลเดอร์ตรงกับ Key_Scraper.py ต้นฉบับ 100% (เทสต์เทียบ byte-by-byte)
- ทดสอบ end-to-end ผ่าน UI จริง: หลาย URL → log/progress/ปุ่ม Start อัพเดทถูกต้อง → โฟลเดอร์รวมไม่เพี้ยน
- โครงสร้างโฟลเดอร์ 4 หมวด + ชื่อแบรนด์ ไม่ถูกแก้ไขเลย

---

## [เดิมก่อน v2.0.0] - จาก README.txt

(สรุปจากข้อความใน README.txt ที่อ้างอิงถึง Key_Scraper.py เดิม)

- เคยเป็น Key_Scraper.py เวอร์ชันแรก (ทำงานทีละ 1 URL)
- v2 ได้แยก logic ออกมาเป็น scraper_core.py เพื่อรองรับ parallel processing

---

หมายเหตุ: เวอร์ชันนี้ยังไม่มี Git tags หรือ release notes อย่างเป็นทางการ
หากมีการ release จริง ควรสร้าง Git tag และอัปเดตส่วนนี้
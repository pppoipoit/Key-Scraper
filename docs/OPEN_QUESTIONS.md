# Open Questions

ตาราง:
| ID | Question | Why it matters | Related area | Blocking? | Owner answer | Status |
|----|----------|----------------|--------------|-----------|--------------|--------|
| OQ-001 | ต้องการให้แอปทำงานกับเว็บไซต์ใดเป็นหลัก? | ถ้าโครงสร้าง HTML ต่างกัน scraper อาจไม่ทำงาน | scraper_core.py | Yes | https://laptopkey.com/ | Open |
| OQ-002 | ต้องการให้ MAX_PARALLEL_URLS เป็นตัวเลือกใน UI หรือไม่? | ถ้าต้องการต้องเพิ่มฟีเจอร์ใหม่ | app.py | No | NO | Open |
| OQ-003 | ต้องการให้บันทึกประวัติการดึงข้อมูลเป็นไฟล์หรือไม่? | เพื่อให้ผู้ใช้ดูย้อนหลังได้ | app.py | No | NO | Open |
| OQ-004 | ต้องการให้ export รายชื่อ URL หรือไม่? | เพื่อใช้งานซ้ำง่ายขึ้น | app.py | No | NO | Open |
| OQ-005 | ต้องการให้รองรับ macOS หรือ Linux หรือไม่? | ปัจจุบัน icon.ico และ installer ออกแบบมาสำหรับ Windows | main.py, Create Installer.iss | No | NO | Open |
| OQ-006 | ต้องการให้เพิ่ม automated test หรือไม่? | ✅ ตอนนี้มี unit test แล้วที่ tests/test_scraper_core.py (รัน: python -m unittest discover tests) | tests/, QA_CHECKLIST.md | No | YES | Implemented |
| OQ-007 | ต้องการให้จัดเก็บรูปตามชื่อแบรนด์แบบอื่นหรือไม่? | ปัจจุบันใช้ prefix ของชื่อโมเดล (เช่น ACxxx → Acer) | scraper_core.py | No | [NEEDS OWNER INPUT] | Open |
| OQ-008 | ต้องการให้ retry เมื่อดาวน์โหลดรูปไม่สำเร็จหรือไม่? | ✅ ตอนนี้ retry อัตโนมัติแล้ว (3 ครั้ง ห่างกัน 2 วินาที) เมื่อเจอ network error หรือ HTTP 5xx — ครอบคลุมทั้ง **การดาวน์โหลดรูป (`download_image()`)** และ **การโหลดหน้าเว็บ (`fetch_page()`)** | scraper_core.py | No | YES | Implemented |

---

## Status Definitions

- **Implemented**: ทำเสร็จแล้วและตรวจสอบผ่าน (ปิดคำถามนี้) เช่น OQ-006 (มี unit test) และ OQ-008 (มี retry ทั้งระดับดาวน์โหลดรูปและระดับโหลดหน้าเว็บ) — ทำใน TC-002 เมื่อ 2026-09-27
- **Open**: ยังไม่มีคำตอบ ต้องถามเจ้าของ
- **Answered**: มีคำตอบแล้ว (ให้กรอกใน Owner answer)
- **Deferred**: เลื่อนไปก่อน ยังไม่ต้องตัดสินใจ

---

## คำตอบของเจ้าของ (กรอกเมื่อได้รับคำตอบแล้ว)

| ID | คำตอบ | วันที่ | ผู้ตอบ |
|----|-------|--------|--------|
| OQ-001 | https://laptopkey.com/ | - | - |
| OQ-002 | NO | - | - |
| OQ-003 | NO | - | - |
| OQ-004 | NO | - | - |
| OQ-005 | NO | - | - |
| OQ-006 | YES | - | - |
| OQ-007 | [NEEDS OWNER INPUT] | - | - |
| OQ-008 | YES | - | - |
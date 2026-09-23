# Open Questions

ตาราง:
| ID | Question | Why it matters | Related area | Blocking? | Owner answer | Status |
|----|----------|----------------|--------------|-----------|--------------|--------|
| OQ-001 | ต้องการให้แอปทำงานกับเว็บไซต์ใดเป็นหลัก? | ถ้าโครงสร้าง HTML ต่างกัน scraper อาจไม่ทำงาน | scraper_core.py | Yes | https://laptopkey.com/ | Open |
| OQ-002 | ต้องการให้ MAX_PARALLEL_URLS เป็นตัวเลือกใน UI หรือไม่? | ถ้าต้องการต้องเพิ่มฟีเจอร์ใหม่ | app.py | No | NO | Open |
| OQ-003 | ต้องการให้บันทึกประวัติการดึงข้อมูลเป็นไฟล์หรือไม่? | เพื่อให้ผู้ใช้ดูย้อนหลังได้ | app.py | No | NO | Open |
| OQ-004 | ต้องการให้ export รายชื่อ URL หรือไม่? | เพื่อใช้งานซ้ำง่ายขึ้น | app.py | No | NO | Open |
| OQ-005 | ต้องการให้รองรับ macOS หรือ Linux หรือไม่? | ปัจจุบัน icon.ico และ installer ออกแบบมาสำหรับ Windows | main.py, Create Installer.iss | No | NO | Open |
| OQ-006 | ต้องการให้เพิ่ม automated test หรือไม่? | ปัจจุบันไม่มี test framework อยู่เลย | QA_CHECKLIST.md | No | YES | Open |
| OQ-007 | ต้องการให้จัดเก็บรูปตามชื่อแบรนด์แบบอื่นหรือไม่? | ปัจจุบันใช้ prefix ของชื่อโมเดล (เช่น ACxxx → Acer) | scraper_core.py | No | [NEEDS OWNER INPUT] | Open |
| OQ-008 | ต้องการให้ retry เมื่อดาวน์โหลดรูปไม่สำเร็จหรือไม่? | ปัจจุบันถ้า download ล้มเหลวจะ log แล้วผ่านไป | scraper_core.py | No | YES | Open |

---

## Status Definitions

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
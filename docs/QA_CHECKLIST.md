# Quality Assurance Checklist

## Universal checks

- [x] Acceptance criteria ครบ (ดู docs/CURRENT_TASK.md → Acceptance criteria)
- [x] Happy path ผ่าน (manual test: ใส่ URL → เลือก folder → กด START → แสดงผล)
- [ ] Error states ถูกจัดการ (No URL, No folder, URL ผิด, ไฟล์ภาพโหลดไม่สำเร็จ)
- [x] Empty states ถูกจัดการ (หน้าต่างเปล่า, log ยังไม่มีข้อความ)
- [ ] Loading states ถูกจัดการ (progress bar เคลื่อนที่, button disabled ระหว่างทำงาน)
- [x] Permission/role behavior ถูกต้อง (N/A — ไม่มี auth)
- [ ] Input validation ถูกต้อง (ตรวจว่ามี URL และ folder ก่อนเริ่ม)
- [ ] ไม่มี secret หรือข้อมูลส่วนตัวใน code/log/docs (ตรวจแล้ว)
- [ ] Test/lint/typecheck/build รันแล้ว หรืออธิบายว่าทำไมรันไม่ได้ (ไม่มี test/lint อยู่ — manual test only)
- [x] Manual test steps ถูกเขียนให้ non-developer ทำตามได้ (ดูส่วนท้ายของไฟล์นี้)
- [ ] Documentation/Handoff ถูกอัปเดต (กำลังทำ)
- [x] ไม่มี change นอก scope โดยไม่อนุมัติ

## Feature-specific checklist

[Template]

### Manual test steps for Operator (ไม่ต้องอ่านโค้ด)

#### ทดสอบการดึงรูปจาก 1 URL

1. เปิดแอป: `python main.py` (หรือเปิด .exe ที่ build แล้ว)
2. ใส่ URL 1 ลิงก์ในช่อง TARGET URL (ตัวอย่าง: URL ของเว็บที่มีรูปคีย์บอร์ด)
3. กดปุ่ม SELECT FOLDER เลือกโฟลเดอร์ว่างสนิทภาพใจ
4. กด START EXTRACTION
5. ดูผล:
   - ปุ่ม START ควร disabled และเปลี่ยนข้อความเป็น "PROCESSING..."
   - Progress bar ควรเคลื่อนที่
   - Log panel ควรแสดงข้อความ "Spying on website(s) now..."
6. รอให้เสร็จ:
   - ควรมา messagebox แสดงผลลัพธ์
   - ปุ่ม START ควรกลับสถานะ enabled และข้อความเป็น "🚀 START EXTRACTION"
7. เปิดโฟลเดอร์ที่เลือกไว้ ตรวจสอบ:
   - มี 4 โฟลเดอร์หลัก (Layout, LARGER KEYS, REGULAR KEY, SMALLER KEYS)
   - ในแต่ละโฟลเดอร์มีโฟลเดอร์ตามแบรนด์ (Acer, ASUS ฯลฯ)
   - มีรูปภาพ .jpg/.png อยู่ในโฟลเดอร์แบรนด์

#### ทดสอบการใส่หลาย URL

1. ใส่ 2-3 URL ในช่อง TARGET URL แต่ละบรรทัดต่อเนื่องกัน
2. เลือกโฟลเดอร์
3. กด START EXTRACTION
4. ดูว่า progress bar ควบคุม 0/N URL และเสร็จทีละ URL

#### ทดสอบ error handling

1. ใส่ URL ที่ผิดหรือเปล่า:
   - ถ้าช่องว่าง → ควรขึ้น warning "No URL?"
   - ถ้าใส่ URL ไม่ใช่ → ควร log error "Cannot open web!" และทำ URL ต่อไป

#### ทดสอบไม่เลือกโฟลเดอร์

1. ใส่ URL แต่ไม่เลือกโฟลเดอร์
2. กด START → ควรขึ้น warning "Choose destination folder first!"

**Expected result**: แอปทำงานผ่านทุกกรณีโดยไม่มี crash และแสดงผลลัพธ์ตามที่คาด

**Actual result**: [ใส่ผลจริงที่เห็น]

## Release checklist

[Template]

### ก่อนส่งงานให้เป็น .exe

- [ ] ทดสอบบน Python แล้ว `python main.py` ทำงานได้
- [ ] ติดตั้ง dependencies ใหม่: `pip install -r requirements.txt`
- [ ] Build ใหม่: `python -m PyInstaller --noconsole --onedir --icon=icon.ico --name "Key_Scraper" main.py`
- [ ] ทดสอบ .exe ที่ `dist/Key_Scraper/` ทำงานได้
- [ ] ตรวจว่าโฟลเดอร์ `dist/` มี `_internal` ครบ dependencies
- [ ] อัปเดต CHANGELOG.md ให้พร้อม release
- [ ] อัปเดต HANDOFF.md ให้เป็นปัจจุบัน

### ก่อนสร้าง installer (.iss)

- [ ] ไฟล์ build ทำงานได้แล้ว
- [ ] ตรวจสอบ path ใน `Create Installer.iss` (ต้องชี้ไปที่ `dist\\onedir\\Key Scraper 2.0\\*`)
- [ ] มี icon.ico อยู่ในโฟลเดอร์เดียกกับสคริปต์
- [ ] Owner ตรวจสอบและอนุมัติก่อน build installer จริง

### Owner ทดสอบกับผู้ใช้จริง

- [ ] ส่ง .exe หรือ installer ให้ผู้ใช้ทดลองกด
- [ ] ผู้ใช้ตั้งโฟลเดอร์สำหรับเก็บรูปตามที่ตั้งไว้
- [ ] ผู้ใช้ใส่ URL และกด Start ตามที่สอน
- [ ] ตรวจสอบโฟลเดอร์ที่ได้ตรงตามที่คาด
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

---

## [v2.0.0] — Clean Slate Release (2026-09-23, commit 49c344d)

**Fact**: Single root-commit history force-pushed to `origin main` (https://github.com/pppoipoit/Key-Scraper.git).
No source-code changes in this release — docs bookkeeping only (CURRENT_TASK, HANDOFF, CHANGELOG).

**Release status**: GitHub Release v2.0.0 NOT yet published (gh CLI not installed on this machine).
Owner action required — publish at https://github.com/pppoipoit/Key-Scraper/releases/new with tag `v2.0.0`.

**Release notes for owner to paste** (title: ✨ Elite Edition v2.0.0 — Clean Slate & Portfolio Ready):

🎉 **Initial Public Release: Elite Edition v2.0.0**

This is the 'Clean Slate' release of the LaptopKey Scraper. The repository has been completely restructured for professional portfolio showcase.

**What's included in v2.0.0:**
- 🚀 Parallel multi-URL scraping engine (up to 4 concurrent threads via ThreadPoolExecutor)
- 🎨 Custom Dark UI with PIL-rendered gradient widgets
- 📂 Automated brand detection and Korean/English folder structuring
- 🛡️ Thread-safe UI architecture (root.after() pattern)
- 📦 Ready-to-build Inno Setup configuration (relative paths)

**Tech Stack:** Python 3.x | Tkinter | Pillow | BeautifulSoup4 | Requests | PyInstaller

*Note: Compiled binaries (.exe) are not hosted on GitHub to keep the repository clean. Build from source using PyInstaller.*

**© 2026 pppoipoit x DRKMTTR Studio**
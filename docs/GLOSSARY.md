# Glossary

ตาราง:
| Term | Meaning in plain Thai | Technical meaning | Example | Notes |
|------|----------------------|-------------------|---------|-------|
| App | โปรแกรมที่รันบนคอมพิวเตอร์ | Application executable file | Key_Scraper.exe | รันได้บน Windows |
| URL | ลิงก์เว็บไซต์ที่ผู้ใช้ใส่ | Uniform Resource Locator | https://example.com/product123 | ใส่ได้หลายบรรทัดในช่อง TARGET URL |
| Folder | โฟลเดอร์บนคอมพิวเตอร์ | Directory for file storage | D:\Downloads\Keyboards | ผู้ใช้เลือกเพื่อเก็บรูปที่ดาวน์โหลด |
| Brand | ยี่ห้อแล็ปท็อป | Manufacturer name detected from model code | Acer, ASUS, MSI, SAMSUNG, DELL, HP, Lenovo, TOSHIBA, Apple, Others | สรุปจากตัวอักษรแรกของรหัสโมเดล (เช่น ACxxx → Acer) |
| Model code | รหัสรุ่นคีย์บอร์ด | String identifying specific keyboard model | AC763, GN845, MGX650 | ดึงจาก div.f_box ใน HTML |
| Scraping | การดึงข้อมูลจากเว็บไซต์ | Automated HTTP GET + HTML parsing | ดึงรูปจาก URL ด้วย requests + BeautifulSoup | ทำใน background thread |
| Parallel processing | ประมวลผลหลายอย่างพร้อมกัน | ThreadPoolExecutor ทำงานหลาย URL พร้อม | ประมวลผล 4 URL พร้อมในเวลาเดียวกัน | MAX_PARALLEL_URLS = 4 |
| Progress bar | แสดงความคืบหน้า | GradientProgressBar widget | แถบสีเขียว-น้ำเงินที่เคลื่อนที่จากซ้ายไปขวา | แสดงจำนวน URL ที่เสร็จแล้ว / ทั้งหมด |
| Log panel | แผ่นบันทึกกิจกรรม | Scrollable Text widget | "Spying on 3 website(s) now..." | แสดงข้อความแบบเรียลไทม์ระหว่างทำงาน |
| Thread | กระบวนการทำงานแยก | Independent flow of execution | Background thread ทำ scraping | ป้องกัน UI ค้างขณะทำงานหนัก |
| Daemon thread | Thread ที่จบเมื่อโปรแกรมจบ | Thread ที่จะถูกบังคับจบเมื่อ main thread ออก | Scraping thread เป็น daemon | ทำให้ปิดแอปได้ทันทีแม้กำลังทำงาน |
| root.after() | วิธีอัปเดต UI จาก thread อื่น | Tkinter method เพื่อความปลอดภัย | app.root.after(0, lambda: update_ui()) | ใช้เพราะ tkinter widget ต้องแก้จาก main thread เท่านั้น |
| requirements.txt | รายการไลบรารีที่ต้องติดตั้ง | Python package list | requests, beautifulsoup4, Pillow | ใช้คำสั่ง `pip install -r requirements.txt` |
| PyInstaller | เครื่องมือแปลง .py เป็น .exe | Python application bundler | แปลง main.py เป็น Key_Scraper.exe | ใช้ตัวเลือก --onedir เพื่อความเร็วในการ start |
| Inno Setup | โปรแกรมสร้าง installer | Windows installer generator | สร้าง Key_Scraper_Setup.exe จากไฟล์ .iss | สร้างไฟล์ติดตั้งพร้อม shortcut และ auto-run |
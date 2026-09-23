# ⚠️ KNOWN ISSUES — Key Scraper v2 (Santa Claude Audit 2026-09-17)

> **Cline: อ่านไฟล์นี้คู่กับ HANDOFF.md และ CURRENT_TASK.md ทุก session**
> ไฟล์นี้บันทึกปัญหาที่ตรวจพบจาก cross-session audit โดย Santa Claude

---

## 🔴 CRITICAL — ต้องแก้ก่อน build exe ครั้งต่อไป

### ISSUE-001: `main.py` ใน Drive เป็นเวอร์ชันเก่า → icon หาไม่เจอตอนรัน exe

**Status**: ❌ ยังไม่แก้ (ณ 2026-09-17)
**Impact**: build เป็น exe ได้ปกติ แต่ icon ที่ title bar จะไม่ขึ้น (หา icon.ico ไม่เจอ)

เวอร์ชันเก่าที่อยู่ใน Drive ตอนนี้:
```python
# ❌ ผิด — __file__ ใช้ไม่ได้เมื่อ PyInstaller ฝัง main.py เป็น bytecode
icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ICON_FILENAME)
```

เวอร์ชันใหม่ที่ถูกต้อง (ต้องมี `get_base_path()`):
```python
# ✅ ถูก — ตรวจสอบว่ารันแบบ frozen (exe) หรือ .py แล้วเลือก path ให้เหมาะสม
import sys

def get_base_path():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS  # PyInstaller แตกไฟล์ชั่วคราวไว้ที่นี่
    return os.path.dirname(os.path.abspath(__file__))

def set_app_icon(root):
    icon_path = os.path.join(get_base_path(), ICON_FILENAME)
    ...
```

**วิธีตรวจ**: เปิด `main.py` แล้วค้น `def get_base_path` — ถ้าไม่พบ = ยังเป็นเวอร์ชันเก่า
**Fix**: เจ้าของอัพโหลด `main.py` เวอร์ชันใหม่ (จาก chat history) ทับไฟล์เดิมใน Drive

---

### ISSUE-002: `app.py` ใน Drive ขนาดคอลัมน์ยังเป็นค่าเก่า (ก่อนสลับ)

**Status**: ❌ ยังไม่แก้ (ณ 2026-09-17)
**Impact**: UI แสดง Log ช่องใหญ่ URL ช่องเล็ก — ผิดจากที่เจ้าของอนุมัติ

```python
# ❌ ค่าใน Drive ปัจจุบัน — Log(590) ใหญ่กว่า URL(300)
left_w, right_w = 300, 590

# ✅ ค่าที่ถูกต้องตามที่เจ้าของสั่ง — URL(590) ใหญ่กว่า Log(300)
left_w, right_w = 590, 300
```

**วิธีตรวจ**: เปิด `app.py` ค้น `left_w, right_w` — ถ้าเป็น `300, 590` = ยังเก่าอยู่
**Fix**: เจ้าของอัพโหลด `app.py` เวอร์ชันใหม่ (จาก chat history) ทับไฟล์เดิมใน Drive

---

## 🟡 MEDIUM — ควรแก้ในโอกาสถัดไป

### ISSUE-003: ไฟล์ icon ซ้อนกัน 2 ตัว สร้างความสับสน

**Status**: ⚠️ รอเจ้าของ confirm ทิศทาง
**รายละเอียด**:
- `icon.ico` — สร้างโดย Santa Claude (โทนชมพู-ม่วงตามธีม) — **ตัวที่โค้ดอ้างถึงตอนนี้**
- `Logo_BK.ico` — ไฟล์ icon ดั้งเดิมของเจ้าของ — **ไม่มีโค้ดอ้างถึง ลอยอยู่เฉยๆ**

**Fix** (ต้องถามเจ้าของก่อน):
- ถ้าจะใช้ `Logo_BK.ico`: แก้ `main.py` บรรทัด `ICON_FILENAME = "icon.ico"` → `"Logo_BK.ico"` และแก้คำสั่ง PyInstaller build (`--icon=Logo_BK.ico --add-data "Logo_BK.ico;."`)
- ถ้าจะใช้ `icon.ico` ต่อ: ลบ `Logo_BK.ico` ทิ้งได้เลย

### ISSUE-004: CURRENT_TASK.md Status header ไม่ตรงกับ Completion Summary

**Status**: ⚠️ doc-only fix (ไม่กระทบโค้ด)
**รายละเอียด**: `CURRENT_TASK.md` บรรทัดต้นบอก `Status: In Progress` แต่ส่วนล่างบอก `COMPLETED - 2026-09-15`
**Fix**: แก้บรรทัด Status เป็น `Status: ✅ COMPLETED (TC-001)` + สร้าง task ใหม่ TC-002

---

## ✅ ตรวจสอบแล้ว ไม่มีปัญหา

| Component | ผลตรวจ |
|---|---|
| scraper_core.py — โครงสร้างโฟลเดอร์ปลายทาง | ✅ ตรงต้นฉบับ 100% (byte-by-byte verified) |
| Thread safety — widget read from background thread | ✅ แก้แล้ว (อ่านใน main thread ก่อนส่ง thread) |
| PIL._tkinter_finder hidden import | ✅ ระบุใน README.txt build command แล้ว |
| gradient_widgets.py — self._w naming collision | ✅ แก้แล้ว (ใช้ self.card_w/card_h แทน) |
| .clinerules/ 6 ไฟล์ | ✅ ครบถ้วน เนื้อหาถูกต้อง |
| docs/ 23 ไฟล์ | ✅ ครบถ้วน |
| requirements.txt | ✅ ถูกต้อง (requests, beautifulsoup4, Pillow) |
| Create Installer.iss | ✅ ใช้ recursesubdirs ครบ, PrivilegesRequired=admin |

---

## 📋 Task ถัดไปสำหรับ Session ใหม่: TC-002

```
TC-002: Apply Santa Audit Fixes
Priority: HIGH
Scope: doc + config เท่านั้น ห้ามแก้ scraping logic

Steps:
1. ขอ/อัพโหลด main.py เวอร์ชันใหม่ (get_base_path) ทับ Drive
2. ขอ/อัพโหลด app.py เวอร์ชันใหม่ (left_w=590) ทับ Drive
3. ถามเจ้าของ: Logo_BK.ico หรือ icon.ico?
4. แก้ CURRENT_TASK.md Status → COMPLETED + สร้าง task entry TC-002 ใหม่
5. ลบ/เก็บ icon ที่ไม่ใช้ตามที่เจ้าของตอบ
```

---
*Audit by: Santa Claude (ซานต้าคลอดด์) | Date: 2026-09-17*
*Drive folder: Key Scraper → docs/KNOWN_ISSUES.md*

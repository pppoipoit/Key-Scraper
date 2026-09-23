# -*- coding: utf-8 -*-
"""
theme.py
---------
รวมค่าสี / ฟอนต์ / ระยะห่างทั้งหมดของแอปไว้ที่เดียว (Single Source of Truth)
โทนสีอ้างอิงจากภาพ Dark Dashboard ที่เจ้านายส่งมา (กรมท่า-ม่วงเข้ม + การ์ด gradient
สีเหลือง/ส้ม, ฟ้า/น้ำเงิน, ฟ้าอมเขียว, ชมพู/แดงเข้ม)
"""

# ---------- พื้นหลังหลัก ----------
BG_APP = "#11132A"          # พื้นหลังนอกสุดของหน้าต่าง (กรมท่าเข้มเกือบดำ)
BG_PANEL = "#1A1D3A"        # พื้นการ์ด/พาเนลหลัก
BG_PANEL_LIGHT = "#222648"  # พื้นการ์ดที่ซ้อนอยู่ในพาเนล (เช่น กล่อง entry, log)
BORDER_SOFT = "#30355E"     # ขอบเส้นบางๆ ใช้แยกส่วน

# ---------- ตัวอักษร ----------
TEXT_TITLE = "#F5F6FA"      # หัวข้อหลัก ขาวอมฟ้า
TEXT_BODY = "#C7CBE8"       # ข้อความทั่วไป
TEXT_MUTED = "#7E84B3"      # ข้อความรอง/คำอธิบาย
TEXT_ON_GRADIENT = "#FFFFFF"

FONT_FAMILY = "Segoe UI"
FONT_TITLE = (FONT_FAMILY, 20, "bold")
FONT_SUBTITLE = (FONT_FAMILY, 10)
FONT_LABEL = (FONT_FAMILY, 9, "bold")
FONT_BODY = (FONT_FAMILY, 10)
FONT_LOG = ("Consolas", 9)
FONT_BUTTON = (FONT_FAMILY, 11, "bold")

# ---------- ชุดสี Gradient (ตามการ์ดในภาพ dashboard) ----------
GRADIENT_SUNSET = ("#FACC15", "#FB7185")   # เหลือง -> ส้มชมพู (การ์ด 98.5%)
GRADIENT_OCEAN = ("#60A5FA", "#2563EB")    # ฟ้า -> น้ำเงิน (การ์ด 2,481)
GRADIENT_MINT = ("#34D399", "#0E7490")     # เขียวมินต์ -> ฟ้าอมเขียว (การ์ด 31,124)
GRADIENT_BERRY = ("#F472B6", "#9333EA")    # ชมพู -> ม่วง (การ์ด $2,125 / ปุ่มหลัก)

GRADIENT_PRIMARY_BTN = GRADIENT_BERRY      # ปุ่ม START EXTRACTION
GRADIENT_PROGRESS = GRADIENT_MINT          # แถบ progress bar

# ---------- ระยะ/ขนาดมุมโค้ง ----------
RADIUS_PANEL = 16
RADIUS_BUTTON = 14
RADIUS_FIELD = 10
SHADOW_BLUR = 14
SHADOW_OPACITY = 90
SHADOW_OFFSET = (0, 6)

# ---------- ขนาดหน้าต่าง ----------
WINDOW_WIDTH = 980
WINDOW_HEIGHT = 600

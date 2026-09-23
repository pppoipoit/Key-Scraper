# -*- coding: utf-8 -*-
"""
main.py
--------
จุดเริ่มต้นโปรแกรม: สร้างหน้าต่างหลัก, ตั้งชื่อ/ขนาด/icon แล้วส่งต่อให้ app.App ทำงาน

วิธีตั้ง icon ที่ title bar:
  วางไฟล์ .ico ชื่อ "icon.ico" ไว้โฟลเดอร์เดียวกับไฟล์นี้ (เปลี่ยนชื่อไฟล์ ICON_FILENAME
  ด้านล่างได้ถ้าอยากใช้ชื่ออื่น เช่น "Logo_BK.ico")
"""

import os
import tkinter as tk

import theme
from app import App

ICON_FILENAME = "icon.ico"


def set_app_icon(root):
    """ตั้ง icon ที่ title bar ถ้าหาไฟล์ .ico เจอ (ทำงานเต็มรูปแบบบน Windows)"""
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ICON_FILENAME)
    if os.path.exists(icon_path):
        try:
            root.iconbitmap(icon_path)
        except tk.TclError:
            pass  # บางระบบ (เช่น Linux) ไม่รองรับ .ico โดยตรง ข้ามไปเงียบๆ ไม่ทำแอปพัง


def main():
    root = tk.Tk()
    root.title("LaptopKey Scraper - Elite Edition v2")
    root.configure(bg=theme.BG_APP)
    root.geometry(f"{theme.WINDOW_WIDTH}x{theme.WINDOW_HEIGHT}")
    root.resizable(False, False)
    set_app_icon(root)

    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()

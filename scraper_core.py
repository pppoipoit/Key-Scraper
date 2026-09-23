# -*- coding: utf-8 -*-
"""
scraper_core.py
-----------------
Logic การ scrape/ดาวน์โหลดรูปทั้งหมด (ไม่ยุ่งกับ UI เลย) แยกมาจาก Key_Scraper.py ต้นฉบับ
*** สำคัญ: โครงสร้างโฟลเดอร์ปลายทางต้องตรงกับต้นฉบับ 100% ห้ามแก้เด็ดขาด ***

ของเดิม (Key_Scraper.py) ทำงานทีละ 1 URL เสมอ ในไฟล์นี้แยกฟังก์ชันย่อยออกมา
เพื่อให้ app.py เรียกใช้ "พร้อมกันหลาย URL" ได้ด้วย ThreadPoolExecutor
โดย logic ภายในของแต่ละ URL ยังเหมือนต้นฉบับทุกขั้นตอน
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

PAGE_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36"
}
IMAGE_HEADERS = {"User-Agent": "Mozilla/5.0"}

# ชื่อโฟลเดอร์ปลายทาง - คัดลอกมาจากต้นฉบับทุกตัวอักษร ห้ามแก้!
FOLDER_LAYOUT = "รูปตัวอย่างแผง Keyboard [Layout]"
FOLDER_LARGER = "รูปตัวอย่าง Lugs, Hinge [LARGER KEYS]"
FOLDER_REGULAR = "รูปตัวอย่าง Lugs, Hinge [REGULAR KEY]"
FOLDER_SMALLER = "รูปตัวอย่าง Lugs, Hinge [SMALLER KEYS]"


def get_brand_name(model_name):
    """แยกชื่อแบรนด์จากตัวอักษรหน้าสุดของรหัส Model (logic เดิมทุกจุด ไม่แก้ไข)"""
    prefix = ""
    for char in model_name:
        if char.isalpha():
            prefix += char
        else:
            break
    prefix = prefix.upper()

    if prefix.startswith("AC"):
        return "Acer"
    elif prefix.startswith("AS"):
        return "ASUS"
    elif prefix.startswith("MS"):
        return "MSI"
    elif prefix.startswith("SG"):
        return "SAMSUNG"
    elif prefix.startswith("D"):
        return "DELL"
    elif prefix.startswith("H"):
        return "HP"
    elif prefix.startswith("L"):
        return "Lenovo"
    elif prefix.startswith("T"):
        return "TOSHIBA"
    elif prefix.startswith("A"):
        return "Apple"
    else:
        return "Others"


def download_image(url, folder, filename, log_callback=None):
    """ดาวน์โหลดรูปเดียว (logic เดิมทุกจุด: stream, header, นามสกุลไฟล์, chunk 1024)"""
    if not url:
        return False
    try:
        res = requests.get(url, stream=True, headers=IMAGE_HEADERS)
        if res.status_code == 200:
            ext = url.split(".")[-1].split("?")[0].lower()
            if len(ext) > 4 or not ext:
                ext = "jpg"

            file_path = os.path.join(folder, f"{filename}.{ext}")
            with open(file_path, "wb") as f:
                for chunk in res.iter_content(1024):
                    f.write(chunk)
            return True
    except Exception as e:
        if log_callback:
            log_callback(f"Error downloading: {filename} | {e}")
    return False


def fetch_page(url, log_callback=None):
    """โหลดหน้าเว็บ + parse เป็น BeautifulSoup คืนค่า None ถ้าผิดพลาด (error message เดิม)"""
    try:
        res = requests.get(url, headers=PAGE_HEADERS)
        res.raise_for_status()
    except Exception as e:
        if log_callback:
            log_callback(f"Cannot open web! Check your URL again, Boss! | {e}")
        return None
    return BeautifulSoup(res.text, "html.parser")


def extract_keyboard_image_url(soup, base_url):
    """หา div.keyboar_wrap > img แล้วคืน absolute url (logic เดิม)"""
    keyboard_wrap = soup.find("div", class_="keyboar_wrap")
    if keyboard_wrap:
        img_tag = keyboard_wrap.find("img")
        if img_tag and img_tag.get("src"):
            return urljoin(base_url, img_tag.get("src"))
    return None


def get_detail_rows(soup):
    """หา div.detail_row ทั้งหมด ไม่รวมแถวหัวตาราง (head_row) - logic เดิม"""
    rows = soup.find_all("div", class_="detail_row")
    return [row for row in rows if "head_row" not in row.get("class", [])]


def build_brand_folders(base_dir, brand_folder):
    """
    สร้าง dict path ปลายทางทั้ง 4 หมวด ตามโครงสร้างเดิมเป๊ะๆ:
    base_dir/<หมวด>/<แบรนด์>/
    """
    return {
        "layout": os.path.join(base_dir, FOLDER_LAYOUT, brand_folder),
        "larger": os.path.join(base_dir, FOLDER_LARGER, brand_folder),
        "regular": os.path.join(base_dir, FOLDER_REGULAR, brand_folder),
        "smaller": os.path.join(base_dir, FOLDER_SMALLER, brand_folder),
    }


def process_row(row, base_url, keyboard_img_url, base_dir, log_callback=None):
    """
    ประมวลผล 1 แถว (1 โมเดล): หาชื่อโมเดล -> แยกแบรนด์ -> สร้างโฟลเดอร์ -> ดาวน์โหลดรูป
    คืนค่า model_name ถ้าประมวลผลสำเร็จ (เจอ f_box) มิฉะนั้นคืน None
    *** ลำดับรูปและปลายทางตรงตามต้นฉบับ: img[0]=regular, img[1]=larger, img[2]=smaller ***
    """
    model_box = row.find("div", class_="f_box")
    if not model_box:
        return None

    model_name = model_box.text.strip()
    brand_folder = get_brand_name(model_name)

    if log_callback:
        log_callback(f"Handling Model: {model_name} -> Brand: {brand_folder}")

    folders = build_brand_folders(base_dir, brand_folder)
    for f_path in folders.values():
        os.makedirs(f_path, exist_ok=True)

    img_tags = row.find_all("img")
    reg_url = urljoin(base_url, img_tags[0].get("src")) if len(img_tags) > 0 and img_tags[0].get("src") else None
    large_url = urljoin(base_url, img_tags[1].get("src")) if len(img_tags) > 1 and img_tags[1].get("src") else None
    small_url = urljoin(base_url, img_tags[2].get("src")) if len(img_tags) > 2 and img_tags[2].get("src") else None

    if reg_url:
        download_image(reg_url, folders["regular"], model_name, log_callback)
    if large_url:
        download_image(large_url, folders["larger"], model_name, log_callback)
    if small_url:
        download_image(small_url, folders["smaller"], model_name, log_callback)
    if keyboard_img_url:
        download_image(keyboard_img_url, folders["layout"], model_name, log_callback)

    return model_name


def process_single_url(url, base_dir, log_callback=None):
    """
    ประมวลผล 1 URL แบบครบ (เทียบเท่า process_scraping เดิม แต่ทำทีละ URL)
    คืนค่า จำนวนโมเดลที่เจอ (int) ; ใช้เรียกแบบ parallel ได้จาก app.py
    """
    if log_callback:
        log_callback(f"Spying on website now: {url}")

    soup = fetch_page(url, log_callback)
    if soup is None:
        return 0

    keyboard_img_url = extract_keyboard_image_url(soup, url)
    rows = get_detail_rows(soup)

    model_count = 0
    if log_callback:
        log_callback(f"Found it! Sucking images for {url} ...")

    for row in rows:
        model_name = process_row(row, url, keyboard_img_url, base_dir, log_callback)
        if model_name:
            model_count += 1

    if log_callback:
        if model_count == 0:
            log_callback(f"Oh? No models found at {url}!")
        else:
            log_callback(f"Done {url} -> {model_count} models downloaded!")

    return model_count

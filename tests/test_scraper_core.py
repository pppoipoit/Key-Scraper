# -*- coding: utf-8 -*-
"""
tests/test_scraper_core.py
---------------------------
Unit tests สำหรับ pure logic ใน scraper_core.py (TC-002 / OQ-006)

- ไม่ใช้ network จริง (mock requests.get ทั้งหมด)
- ไม่แตะ UI และห้าม import tkinter (คนละ thread/model กับ app.py)
- ใช้ unittest ของ Python ล้วนๆ ไม่เพิ่ม dependency

รันจาก root ของโปรเจกต์: python -m unittest discover tests
"""

import os
import sys
import tempfile
import unittest
from unittest import mock

# ให้ import scraper_core ได้จากทุก working directory (ไฟล์นี้อยู่ใน tests/ ใต้ root)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from bs4 import BeautifulSoup

import scraper_core
from scraper_core import (
    FOLDER_LARGER,
    FOLDER_LAYOUT,
    FOLDER_REGULAR,
    FOLDER_SMALLER,
    build_brand_folders,
    download_image,
    extract_keyboard_image_url,
    get_brand_name,
    get_detail_rows,
)


class TestGetBrandName(unittest.TestCase):
    """ADR-002: brand detection ต้องตรงกับ logic เดิมทุกประการ — ห้ามแก้"""

    def test_get_brand_name_known_prefixes(self):
        cases = [
            ("AC315-52G", "Acer"),
            ("AS01234", "ASUS"),
            ("MS-16F4", "MSI"),
            ("SG12345", "SAMSUNG"),
            ("DELL-G3", "DELL"),
            ("HP-14CF", "HP"),
            ("LENOVO-IDP", "Lenovo"),
            ("TOSHIBA-SAT", "TOSHIBA"),
            ("A123", "Apple"),
        ]
        for model, expected in cases:
            with self.subTest(model=model):
                self.assertEqual(get_brand_name(model), expected)

    def test_get_brand_name_single_letter_prefixes(self):
        cases = [
            ("D1", "DELL"),
            ("H1", "HP"),
            ("L1", "Lenovo"),
            ("T1", "TOSHIBA"),
            ("A1", "Apple"),
        ]
        for model, expected in cases:
            with self.subTest(model=model):
                self.assertEqual(get_brand_name(model), expected)

    def test_get_brand_name_prefix_order_ac_as_beat_a(self):
        # "AC" / "AS" ต้องชนะ "A" (ไม่งั้น AC315 จะกลายเป็น Apple)
        self.assertEqual(get_brand_name("AC315"), "Acer")
        self.assertEqual(get_brand_name("AS1234"), "ASUS")

    def test_get_brand_name_is_case_insensitive(self):
        self.assertEqual(get_brand_name("ac15"), "Acer")
        self.assertEqual(get_brand_name("as22"), "ASUS")
        self.assertEqual(get_brand_name("dell g3"), "DELL")

    def test_get_brand_name_unknown_prefix_maps_to_others(self):
        cases = ["XX123", "S123", "12345", "9XYZ", ""]
        for model in cases:
            with self.subTest(model=model):
                self.assertEqual(get_brand_name(model), "Others")


class TestUrlJoining(unittest.TestCase):
    """URL string manipulation: urljoin logic ใน extract_keyboard_image_url"""

    def test_relative_src_is_joined_to_base_url(self):
        soup = BeautifulSoup(
            '<div class="keyboar_wrap"><img src="img/kb.jpg"/></div>', "html.parser"
        )
        result = extract_keyboard_image_url(
            soup, "https://example.com/products/view.php?id=1"
        )
        self.assertEqual(result, "https://example.com/products/img/kb.jpg")

    def test_absolute_src_is_kept_unchanged(self):
        soup = BeautifulSoup(
            '<div class="keyboar_wrap"><img src="https://cdn.example.com/kb.png"/></div>',
            "html.parser",
        )
        result = extract_keyboard_image_url(soup, "https://example.com/page.html")
        self.assertEqual(result, "https://cdn.example.com/kb.png")

    def test_root_relative_src_joins_to_domain(self):
        soup = BeautifulSoup(
            '<div class="keyboar_wrap"><img src="/uploads/kb.png"/></div>', "html.parser"
        )
        result = extract_keyboard_image_url(soup, "https://example.com/page.html")
        self.assertEqual(result, "https://example.com/uploads/kb.png")

    def test_missing_keyboard_wrap_returns_none(self):
        soup = BeautifulSoup(
            '<div class="other"><img src="x.jpg"/></div>', "html.parser"
        )
        self.assertIsNone(extract_keyboard_image_url(soup, "https://example.com/"))

    def test_img_without_src_returns_none(self):
        soup = BeautifulSoup('<div class="keyboar_wrap"><img/></div>', "html.parser")
        self.assertIsNone(extract_keyboard_image_url(soup, "https://example.com/"))


class TestGetDetailRows(unittest.TestCase):
    """get_detail_rows: ต้องไม่รวมแถวหัวตาราง (head_row) — logic เดิม"""

    def test_head_row_is_excluded(self):
        html = """
        <div class="detail_row head_row"><div class="f_box">Header</div></div>
        <div class="detail_row"><div class="f_box">AC123</div></div>
        <div class="detail_row"><div class="f_box">AS456</div></div>
        """
        soup = BeautifulSoup(html, "html.parser")
        rows = get_detail_rows(soup)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0].find("div", class_="f_box").text.strip(), "AC123")
        self.assertEqual(rows[1].find("div", class_="f_box").text.strip(), "AS456")


class TestBuildBrandFolders(unittest.TestCase):
    """ADR-002: ชื่อโฟลเดอร์เกาหลี + โครงสร้าง path ต้องตรงต้นฉบับ — ห้ามแก้"""

    def test_korean_folder_names_are_unchanged(self):
        self.assertEqual(FOLDER_LAYOUT, "รูปตัวอย่างแผง Keyboard [Layout]")
        self.assertEqual(FOLDER_LARGER, "รูปตัวอย่าง Lugs, Hinge [LARGER KEYS]")
        self.assertEqual(FOLDER_REGULAR, "รูปตัวอย่าง Lugs, Hinge [REGULAR KEY]")
        self.assertEqual(FOLDER_SMALLER, "รูปตัวอย่าง Lugs, Hinge [SMALLER KEYS]")

    def test_paths_include_category_and_brand(self):
        base = os.path.join("some", "base")
        folders = build_brand_folders(base, "Acer")
        self.assertEqual(set(folders), {"layout", "larger", "regular", "smaller"})
        self.assertEqual(folders["layout"], os.path.join(base, FOLDER_LAYOUT, "Acer"))
        self.assertEqual(folders["larger"], os.path.join(base, FOLDER_LARGER, "Acer"))
        self.assertEqual(folders["regular"], os.path.join(base, FOLDER_REGULAR, "Acer"))
        self.assertEqual(folders["smaller"], os.path.join(base, FOLDER_SMALLER, "Acer"))



class TestDownloadImageRetry(unittest.TestCase):
    """TC-002 / OQ-008: retry สูงสุด 3 ครั้ง ห่างกัน 2 วินาที — mock ทั้งหมด ไม่แตะ network"""

    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp_dir.cleanup)
        self.logs = []

    @staticmethod
    def _mock_response(status_code, chunks=None):
        res = mock.Mock()
        res.status_code = status_code
        res.iter_content.return_value = chunks if chunks is not None else [b"image-bytes"]
        return res

    def test_empty_url_returns_false_without_request(self):
        with mock.patch.object(scraper_core.requests, "get") as mock_get:
            result = download_image("", self.tmp_dir.name, "m", self.logs.append)
        self.assertFalse(result)
        mock_get.assert_not_called()

    def test_success_first_attempt_no_retry_no_sleep(self):
        with mock.patch.object(
            scraper_core.requests, "get", return_value=self._mock_response(200)
        ) as mock_get, mock.patch.object(scraper_core.time, "sleep") as mock_sleep:
            result = download_image(
                "https://example.com/pic.jpg", self.tmp_dir.name, "model1", self.logs.append
            )
        self.assertTrue(result)
        self.assertEqual(mock_get.call_count, 1)
        mock_sleep.assert_not_called()
        self.assertTrue(os.path.isfile(os.path.join(self.tmp_dir.name, "model1.jpg")))

    def test_retries_on_5xx_then_succeeds(self):
        responses = [
            self._mock_response(503),
            self._mock_response(500),
            self._mock_response(200),
        ]
        with mock.patch.object(
            scraper_core.requests, "get", side_effect=responses
        ) as mock_get, mock.patch.object(scraper_core.time, "sleep") as mock_sleep:
            result = download_image(
                "https://example.com/pic.png", self.tmp_dir.name, "model2", self.logs.append
            )
        self.assertTrue(result)
        self.assertEqual(mock_get.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 2)
        mock_sleep.assert_called_with(scraper_core.DOWNLOAD_RETRY_DELAY_SECONDS)
        self.assertTrue(any("Retry" in msg for msg in self.logs))

    def test_retries_on_connection_error_then_succeeds(self):
        responses = [
            requests.exceptions.ConnectionError("boom"),
            requests.exceptions.Timeout("too slow"),
            self._mock_response(200),
        ]
        with mock.patch.object(
            scraper_core.requests, "get", side_effect=responses
        ) as mock_get, mock.patch.object(scraper_core.time, "sleep") as mock_sleep:
            result = download_image(
                "https://example.com/pic.jpg", self.tmp_dir.name, "model3", self.logs.append
            )
        self.assertTrue(result)
        self.assertEqual(mock_get.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 2)
        self.assertTrue(os.path.isfile(os.path.join(self.tmp_dir.name, "model3.jpg")))

    def test_gives_up_after_max_retries_and_logs_failure(self):
        with mock.patch.object(
            scraper_core.requests,
            "get",
            side_effect=requests.exceptions.ConnectionError("always down"),
        ) as mock_get, mock.patch.object(scraper_core.time, "sleep") as mock_sleep:
            result = download_image(
                "https://example.com/pic.jpg", self.tmp_dir.name, "model4", self.logs.append
            )
        self.assertFalse(result)
        # attempt แรก + DOWNLOAD_MAX_RETRIES ครั้ง = 4 ครั้ง, sleep ระหว่าง retry = 3 ครั้ง
        self.assertEqual(mock_get.call_count, scraper_core.DOWNLOAD_MAX_RETRIES + 1)
        self.assertEqual(mock_sleep.call_count, scraper_core.DOWNLOAD_MAX_RETRIES)
        self.assertTrue(self.logs[-1].startswith("Error downloading: model4"))

    def test_4xx_fails_immediately_without_retry(self):
        with mock.patch.object(
            scraper_core.requests, "get", return_value=self._mock_response(404)
        ) as mock_get, mock.patch.object(scraper_core.time, "sleep") as mock_sleep:
            result = download_image(
                "https://example.com/pic.jpg", self.tmp_dir.name, "model5", self.logs.append
            )
        self.assertFalse(result)
        self.assertEqual(mock_get.call_count, 1)
        mock_sleep.assert_not_called()
        self.assertTrue(self.logs[-1].startswith("Error downloading: model5"))


if __name__ == "__main__":
    unittest.main()

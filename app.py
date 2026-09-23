# -*- coding: utf-8 -*-
"""
app.py
-------
ประกอบหน้าจอ UI ทั้งหมด (Dark Dashboard style) + ผูก event เข้ากับ scraper_core
- รองรับ URL หลายอันพร้อมกัน (เทียบเท่า "ดูดพร้อมกันหลาย url") ด้วย ThreadPoolExecutor
- ช่อง Log และ URL เลื่อนเมาส์ขึ้นลงได้ (Text + Scrollbar)
- โครงสร้างโฟลเดอร์ปลายทางใช้ scraper_core ทั้งหมด -> ไม่มีการแก้ logic เดิม
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

import theme
import scraper_core as core
from gradient_widgets import GradientPanel, GradientButton, GradientProgressBar

MAX_PARALLEL_URLS = 4  # ดูดพร้อมกันได้สูงสุดกี่ URL ในเวลาเดียวกัน (กันยิง request ถี่เกินไป)


def make_card(parent, width, height, color1, color2, content_bg, radius=None):
    """
    สร้าง 'การ์ด' = GradientPanel (เงา+gradient+มุมโค้ง) ซ้อนด้วย Frame เนื้อในแบบเรียบ
    คืนค่า (panel_canvas, inner_frame) ; ใส่ widget จริงลงใน inner_frame
    """
    radius = radius or theme.RADIUS_PANEL
    panel = GradientPanel(parent, width, height, color1, color2, radius=radius,
                           bg_root=parent["bg"])
    inner = tk.Frame(parent, bg=content_bg)
    inner.place(in_=panel, x=3, y=3, width=width - 6, height=height - 6)
    return panel, inner


def add_mousewheel_scroll(widget):
    """bind การเลื่อนเมาส์ (รองรับ Windows/Mac/Linux) ให้กับ Text widget"""

    def _on_wheel(event):
        if event.delta:
            widget.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif getattr(event, "num", None) == 4:
            widget.yview_scroll(-1, "units")
        elif getattr(event, "num", None) == 5:
            widget.yview_scroll(1, "units")
        return "break"

    widget.bind("<MouseWheel>", _on_wheel)      # Windows / Mac
    widget.bind("<Button-4>", _on_wheel)        # Linux scroll up
    widget.bind("<Button-5>", _on_wheel)        # Linux scroll down


class App:
    def __init__(self, root):
        self.root = root
        self.executor = None
        self._build_ui()

    # ------------------------------------------------------------------ UI
    def _build_ui(self):
        self.root.configure(bg=theme.BG_APP)

        outer = tk.Frame(self.root, bg=theme.BG_APP)
        outer.pack(fill="both", expand=True, padx=22, pady=18)

        self._build_header(outer)

        body = tk.Frame(outer, bg=theme.BG_APP)
        body.pack(fill="both", expand=True, pady=(16, 0))

        left_w, right_w = 300, 590
        card_h = 300

        left_panel, left_inner = make_card(
            body, left_w, card_h, *theme.GRADIENT_OCEAN, theme.BG_PANEL
        )
        left_panel.grid(row=0, column=0, sticky="n")
        self._build_left_column(left_inner, left_w - 6, card_h - 6)

        right_panel, right_inner = make_card(
            body, right_w, card_h, *theme.GRADIENT_MINT, theme.BG_PANEL
        )
        right_panel.grid(row=0, column=1, sticky="n", padx=(18, 0))
        self._build_log_column(right_inner, right_w - 6, card_h - 6)

        self._build_action_row(outer, left_w + right_w + 18)

    def _build_header(self, parent):
        header = tk.Frame(parent, bg=theme.BG_APP)
        header.pack(fill="x")

        badge = GradientPanel(header, 46, 46, *theme.GRADIENT_BERRY, radius=12,
                               bg_root=theme.BG_APP)
        badge.grid(row=0, column=0, rowspan=2, sticky="n")
        badge.create_text(23, 23, text="⌨", font=(theme.FONT_FAMILY, 20), fill="#FFFFFF")

        tk.Label(header, text="LaptopKey Scraper", font=theme.FONT_TITLE,
                 bg=theme.BG_APP, fg=theme.TEXT_TITLE).grid(row=0, column=1, sticky="w", padx=(14, 0))
        tk.Label(header, text="Elite Edition v2 · Multi-URL Parallel Engine",
                 font=theme.FONT_SUBTITLE, bg=theme.BG_APP, fg=theme.TEXT_MUTED
                 ).grid(row=1, column=1, sticky="w", padx=(14, 0))

    def _build_left_column(self, parent, width, height):
        parent.grid_columnconfigure(0, weight=1)
        pad_x = 16

        tk.Label(parent, text="🔗 TARGET URLs  (1 บรรทัด = 1 ลิงก์ ดูดพร้อมกันได้หลายลิงก์)",
                 font=theme.FONT_LABEL, bg=theme.BG_PANEL, fg=theme.TEXT_BODY,
                 wraplength=width - pad_x * 2, justify="left"
                 ).grid(row=0, column=0, sticky="w", padx=pad_x, pady=(14, 6))

        url_frame = tk.Frame(parent, bg=theme.BG_PANEL_LIGHT, highlightthickness=1,
                              highlightbackground=theme.BORDER_SOFT)
        url_frame.grid(row=1, column=0, sticky="we", padx=pad_x)

        self.url_text = tk.Text(url_frame, height=6, width=30, font=theme.FONT_BODY,
                                 bg=theme.BG_PANEL_LIGHT, fg=theme.TEXT_BODY,
                                 insertbackground=theme.TEXT_TITLE, bd=0,
                                 wrap="none", padx=8, pady=8)
        self.url_text.pack(side="left", fill="both", expand=True)
        url_scroll = tk.Scrollbar(url_frame, command=self.url_text.yview,
                                   troughcolor=theme.BG_PANEL, bg=theme.BORDER_SOFT)
        url_scroll.pack(side="right", fill="y")
        self.url_text.configure(yscrollcommand=url_scroll.set)
        add_mousewheel_scroll(self.url_text)

        tk.Label(parent, text="📁 SAVE DESTINATION", font=theme.FONT_LABEL,
                 bg=theme.BG_PANEL, fg=theme.TEXT_BODY
                 ).grid(row=2, column=0, sticky="w", padx=pad_x, pady=(14, 6))

        dest_row = tk.Frame(parent, bg=theme.BG_PANEL)
        dest_row.grid(row=3, column=0, sticky="we", padx=pad_x)
        dest_row.grid_columnconfigure(0, weight=1)

        dest_box = tk.Frame(dest_row, bg=theme.BG_PANEL_LIGHT, highlightthickness=1,
                             highlightbackground=theme.BORDER_SOFT)
        dest_box.grid(row=0, column=0, sticky="we")
        self.path_entry = tk.Entry(dest_box, font=theme.FONT_BODY, bg=theme.BG_PANEL_LIGHT,
                                    fg=theme.TEXT_BODY, insertbackground=theme.TEXT_TITLE,
                                    bd=0, relief="flat")
        self.path_entry.pack(fill="both", expand=True, padx=8, pady=8)
        import os
        default_path = os.path.join(os.path.expanduser("~"), "Desktop", "LaptopKey_Downloads")
        self.path_entry.insert(0, default_path)

        browse_btn = tk.Button(dest_row, text="Browse", font=(theme.FONT_FAMILY, 9, "bold"),
                                bg=theme.BG_PANEL_LIGHT, fg=theme.TEXT_TITLE, bd=0,
                                activebackground=theme.BORDER_SOFT, cursor="hand2",
                                command=self.browse_folder)
        browse_btn.grid(row=0, column=1, sticky="ns", padx=(8, 0), ipadx=8)

    def _build_log_column(self, parent, width, height):
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        pad_x = 16

        tk.Label(parent, text="🖥️ SYSTEM STATUS LOG", font=theme.FONT_LABEL,
                 bg=theme.BG_PANEL, fg=theme.TEXT_BODY
                 ).grid(row=0, column=0, sticky="w", padx=pad_x, pady=(14, 6))

        log_frame = tk.Frame(parent, bg=theme.BG_PANEL_LIGHT, highlightthickness=1,
                              highlightbackground=theme.BORDER_SOFT)
        log_frame.grid(row=1, column=0, sticky="nswe", padx=pad_x, pady=(0, 14))

        self.log_text = tk.Text(log_frame, font=theme.FONT_LOG, bg=theme.BG_PANEL_LIGHT,
                                 fg="#8BE9C8", bd=0, wrap="word", padx=10, pady=10,
                                 state="disabled")
        self.log_text.pack(side="left", fill="both", expand=True)
        log_scroll = tk.Scrollbar(log_frame, command=self.log_text.yview,
                                   troughcolor=theme.BG_PANEL, bg=theme.BORDER_SOFT)
        log_scroll.pack(side="right", fill="y")
        self.log_text.configure(yscrollcommand=log_scroll.set)
        add_mousewheel_scroll(self.log_text)

        self._log_message("System ready. Waiting for Boss's command.")

    def _build_action_row(self, parent, total_width):
        action = tk.Frame(parent, bg=theme.BG_APP)
        action.pack(fill="x", pady=(20, 0))

        self.start_btn = GradientButton(
            action, text="🚀 START EXTRACTION", command=self.start_download_thread,
            width=total_width, height=50, color1=theme.GRADIENT_PRIMARY_BTN[0],
            color2=theme.GRADIENT_PRIMARY_BTN[1], font=theme.FONT_BUTTON,
            bg_root=theme.BG_APP,
        )
        self.start_btn.pack(fill="x")

        progress_wrap = tk.Frame(parent, bg=theme.BG_APP)
        progress_wrap.pack(fill="x", pady=(14, 0))

        self.progress_bar = GradientProgressBar(
            progress_wrap, width=total_width, height=14,
            color1=theme.GRADIENT_PROGRESS[0], color2=theme.GRADIENT_PROGRESS[1],
            track_color=theme.BG_PANEL_LIGHT, bg_root=theme.BG_APP,
        )
        self.progress_bar.pack(fill="x")

        self.progress_label = tk.Label(progress_wrap, text="พร้อมเริ่มงาน",
                                        font=theme.FONT_SUBTITLE, bg=theme.BG_APP,
                                        fg=theme.TEXT_MUTED)
        self.progress_label.pack(anchor="w", pady=(6, 0))

    # ------------------------------------------------------------- helpers
    def browse_folder(self):
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, selected_dir)

    def _log_message(self, text):
        self.log_text.configure(state="normal")
        self.log_text.insert(tk.END, f"> {text}\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state="disabled")

    def safe_log(self, text):
        self.root.after(0, lambda: self._log_message(text))

    def safe_set_progress(self, fraction, label_text):
        def _update():
            self.progress_bar.set_progress(fraction)
            self.progress_label.configure(text=label_text)
        self.root.after(0, _update)

    def safe_toggle_controls(self, running):
        def _update():
            if running:
                self.start_btn.set_state("disabled", text="⏳ SPYING ON WEBSITES...")
                self.url_text.configure(state="disabled")
                self.path_entry.configure(state="disabled")
            else:
                self.start_btn.set_state("normal", text="🚀 START EXTRACTION")
                self.url_text.configure(state="normal")
                self.path_entry.configure(state="normal")
        self.root.after(0, _update)

    # ------------------------------------------------------------ actions
    def start_download_thread(self):
        """
        อ่านค่าจาก widget ตรงนี้ (ทำงานบน main thread อยู่แล้ว เพราะถูกเรียกจาก
        ปุ่มกด/event ของ Tkinter) แล้วส่งค่าเป็นพารามิเตอร์ให้ thread พื้นหลังทำงานต่อ
        *** ห้ามให้ background thread เรียก self.url_text.get()/self.path_entry.get()
            ตรงๆ เด็ดขาด เพราะ Tkinter widget อ่าน/เขียนได้แค่จาก main thread เท่านั้น
            (เจอบัค RuntimeError: main thread is not in main loop จริงตอนเทสต์) ***
        """
        raw_text = self.url_text.get("1.0", tk.END)
        urls = [line.strip() for line in raw_text.splitlines() if line.strip()]
        base_dir = self.path_entry.get().strip()

        if not urls:
            self._log_message("No URL? Want me to download from heaven or what?!")
            messagebox.showwarning("Warning", "No URL? Want me to download from heaven or what?!")
            return
        if not base_dir:
            self._log_message("Choose destination folder first!")
            messagebox.showwarning("Warning", "Choose destination folder first!")
            return

        threading.Thread(target=self.process_scraping, args=(urls, base_dir), daemon=True).start()

    def process_scraping(self, urls, base_dir):
        """รันบน background thread เท่านั้น - ห้ามแตะ Tkinter widget ตรงๆ ในนี้
        ใช้ safe_log / safe_set_progress / safe_toggle_controls (ผ่าน root.after) เท่านั้น"""
        self.safe_toggle_controls(True)
        self.safe_set_progress(0.0, f"กำลังเริ่มงาน 0/{len(urls)} URL")
        self.safe_log(f"Spying on {len(urls)} website(s) now, wait a second Boss...")

        total_urls = len(urls)
        completed_urls = 0
        total_models = 0
        lock = threading.Lock()

        def _run_one(url):
            return url, core.process_single_url(url, base_dir, log_callback=self.safe_log)

        with ThreadPoolExecutor(max_workers=min(MAX_PARALLEL_URLS, total_urls)) as executor:
            futures = [executor.submit(_run_one, u) for u in urls]
            for future in as_completed(futures):
                try:
                    _url, model_count = future.result()
                except Exception as e:
                    self.safe_log(f"Unexpected error: {e}")
                    model_count = 0
                with lock:
                    completed_urls += 1
                    total_models += model_count
                    frac = completed_urls / total_urls
                    self.safe_set_progress(
                        frac, f"เสร็จแล้ว {completed_urls}/{total_urls} URL")

        self.safe_toggle_controls(False)

        if total_models == 0:
            self.safe_log("Oh? No models found! Are you sure you gave me the right URL, Boss?")
            self.root.after(0, lambda: messagebox.showinfo(
                "Result", "Oh? No models found! Are you sure you gave me the right URL, Boss?"))
        else:
            self.safe_log(f"Finish already, Boss! Downloaded {total_models} models "
                           f"from {total_urls} URL(s)!")
            self.root.after(0, lambda: messagebox.showinfo(
                "Success",
                f"Finish already, Boss! Downloaded {total_models} models!\n"
                f"Separated by Brands completely!"))

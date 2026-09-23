# -*- coding: utf-8 -*-
"""
gradient_widgets.py
--------------------
รวม widget แบบ custom ที่ใช้ PIL วาดพื้นหลัง gradient + มุมโค้ง + shadow เบาๆ
เพื่อให้ได้ลุค "การ์ด dashboard" ตามภาพตัวอย่างที่เจ้านายส่งมา
(Tkinter ปกติทำ gradient/มุมโค้ง/shadow ไม่ได้ ต้องพึ่ง PIL ช่วยวาดเป็นรูปแล้วแปะ)
"""

import tkinter as tk
from PIL import Image, ImageDraw, ImageTk, ImageFilter


# ----------------------------------------------------------------------------
# Helper functions (pure PIL, ไม่พึ่ง Tk เลย เทสต์แยกได้)
# ----------------------------------------------------------------------------
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def make_gradient(width, height, color1, color2, direction="horizontal"):
    """สร้างภาพ gradient เรียบ (RGB) ขนาด width x height"""
    width = max(1, int(width))
    height = max(1, int(height))
    c1 = hex_to_rgb(color1)
    c2 = hex_to_rgb(color2)
    base = Image.new("RGB", (width, height), c1)
    top = Image.new("RGB", (width, height), c2)
    mask = Image.new("L", (width, height))
    mask_data = []
    if direction == "horizontal":
        for _y in range(height):
            for x in range(width):
                mask_data.append(int(255 * (x / max(width - 1, 1))))
    else:  # vertical
        for y in range(height):
            row_val = int(255 * (y / max(height - 1, 1)))
            mask_data.extend([row_val] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


def rounded_mask(width, height, radius):
    width = max(1, int(width))
    height = max(1, int(height))
    radius = max(0, min(int(radius), width // 2, height // 2))
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=255)
    return mask


def make_rounded_gradient(width, height, color1, color2, radius=16, direction="horizontal"):
    """gradient + ตัดมุมโค้ง คืนเป็นภาพ RGBA"""
    grad = make_gradient(width, height, color1, color2, direction).convert("RGBA")
    mask = rounded_mask(width, height, radius)
    grad.putalpha(mask)
    return grad


def make_rounded_solid(width, height, color, radius=16):
    width = max(1, int(width))
    height = max(1, int(height))
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    radius = max(0, min(int(radius), width // 2, height // 2))
    draw.rounded_rectangle([0, 0, width - 1, height - 1], radius=radius, fill=hex_to_rgb(color) + (255,))
    return img


def make_shadow(width, height, radius=16, blur=14, opacity=90, offset=(0, 6)):
    """เงานุ่มๆด้านหลังการ์ด คืนภาพ RGBA ที่ขนาดใหญ่กว่า width/height (เผื่อระยะเบลอ)"""
    width = max(1, int(width))
    height = max(1, int(height))
    pad = blur * 2
    canvas = Image.new("RGBA", (width + pad * 2, height + pad * 2), (0, 0, 0, 0))
    solid = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    mask = rounded_mask(width, height, radius)
    black = Image.new("RGBA", (width, height), (0, 0, 0, opacity))
    solid.paste(black, (0, 0), mask)
    canvas.paste(solid, (pad + offset[0], pad + offset[1]), solid)
    canvas = canvas.filter(ImageFilter.GaussianBlur(blur / 2.2))
    return canvas, pad


# ----------------------------------------------------------------------------
# Tkinter widgets
# ----------------------------------------------------------------------------
class GradientPanel(tk.Canvas):
    """
    Canvas ที่มีพื้นหลังเป็นการ์ด gradient/solid มุมโค้ง + shadow เบาๆ
    ใช้แทน tk.Frame ตรงไหนก็ได้ที่อยากให้ดูมีมิติ
    """

    def __init__(self, master, width, height, color1, color2=None, radius=16,
                 direction="horizontal", shadow=True, bg_root="#11132A", **kwargs):
        super().__init__(master, width=width, height=height, highlightthickness=0,
                          bg=bg_root, bd=0, **kwargs)
        # หมายเหตุบัค: ห้ามตั้งชื่อ attribute ว่า self._w / self._h เด็ดขาด!
        # เพราะ Tkinter ใช้ "self._w" เป็น internal attribute เก็บ widget path name
        # (เช่น ".!frame.!canvas") การตั้งทับจะทำให้ widget พังทันที (เจอบัคนี้จริงระหว่างเทสต์)
        self.card_w = width
        self.card_h = height
        self._color1 = color1
        self._color2 = color2 or color1
        self._radius = radius
        self._direction = direction
        self._shadow = shadow
        self._photo_card = None
        self._photo_shadow = None
        self._draw()

    def _draw(self):
        self.delete("all")
        if self._shadow:
            shadow_img, pad = make_shadow(self.card_w, self.card_h, radius=self._radius)
            self._photo_shadow = ImageTk.PhotoImage(shadow_img)
            self.create_image(-pad, -pad, image=self._photo_shadow, anchor="nw")
        card_img = make_rounded_gradient(self.card_w, self.card_h, self._color1, self._color2,
                                          radius=self._radius, direction=self._direction)
        self._photo_card = ImageTk.PhotoImage(card_img)
        self.create_image(0, 0, image=self._photo_card, anchor="nw")


class GradientButton(tk.Canvas):
    """ปุ่ม gradient มุมโค้ง + shadow พร้อม hover/click effect"""

    def __init__(self, master, text, command, width=200, height=46,
                 color1="#F472B6", color2="#9333EA", radius=14,
                 font=("Segoe UI", 11, "bold"), text_color="#FFFFFF",
                 bg_root="#11132A", state="normal"):
        super().__init__(master, width=width, height=height, highlightthickness=0,
                          bg=bg_root, bd=0, cursor="hand2")
        self.command = command
        self.width_ = width
        self.height_ = height
        self.color1 = color1
        self.color2 = color2
        self.radius = radius
        self.font = font
        self.text_color = text_color
        self.text = text
        self._state = state
        self._photo_shadow = None
        self._photo_btn = None
        self._render()
        self.bind("<Button-1>", self._on_click)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

    def _render(self, hover=False):
        self.delete("all")
        shadow_img, pad = make_shadow(self.width_, self.height_, radius=self.radius,
                                       opacity=70 if not hover else 110)
        self._photo_shadow = ImageTk.PhotoImage(shadow_img)
        self.create_image(-pad, -pad, image=self._photo_shadow, anchor="nw")

        c1, c2 = self.color1, self.color2
        if self._state == "disabled":
            c1, c2 = "#3A3D5C", "#2A2D48"
        elif hover:
            c1, c2 = self._lighten(c1), self._lighten(c2)

        btn_img = make_rounded_gradient(self.width_, self.height_, c1, c2,
                                         radius=self.radius, direction="horizontal")
        self._photo_btn = ImageTk.PhotoImage(btn_img)
        self.create_image(0, 0, image=self._photo_btn, anchor="nw")
        fill = self.text_color if self._state != "disabled" else "#8B8FB5"
        self.create_text(self.width_ // 2, self.height_ // 2, text=self.text,
                          font=self.font, fill=fill)

    @staticmethod
    def _lighten(hex_color, amount=22):
        r, g, b = hex_to_rgb(hex_color)
        r = min(255, r + amount)
        g = min(255, g + amount)
        b = min(255, b + amount)
        return f"#{r:02x}{g:02x}{b:02x}"

    def _on_click(self, _event):
        if self._state != "disabled" and self.command:
            self.command()

    def _on_enter(self, _event):
        if self._state != "disabled":
            self._render(hover=True)

    def _on_leave(self, _event):
        if self._state != "disabled":
            self._render(hover=False)

    def set_state(self, state, text=None):
        """state: 'normal' หรือ 'disabled' ; เปลี่ยน text ปุ่มได้พร้อมกัน"""
        self._state = state
        if text is not None:
            self.text = text
        self._render(hover=False)


class GradientProgressBar(tk.Canvas):
    """
    แถบ progress แบบ gradient มุมโค้ง ไม่จำเป็นต้องโชว์ตัวเลข %
    เรียก set_progress(fraction) โดย fraction อยู่ในช่วง 0.0 - 1.0
    """

    def __init__(self, master, width=400, height=14, color1="#34D399", color2="#0E7490",
                 track_color="#222648", radius=7, bg_root="#11132A"):
        super().__init__(master, width=width, height=height, highlightthickness=0,
                          bg=bg_root, bd=0)
        self.width_ = width
        self.height_ = height
        self.color1 = color1
        self.color2 = color2
        self.track_color = track_color
        self.radius = radius
        self._fraction = 0.0
        self._photo_track = None
        self._photo_fill = None
        self._render()

    def _render(self):
        self.delete("all")
        track_img = make_rounded_solid(self.width_, self.height_, self.track_color, radius=self.radius)
        self._photo_track = ImageTk.PhotoImage(track_img)
        self.create_image(0, 0, image=self._photo_track, anchor="nw")

        fill_w = max(0, min(self.width_, int(self.width_ * self._fraction)))
        if fill_w > 2:
            fill_img = make_rounded_gradient(fill_w, self.height_, self.color1, self.color2,
                                              radius=self.radius, direction="horizontal")
            self._photo_fill = ImageTk.PhotoImage(fill_img)
            self.create_image(0, 0, image=self._photo_fill, anchor="nw")

    def set_progress(self, fraction):
        self._fraction = max(0.0, min(1.0, fraction))
        self._render()

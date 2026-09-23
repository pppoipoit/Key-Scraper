# Product Brief

## Product name

LaptopKey Scraper - Elite Edition v2

## One-sentence summary

Desktop application for scraping laptop keyboard images from websites and organizing them by brand and key type automatically.

## Problem being solved

Users need to download keyboard layout images and individual key images (larger keys, regular keys, smaller keys) from specific websites for laptop keyboard identification/replacement purposes. Doing this manually is time-consuming and error-prone.

## Target users

- Laptop repair technicians
- Keyboard replacement parts sellers
- Anyone needing to identify laptop keyboard layouts and key types

## Primary user roles

| Role | Description |
|------|-------------|
| Operator | Runs the app, inputs URLs, selects destination folder, starts extraction |

## Core user journey

1. User launches the application
2. User pastes one or more target URLs (one per line) into the URL box
3. User selects a destination folder for downloaded images
4. User clicks "START EXTRACTION"
5. App scrapes all URLs in parallel (max 4 at a time), showing progress bar and logs
6. App downloads and organizes images into brand-specific folders by key type
7. User receives completion notification with count of models downloaded

## Product goals

- Download keyboard images reliably from target websites
- Organize images into correct folder structure (Layout / Larger Keys / Regular Key / Smaller Keys) by brand
- Support multiple URLs processed in parallel for efficiency
- Provide clear visual feedback (progress, logs) during operation
- Maintain 100% compatibility with original folder structure and file naming

## Non-goals

- Web-based or cloud service
- Support for websites other than the specific target site structure
- Image processing/editing beyond downloading
- Database or user accounts
- Scheduling or automation beyond manual trigger

## Success metrics

- Extraction completes without crashes
- Folder structure matches original specification exactly
- All images downloaded for each model found on page
- Parallel processing works without thread-safety issues

## Constraints

- Windows desktop application (tkinter)
- Python 3.x with requests, beautifulsoup4, Pillow
- Target website structure is fixed (div.keyboar_wrap, div.detail_row, div.f_box)
- Folder names in Thai must match exactly: "รูปตัวอย่างแผง Keyboard [Layout]", "รูปตัวอย่าง Lugs, Hinge [LARGER KEYS]", "รูปตัวอย่าง Lugs, Hinge [REGULAR KEY]", "รูปตัวอย่าง Lugs, Hinge [SMALLER KEYS]"
- Brand detection logic based on model prefix must not change

## Assumptions

- Target website structure remains stable
- Network connectivity available
- User has write permission to destination folder
- Python environment with dependencies installed

## Open questions

- Should the app support more websites in the future?
- Is there a need for export/import of URL lists?
- Should there be a configuration file for MAX_PARALLEL_URLS?

## Last updated

2026-09-14 (Initial bootstrap from repository inspection)
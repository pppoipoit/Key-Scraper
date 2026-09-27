# Windows Compatibility

## Single Build — All Windows Versions

This project uses **Python 3.8.x** which supports **all** target Windows versions.

| Windows Version | Supported | Python Required |
|----------------|-----------|----------------|
| Windows 7      | ✅ Yes    | Python 3.8.x   |
| Windows 8/8.1  | ✅ Yes    | Python 3.8.x   |
| Windows 10     | ✅ Yes    | Python 3.8.x   |
| Windows 11     | ✅ Yes    | Python 3.8.x   |

## Why Python 3.8?

- Python 3.9+ dropped official Windows 7 support
- Python 3.8 is the LAST version that supports Windows 7
- Python 3.8 works perfectly on Windows 10 and 11
- Therefore: **ONE Python version (3.8) = ALL Windows versions**

## Build Command (Single)

```batch
pip install -r requirements.txt
python -m PyInstaller --noconsole --onedir --icon=icon.ico --name "Key_Scraper" main.py
```

## Library Compatibility Note



| Library        | Version Constraint | Reason                                   |
| -------------- | ------------------ | ---------------------------------------- |
| Pillow         | <=9.5.0            | Last version with full Windows 7 support |
| requests       | any                | Works on all Windows versions            |
| beautifulsoup4 | any                | Works on all Windows versions            |

## Decision Record

**ADR-006: Single Build for All Windows Versions**

- Date: 2026-09-27
- Status: Accepted
- Context: Initially created separate build scripts for Win7/Win10. Boss decided Python 3.8 covers all targets.
- Decision: Use ONE build script, ONE requirements.txt, ONE build command for all Windows versions.
- Why: Simpler maintenance, less confusion, fewer files to manage.
- Owner approval: Boss (pppoipoit) on 2026-09-27

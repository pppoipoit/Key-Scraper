# Windows Compatibility Matrix

**Last updated**: 2026-09-27 — Created for multi-version build setup (docs/config only, no source-code changes)
**Verified environment**: Python 3.8.10 on this build machine

---

## Python Version Requirements

| Windows Version | Minimum Python | Maximum Python | Status          |
| --------------- | -------------- | -------------- | --------------- |
| Windows 7       | 3.8            | 3.8            | Legacy Support  |
| Windows 8/8.1   | 3.8            | 3.8            | Legacy Support  |
| Windows 10      | 3.8            | 3.12+          | Fully Supported |
| Windows 11      | 3.8            | 3.12+          | Fully Supported |

## Critical Notes

- Python 3.9+ dropped official Windows 7 support
- For Windows 7 users: MUST use Python 3.8.x
- For Windows 10/11 users: Recommend Python 3.10 or 3.11 for stability
- PyInstaller builds must match target Python version

## Library Compatibility

| Library        | Windows 7 Compatible    | Windows 10/11 Compatible |
| -------------- | ----------------------- | ------------------------ |
| requests       | ✅ (any version)         | ✅ (any version)          |
| beautifulsoup4 | ✅ (any version)         | ✅ (any version)          |
| Pillow         | ⚠️ Use <= 9.5.0 for Win7 | ✅ (latest)               |
| tkinter        | ✅ Python 3.8            | ✅ Python 3.8+            |

---

## Build Matrix

| Target        | Requirements File      | Build Script       | PyInstaller Output          |
| ------------- | ---------------------- | ------------------ | --------------------------- |
| Windows 7/8   | `requirements-win7.txt`  | `build_win7.bat`   | `dist\Key_Scraper_Win7\`    |
| Windows 10/11 | `requirements-win10.txt` | `build_win10.bat`  | `dist\Key_Scraper_Win10\`   |

**Rules:**
- A Win7 build MUST be produced on a machine running Python 3.8.x (PyInstaller bundles the interpreter it runs on).
- A build produced on Python 3.9+ will NOT run on Windows 7.
- Do not mix dependency sets: Win7 builds install `requirements-win7.txt` only (Pillow pinned to <= 9.5.0).

## Fact vs Assumption

- **Fact**: Build machine reports Python 3.8.10 (verified via `python --version` 2026-09-27).
- **Fact**: `requests`, `beautifulsoup4`, `Pillow` are not currently installed in the machine-level environment (verified via `pip list`) — the build scripts install them from the requirements files.
- **Assumption**: Windows 7/8 support status per official Python release lifecycle (Python 3.8 is the last release with Windows 7 support).
- **Open question**: Whether Win7 builds are actually tested on real Windows 7 hardware — not yet verified (see docs/OPEN_QUESTIONS.md if owner wants this tracked).

# Windows Compatibility

> **⚠️ CRITICAL — READ BEFORE BUILDING OR SHIPPING**
>
> **The build MUST be performed with Python 3.8.x.**
> An exe built with Python 3.9+ will fail on Windows 7 with
> `api-ms-win-core-path-l1-1-0.dll is missing`.
> **Old `dist/` artifacts (built before the Python 3.8 rebuild) are NOT Windows 7 compatible.**
>
> **Why this happens (verified 2026-09-28, not a guess):** Python 3.9 dropped official
> Windows 7 support. The 3.9+ runtime DLL imports the API set
> `api-ms-win-core-path-l1-1-0.dll`, which Windows 7 does not ship. The app therefore
> dies *before the window ever appears* — it is not a bug in this project's code.
>
> **How to check any build in 5 seconds:** open the build folder and look inside `_internal`:
>
> | You see | Verdict |
> |---------|---------|
> | `python38.dll` | ✅ Windows 7 capable |
> | `python313.dll` (or `python39/310/311/312.dll`) | ❌ Will **not** run on Windows 7 |

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

**Always confirm the build log header says `Python: 3.8.x` before trusting the output:**

```
440 INFO: PyInstaller: 6.22.3, contrib hooks: 2026.7
440 INFO: Python: 3.8.10          <-- must be 3.8.x
473 INFO: Platform: Windows-10-10.0.26100-SP0
```

## Verified Build — 2026-09-28 (Python 3.8 Rebuild)

Rebuilt on this machine to fix the Windows 7 failure. Facts below were measured, not assumed.

| Item | Value |
|------|-------|
| Output path | `dist\Key_Scraper\` |
| Interpreter | Python **3.8.10** (`C:\Program Files\Python38`) |
| PyInstaller | 6.22.3 |
| Runtime DLL bundled | `python38.dll` ✅ |
| Win7-unsafe API-set imports | **none** (checked all 31 `.exe`/`.dll`/`.pyd` in the bundle) |
| Launch smoke test | GUI stayed alive 8s ✅ |
| Test suite | `Ran 26 tests — OK` |

### Evidence for the old failure

The previous `dist\onedir\Key Scraper 2.0\` bundle was scanned the same way:

| File | Problem |
|------|---------|
| `_internal\python313.dll` | imports `api-ms-win-core-path-l1-1-0.dll` → **the exact error the owner reported** |
| `_internal\cryptography\hazmat\bindings\_rust.pyd` | imports `api-ms-win-core-synch-l1-2-0.dll` → also missing on Win7 |

Note the old bundle also contained `numpy`, `lxml` and `cryptography` — packages **not** in
`requirements.txt`. The old artifact was not produced by the documented build command.

### The PyInstaller version is NOT the problem

PyInstaller 6.x documents that it "runs in Windows 8 and newer" — that is a statement about
the **build machine**, not the machines the exe is copied to. The 6.22.3 Windows bootloader
(`bootloader\Windows-64bit-intel\runw.exe`) was scanned and imports **no** post-Win7 API sets,
so PyInstaller 6.22.3 can still produce a Windows 7-capable exe when the interpreter is 3.8.x.

**Fact vs assumption:** the "Win7-safe" verdict is based on static PE import analysis. The
build has **not** been executed on a real Windows 7 machine — that final confirmation must be
done on the Boss's Windows 7 PC.

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

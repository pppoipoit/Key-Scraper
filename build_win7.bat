@echo off
echo ========================================
echo Building for Windows 7 (Python 3.8)
echo ========================================
echo.
echo IMPORTANT: You must have Python 3.8 installed!
echo Download from: https://www.python.org/downloads/release/python-380/
echo.
pause

REM Install Win7-compatible dependencies
pip install -r requirements-win7.txt

REM Build with PyInstaller
python -m PyInstaller --noconsole --onedir --icon=icon.ico --name "Key_Scraper_Win7" main.py

echo.
echo Build complete! Check dist\Key_Scraper_Win7\ folder
pause

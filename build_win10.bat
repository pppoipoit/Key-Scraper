@echo off
echo ========================================
echo Building for Windows 10/11 (Python 3.10+)
echo ========================================
echo.
echo Recommended: Python 3.10 or 3.11
echo.
pause

REM Install latest dependencies
pip install -r requirements-win10.txt

REM Build with PyInstaller
python -m PyInstaller --noconsole --onedir --icon=icon.ico --name "Key_Scraper_Win10" main.py

echo.
echo Build complete! Check dist\Key_Scraper_Win10\ folder
pause

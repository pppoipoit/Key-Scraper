; -----------------------------------------------------------------------------
; Inno Setup Script Created by Santa Claude for Boss! (Key Scraper 2.0)
; -----------------------------------------------------------------------------
[Setup]
AppId={{C78F9B64-D1E4-42E3-BCE7-9E4571A2E394}
AppName=Key Scraper
AppVersion=2.0.0
AppPublisher=DRKMTTR Studio
DefaultDirName={autopf}\Key Scraper
DefaultGroupName=Key Scraper
DisableProgramGroupPage=yes
PrivilegesRequired=admin
SetupIconFile=icon.ico
OutputDir=dist\installer
OutputBaseFilename=Key_Scraper_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; ดึงไฟล์และโฟลเดอร์ระบบทั้งหมดใน onedir (รวม Key_Scraper.exe + _internal\ ที่มี icon.ico ฝังอยู่แล้ว)
; IMPORTANT (2026-09-28): must point at the Python 3.8.10 build. The old folder
; "dist\onedir\Key Scraper 2.0" is a Python 3.13 build whose python313.dll imports
; api-ms-win-core-path-l1-1-0.dll -> installer would crash on Windows 7.
Source: "dist\Key_Scraper\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\Key Scraper"; Filename: "{app}\Key_Scraper.exe"
Name: "{autodesktop}\Key Scraper"; Filename: "{app}\Key_Scraper.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Key_Scraper.exe"; Description: "{cm:LaunchProgram,Key Scraper}"; Flags: nowait postinstall skipifsilent

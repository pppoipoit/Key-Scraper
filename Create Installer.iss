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
Source: "dist\onedir\Key Scraper 2.0\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\Key Scraper"; Filename: "{app}\Key_Scraper.exe"
Name: "{autodesktop}\Key Scraper"; Filename: "{app}\Key_Scraper.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Key_Scraper.exe"; Description: "{cm:LaunchProgram,Key Scraper}"; Flags: nowait postinstall skipifsilent

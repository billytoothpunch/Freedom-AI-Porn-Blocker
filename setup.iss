[Setup]
AppName=Freedom Blocker
AppVersion=1.2
DefaultDirName={pf}\bammus
DefaultGroupName=bammus
OutputDir=C:\Users\fresh\Documents\rich\app8
OutputBaseFilename=FreedomBlockerInstaller
Compression=lzma
SolidCompression=yes

[Files]
; 🔹 Core executables
Source: "C:\Users\fresh\Documents\rich\app8\dist\freedom_blocker.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\fresh\Documents\rich\app8\dist\watchdog.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\fresh\Documents\rich\app8\dist\preventer.exe"; DestDir: "{app}"; Flags: ignoreversion


; 🔹 NudeNet models
Source: "C:\Users\fresh\Documents\rich\app8\models\*"; DestDir: "{app}\models"; Flags: ignoreversion recursesubdirs createallsubdirs

; 🔹 Tesseract OCR (for text detection)
Source: "C:\Users\fresh\Documents\rich\app8\tesseract\*"; DestDir: "{app}\tesseract"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Freedom_Blocker"; Filename: "{app}\freedom_blocker.exe"

[Registry]

; 🔹 Run Main on startup
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "Main"; ValueData: """{app}\main.exe"""; Flags: uninsdeletevalue

[Run]
; 🔹 Start Freedom Blocker after install
Filename: "{app}\freedom_blocker.exe"; Description: "Run Freedom Blocker"; Flags: nowait postinstall skipifsilent

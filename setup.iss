[Setup]
AppName=Freedom Blocker
AppVersion=1.1
DefaultDirName={pf}\Freedom_Blocker
DefaultGroupName=Freedom_Blocker
OutputDir=C:\Users\fresh\Documents\rich\app5
OutputBaseFilename=FreedomBlockerInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\fresh\Documents\rich\app5\dist\freedom_blocker.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\fresh\Documents\rich\app5\dist\watchdog_1.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\fresh\Documents\rich\app5\dist\watchdog_2.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\fresh\Documents\rich\app5\models\*"; DestDir: "{app}\models"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Freedom_Blocker"; Filename: "{app}\freedom_blocker.exe"

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "Freedom_Blocker"; ValueData: """{app}\freedom_blocker.exe"""; Flags: uninsdeletevalue
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "Watchdog_1"; ValueData: """{app}\watchdog_1.exe"""; Flags: uninsdeletevalue
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "Watchdog_2"; ValueData: """{app}\watchdog_2.exe"""; Flags: uninsdeletevalue

[Run]
Filename: "{app}\freedom_blocker.exe"; Description: "Run Freedom Blocker"; Flags: nowait postinstall skipifsilent


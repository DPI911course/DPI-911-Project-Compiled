## Regsvr32

**Description**
Regsvr32.exe is a command-line program used to register and unregister object linking and embedding controls, including dynamic link libraries (DLLs), on Windows systems. Regsvr32.exe can be used to execute arbitrary binaries

**Assumptions**
Windows Platform, User/Administrator Permissions Required

**Execution**
Run in Command Prompt:

Replace filename with the name of the local file

####regsvr32.exe /s /u /i:#{filename} scrobj.dll

**Detection - Filter**
#### source="WinEventLog:Microsoft-Windows-Sysmon/Operational" sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", "RegSvr32.sct" "C:\\Windows\\system32\\cmd.exe", "SHA1=60733DE225B5C4BFC42FB79E5D1A4F6683243E4A" "C:\\Windows\\System32\\NOTEPAD.EXE", CommandLine
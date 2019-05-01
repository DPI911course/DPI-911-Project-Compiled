## Rootkit

**Description**
Rootkits are programs that hide the existence of malware by intercepting (i.e., Hooking) and modifying operating system API calls that supply system information.

**Assumptions:** 
Linux/macOS/Windows Platform, Administrator/root/SYSTEM Permissions Required

**Execution** 
#### No Test

**Detection Filter(s)**
#### source="WinEventLog:Microsoft-Windows-Sysmon/Operational" sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", "puppetstrings.exe"
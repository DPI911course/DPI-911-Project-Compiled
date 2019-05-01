##Signed Script Proxy Execution

**Description**
Execute a binary, command, or script via a method that interacts with Windows services, such as the Service Control Manager. This can be done by either creating a new service or modifying an existing service.

**Assumptions**
Administrator/SYSTEM Permissions Required

**Execution**
mavinject.exe 1000 /INJECTRUNNING [file_name].dll

**Detection Filter**
source="WinEventLog:Microsoft-Windows-Sysmon/Operational", sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", mavinject.exe CommandLine

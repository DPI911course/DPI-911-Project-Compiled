## Signed Binary Proxy Execution

**Description**
Binaries signed with trusted digital certificates can execute on Windows systems protected by digital signature validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of other files. This behavior may be abused by adversaries to execute malicious files that could bypass application whitelisting and signature validation on system

**Assumptions**
Windows Platform, User Permissions

**Execution**
mavinject.exe #pid /INJECTRUNNING [file_name].dll

**Detection Filter**
source="WinEventLog:Microsoft-Windows-Sysmon/Operational", sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", mavinject.exe CommandLine

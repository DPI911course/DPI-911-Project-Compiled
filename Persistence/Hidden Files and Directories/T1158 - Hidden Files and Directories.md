##Hidden Files and Directories

**Description** 
To prevent normal users from accidentally changing special files on a system, most operating systems have the concept of a ‘hidden’ file. These files don’t show up when a user browses the file system with a GUI or when using normal commands on the command line

**Assumptions**
Linux/macOS/Windows Platform, User Permissions Required

**Execution** 
cmd|powershell> attrib +[h|s|r] filename

**Detection Filter**
source="WinEventLog:Microsoft-Windows-Sysmon/Operational" sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" "C:\\Windows\\system32\\attrib.exe"
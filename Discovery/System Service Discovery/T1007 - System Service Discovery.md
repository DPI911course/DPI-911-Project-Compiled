## System Service Discovery

**Description**
Adversaries may try to get information about registered services. Commands that may obtain information about services using operating system utilities are "sc," "tasklist /svc" using Tasklist, and "net start" using Net, but adversaries may also use other tools as well.

**Assumptions**
Windows Platform, Administrator/User/SYSTEM Permissions Required

**Execution**
#### `cmd> net start`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Discovery/screenshots/system_service_discovery_command1.PNG)

#### `PS> Get-Service | Where {$_.status –eq 'running'}`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Discovery/screenshots/system_service_discovery_command2.PNG)

**Detection Filter(s)**
#### `sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", source = WinEventLog:Microsoft-Windows-Sysmon/Operational, "C:\\Windows\\system32\\net1 start", "CommandLine"`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Discovery/screenshots/system_service_discovery_filter1.PNG)

#### `source = WinEventLog:Microsoft-Windows-PowerShell/Operational, sourcetype = WinEventLog:Microsoft-Windows-PowerShell/Operational, commandinvocation, "Get-Service", NOT "CommandInvocation(Set-StrictMode)", NOT "CommandInvocation(PSConsoleHostReadLine)"`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Discovery/screenshots/system_service_discovery_filter2.PNG)

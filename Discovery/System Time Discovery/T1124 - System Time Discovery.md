## System Time Discovery

**Description**
The system time is set and stored by the Windows Time Service within a domain to maintain time synchronization between systems and services in an enterprise network.

**Assumptions**
Windows Platform, Administrator/User/SYSTEM Permissions Required

**Execution**
#### `cmd> net time <perameters>`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Discovery/screenshots/system_time_discovery_command.PNG)

**Detection Filter(s)**
#### `sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", source = WinEventLog:Microsoft-Windows-Sysmon/Operational, "C:\\Windows\\system32\\net1  time", "CommandLine"`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Discovery/screenshots/system_time_discovery_filter.PNG)

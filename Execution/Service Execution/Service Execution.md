## Service Execution

**Description**
Execute a binary, command, or script via a method that interacts with Windows services, such as the Service Control Manager. This can be done by either creating a new service or modifying an existing service.

**Assumptions**
Administrator/SYSTEM Permissions Required

**Execution**
#### `cmd> net start`
#### `cmd> net stop`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Execution/screenshots/service_execution_command.PNG)

**Detection Filter**
#### `sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", source = WinEventLog:Microsoft-Windows-Sysmon/Operational, "C:\\Windows\\system32\\net1", "CommandLine"`

![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Execution/screenshots/service_execution_filter.PNG)

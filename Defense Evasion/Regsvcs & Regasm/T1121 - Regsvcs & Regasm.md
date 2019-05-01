## Regsvcs/Regasm

**Description**
Adversaries can use Regsvcs and Regasm to proxy execution of code through a trusted Windows utility. Both utilities may be used to bypass process whitelisting through use of attributes within the binary to specify code that should be run before registration or unregistration: [ComRegisterFunction] or [ComUnregisterFunction] respectively. The code with the registration and unregistration attributes will be executed even if the process is run under insufficient privileges and fails to execute.

**Assumptions**
Windows Platform, User/Administrator Permissions Required

**Execution**
#### `cmd> regasm.exe /U <filename>`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Defense%20Evasion/screenshots/regsvcs-regasm_command.PNG)

#### `cmd> regsvcs.exe /U <filename>`

**Detection Filter(s)**
#### `source="WinEventLog:Microsoft-Windows-Sysmon/Operational" sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", "C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\regasm.exe", ".cs"`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Defense%20Evasion/screenshots/regsvcs-regasm_filter.PNG)

#### `source="WinEventLog:Microsoft-Windows-Sysmon/Operational" sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", "C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\regsvcs.exe", ".cs"`

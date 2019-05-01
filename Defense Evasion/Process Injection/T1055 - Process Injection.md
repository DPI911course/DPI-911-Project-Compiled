## Process Injection

**Description**
Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges.

**Assumptions**
Linux/macOS/Windows Platform, Administrator/User/SYSTEM/root Permissions Required, Effective Permissions: SYSTEM/User/Administrator/root

**Execution**
#### `PS> mavinject $pid /INJECTRUNNING <dll>`

![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Defense%20Evasion/screenshots/process_injection_command.PNG)

**Detection Filter(s)**
#### `"SourceName=Microsoft-Windows-PowerShell", "mavinject 7832 /INJECTRUNNING .\\T1055\\src\\x64\\T1055.dll"`

![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Defense%20Evasion/screenshots/process_injection_filter.PNG)

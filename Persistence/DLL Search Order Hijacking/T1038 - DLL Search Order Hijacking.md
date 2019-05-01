## DLL Search Order Hijacking

**Description**
Windows systems use a common method to look for required DLLs to load into a program. Adversaries may take advantage of the Windows DLL search order and programs that ambiguously specify DLLs to gain privilege escalation and persistence.
**Assumptions**
Windows Platform with PowerShell Enabled

**Execution**
#### `cmd> net user /add <username> <password>`
#### `PS> Write-HijackDLL`
Before you can run the hijacking module, Powersploit will need to be installed into the **Modules** folder located within PowerShell's System32 folder. Please see Powersploit's GitHub for modules. (https://github.com/PowerShellMafia/PowerSploit)

**Detection Filter(s)**
#### `source="WinEventLog:Microsoft-Windows-PowerShell/Operational" sourcetype="WinEventLog:Microsoft-Windows-PowerShell/Operational", "Write-HijackDLL", "Function"`

![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Persistence/screenshots/dll_search_order_hijacking_filter1.PNG)

![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Persistence/screenshots/dll_search_order_hijacking_filter2.PNG)

## Input Capture

**Description**
Adversaries can use methods of capturing user input for obtaining credentials for Valid Accounts and information Collection that include keylogging and user input field interception.

**Assumptions**
Linux/macOS/Windows Platform, Administrator/SYSTEM Permissions Required

**Execution**
#### `PS> `.\Get-Keystrokes.ps1 -LogPath <file path>
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Collection/screenshots/input_capture_command.PNG)

**Detection Filter(s)**
#### `source = WinEventLog:Microsoft-Windows-PowerShell/Operational, sourcetype = WinEventLog:Microsoft-Windows-PowerShell/Operational, NOT "CommandInvocation(Set-StrictMode)", NOT "CommandInvocation(PSConsoleHostReadLine)", "Get-Keystrokes.ps1"`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Collection/screenshots/input_capture_filter.PNG)

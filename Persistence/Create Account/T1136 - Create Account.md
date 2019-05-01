## Create Account

**Description**
Adversaries with a sufficient level of access may create a local system or domain account. Such accounts may be used for persistence that do not require persistent remote access tools to be deployed on the system.

**Assumptions**
Linux/macOS/Windows Platform, Administrator Permissions

**Execution**
#### `cmd> net user /add <username> <password>`
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Persistence/screenshots/create_account_command.PNG)
#### `PS> New-LocalUser "<username>" -Password $Password`
For ease of use, store the password within a variable when using PowerShell.

**Detection Filter(s)**
#### `sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational", source = WinEventLog:Microsoft-Windows-Sysmon/Operational, "C:\\Windows\\system32\\net1  user /add", "CommandLine"`\
![alt text](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project/blob/master/Persistence/screenshots/create_account_filter.PNG)

#### `source = WinEventLog:Microsoft-Windows-PowerShell/Operational, sourcetype = WinEventLog:Microsoft-Windows-PowerShell/Operational, commandinvocation, NOT "CommandInvocation(Set-StrictMode)", NOT "CommandInvocation(PSConsoleHostReadLine)", "New-LocalUser"`

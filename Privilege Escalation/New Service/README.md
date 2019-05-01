# Technique Description

## T1050 - New Service
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1050/)
<blockquote>
When operating systems boot up, they can start programs or applications called services that perform background system functions. [1] A service's configuration information, including the file path to the service's executable, is stored in the Windows Registry.

Adversaries may install a new service that can be configured to execute at startup by using utilities to interact with services or by directly modifying the Registry. The service name may be disguised by using a name from a related operating system or benign software with Masquerading. Services may be created with administrator privileges but are executed under SYSTEM privileges, so an adversary may also use a service to escalate privileges from administrator to SYSTEM. Adversaries may also directly start services through Service Execution.
</blockquote>

# Assumption
The assumption here is that no one on this endpoint shouldbe creating a new service manually, through commandline.

# Execution
Reference to Red-Atomic T1050 https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1050

# Detection

## Visibility
Use Sysmon command line monitoring for known technqiues used by APTs listed, for example Wingbird uses of "sc.exe", Sakula's use of "net start" command and finally the use of PowerShell for local service creation.

## Splunk Filter
Wingbird - Service.exe, Splunk filter recommended is host=SPLUNKFWD IntegrityLevel="high" app="C:\\Windows\\System32\\sc.exe" source="WinEventLog:Microsoft-Windows-Sysmon/Operational"
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Privilege-escalation/New%20Service/Screenshots/1.png">
</p>

Sakula use of net start, Splunk filter recommended host=SPLUNKFWD net start CommandLine="C:\\Windows\\system32\\net1  start" source="WinEventLog:Microsoft-Windows-Sysmon/Operational" Image="C:\\Windows\\System32\\net1.exe"
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Privilege-escalation/New%20Service/Screenshots/2.png">
</p>

Use of PowerShell to create local test service along with recommended Splunk filter
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Privilege-escalation/New%20Service/Screenshots/3.png">
</p>

<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Privilege-escalation/New%20Service/Screenshots/4.png">
</p>
 

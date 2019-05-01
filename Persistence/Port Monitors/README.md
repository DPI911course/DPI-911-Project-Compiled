# Technique Description

## T1013 -  Port Monitors 
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1013/)
<blockquote>
A port monitor can be set through the [1] API call to set a DLL to be loaded at startup. [1] This DLL can be located in C:\Windows\System32 and will be loaded by the print spooler service, spoolsv.exe, on boot. The spoolsv.exe process also runs under SYSTEM level permissions. [2] Alternatively, an arbitrary DLL can be loaded if permissions allow writing a fully-qualified pathname for that DLL to HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors. The Registry key contains entries for the following: Local Port Standard TCP/IP Port USB Monitor WSD Port
</blockquote>

# Assumption
For this technique we have to assume that any new keys entered into the registry at HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors should be considered malicious.

# Execution
There were not Atomics from the Red-Atomic team for this technique.

# Detection

## Visibility
Ensure that Sysmon is monitoring changes to the following registry: HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Port%20Monitors/Screenshots/1.png">
</p>

Ensure that sysmonconfig-export.xml configuration file is updated to monitor changes to the specified registry above
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Port%20Monitors/Screenshots/2.png">
</p>

## Splunk Filter
You want to monitor for EventID 12 at the specified registry, any changes, additions or keys deleted should be alerted.
host=SPLUNKFWD signature="Registry object added or deleted"  EventID=12 object_path="HKLM\\System\\CurrentControlSet\\Control\\Print\\Monitors\\*"
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Port%20Monitors/Screenshots/3.png">
</p>

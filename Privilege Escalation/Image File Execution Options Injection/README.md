# Technique Description

## T1183 - Image File Execution Options Injection 
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1183/)
<blockquote>
Image File Execution Options (IFEO) enable a developer to attach a debugger to an application. When a process is created, a debugger present in an application’s IFEO will be prepended to the application’s name, effectively launching the new process under the debugger (e.g., "C:\dbg\ntsd.exe -g notepad.exe"). [1]

IFEOs can be set directly via the Registry or in Global Flags via the GFlags tool. [2] IFEOs are represented as Debugger values in the Registry under HKLM\SOFTWARE{\Wow6432Node}\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\ where is the binary on which the debugger is attached. [1]
</blockquote>

# Assumption
The assumption here is that no user on the endpoint should be using a debugger in the first place. Therefore, if it were compromised and an adversary uses a debugger we would be monitoring the correct registry for changes.

# Execution
Execution applied as per the methods outlined by the Red Atomics team, https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1183/T1183.md#atomic-test-1---ifeo-add-debugger

# Detection

## Visibility
Ensure that the registry HKLM\SOFTWARE{\Wow6432Node}\Microsoft\Windows NT\CurrentVersion\Image File Execution Options is being monitored. As this techniques involves the debugger attaching to this registry before spawning a new process.
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Privilege-escalation/Image%20File%20Execution%20Options%20Injection/Screenshots/1.png">
</p>

Next make the changes in the sysmonconfig-export.xml files are updated. 
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Privilege-escalation/Image%20File%20Execution%20Options%20Injection/Screenshots/2.png">
</p>

## Splunk Filter

### Atomic Test #1 - IFEO Add Debugger
As we can see here that Sysmon is picking up changes to the registry in question after applying our attack from Red Atomics.
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Privilege-escalation/Image%20File%20Execution%20Options%20Injection/Screenshots/3.png">
</p>

Following Splunk filter allows us to monitor changes to the specified registry for any changes, the main objective here is to catch the “debugger” object being used. host=SPLUNKFWD winword object_path="HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\*" EventID=13 object=Debugger
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Privilege-escalation/Image%20File%20Execution%20Options%20Injection/Screenshots/4.png">
</p>

### Atomic Test #2 - IFEO Global Flags
Following Splunk filter will capture changes to the registry in question as well as the object GlobalFlag: 
host=SPLUNKFWD winword object_path="HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\*" EventID=13 object=GlobalFlag
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Privilege-escalation/Image%20File%20Execution%20Options%20Injection/Screenshots/5.png">
</p>










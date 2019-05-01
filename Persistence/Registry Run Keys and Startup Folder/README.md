# Technique Description

## T1060 - Registry Run Keys / Startup Folder 
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1060/)
<blockquote>
Adding an entry to the "run keys" in the Registry or startup folder will cause the program referenced to be executed when a user logs in. [1] These programs will be executed under the context of the user and will have the account's associated permissions level.

The following run keys are created by default on Windows systems: \
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
\
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce 
\
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run 
\
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce
</blockquote>

# Assumption
The assumption here is that there should be no keys entered to any of the Run keys in the registry. 

# Execution
The execution method used is from Red-Atomics atomics T1060 https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1060/T1060.md

# Detection

## Visibility
Ensure that the sysmonconf-export.xml file is configured to being monitoring for registry keys recommended by MITRE ATT&CK.
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Registry%20Run%20Keys%20and%20Startup%20Folder/Screenshots/1.png">
</p>

Ensure that Sysmon is updated with changes to the config file.
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Registry%20Run%20Keys%20and%20Startup%20Folder/Screenshots/2.png">
</p>

## Splunk Filter

### Atomic Test #1 - Reg Key Run
As per the Atomic Red Team attack we made changes to the following registry: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run. Next we can see that these changes were picked up by Sysmon Operation, which is monitoring that specific registry for any changes. 
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Registry%20Run%20Keys%20and%20Startup%20Folder/Screenshots/3.png">
</p>

Following Splunk filter will monitor and for changes made to this director: host=SPLUNKFWD splwow64 EventID=13 TargetObject="HKU\\S-1-5-21-2374700888-3469647544-1377038430-1000\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\C:\\Windows\\*" tag=change
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Registry%20Run%20Keys%20and%20Startup%20Folder/Screenshots/4.png">
</p>

### Atomic Test #2 - Reg Key RunOnce
Here we make changes to the following registry, HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run. In the background we can see that Sysmon has picked up activity on its log. 
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Registry%20Run%20Keys%20and%20Startup%20Folder/Screenshots/5.png">
</p>

Following Splunk filter will allow us to monitor changes to this registry: host=SPLUNKFWD object_path="HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx\\*" tag=change EventID=13
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Registry%20Run%20Keys%20and%20Startup%20Folder/Screenshots/6.png">
</p>

### Atomic Test #3 - PowerShell Registry RunOnce
Here we see attempts to the registry key made from PowerShell appearing in Sysmon logs as per the third Red Atomic attack
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Registry%20Run%20Keys%20and%20Startup%20Folder/Screenshots/7.png">
</p>

Following Splunk filter can monitor the registry key NextRun for changes along with the user of the PowerShell process. host=SPLUNKFWD object_path="HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\NextRun" EventID=12 process="powershell.exe" object=NextRun
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Registry%20Run%20Keys%20and%20Startup%20Folder/Screenshots/8.png">
</p>

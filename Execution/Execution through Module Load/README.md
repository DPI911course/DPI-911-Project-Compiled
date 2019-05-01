# Technique Description

## T1129 -  Execution through Module Load 
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1129/)
<blockquote>
The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention (UNC) network paths. This functionality resides in NTDLL.dll and is part of the Windows Native API which is called from functions like CreateProcess(), LoadLibrary(), etc. of the Win32 API. [1]
</blockquote>

# Assumption
This technique is difficult to monitor with any of the tools we have discussed. There are too many DLL loads that can occur making monitoring and detection efforts pointless. Mitigation techqniues such as limiting module loads to %SystemRoot% and %ProgramFiles% are recommended as per ATT&CK.

# Execution

# Detection

## Visibility

## Splunk Filter

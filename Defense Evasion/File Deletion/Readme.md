# Technique Description

## T1107 - File Deletion
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1107/)
<blockquote>
Malware, tools, or other non-native files dropped or created on a system by an adversary may leave traces behind as to what was done within a network and how. Adversaries may remove these files over the course of an intrusion to keep their footprint low or remove them at the end as part of the post-intrusion cleanup process.

There are tools available from the host operating system to perform cleanup, but adversaries may use other tools as well. Examples include native cmd functions such as DEL, secure deletion tools such as Windows Sysinternals SDelete, or other third-party file deletion tools.
</blockquote>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised, and that any files that were deleted was by the attacker as a means to evade our defenses. We also asume that a regular user is not going to delete files using command line and powershell etc.

# Execution
The Atomic-Red-Team T1089 module describes the test for this technique (https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1107/T1107.md)

<b>Test 1 - Deleting files using command line:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Deleting-File.PNG">
</p>

<b>Test 2 - Deleting files using Powershell:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Deleting-File-Powershell.PNG">
</p>

<b>Test 3 - Deleting volume shadow copies using vssadmin:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Deletion-vssadmin.PNG">
</p>

<b>Test 4 - Deleting volume shadow copies with wmic:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Deletion-wmic.PNG">
</p>

<b>Test 5 - Removing boot time recovery measures:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Deleting-bcedit.PNG">
</p>

<b>Test 6 - Deleting windows backup catalogs:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Deleting-bcedit.PNG">
</p>

# Detection
Detection is done by monitoring processes, command line arguments and file directories. we look for the arguments like vssadmin, wmic, wbadmin and fltmc.exe unload whihc could indicate tools are being disabled.

## Splunk Filter
The following splunk query will allow us to detect these techniques

<b>Filter 1 - Splunk filter to detect command line deletion:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Splunk-DeleteFile.PNG">
</p>

<b>Filter 2 - Splunk filter to detect powershell deletion:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Splunk-File-Powershell.PNG">
</p>

<b>Filter 3 - Splunk filter to detect vssadmin deletion:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Splunk-vssadmin.PNG">
</p>

<b>Filter 4 - Splunk filter to detect wmic deletion:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Splunk-wmic.PNG">
</p>

<b>Filter 5 - Splunk filter to detect bcdedit deletion:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Splunk-bcdedit.PNG">
</p>

<b>Filter 6 - Splunk filter to detect wbadmin deletion:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/File%20Deletion%20-%20T1107/Screenshots/Splunk-wbadmin.PNG">
</p>

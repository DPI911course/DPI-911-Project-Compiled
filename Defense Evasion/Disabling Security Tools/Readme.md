# Technique Description

## T1089 - Disabling Security Tools
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1089/)
<blockquote>
Adversaries may disable security tools to avoid possible detection of their tools and activities. This can take the form of killing security software or event logging processes, deleting Registry keys so that tools do not start at run time, or other methods to interfere with security scanning or event reporting.
</blockquote>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised, and that any security tools that were disabled was by the attacker as a means to evade our defenses.

# Execution
The Atomic-Red-Team T1089 module describes the test for this technique (https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1089/T1089.md)

<b>Test 1 - Killing the AntiVirus process:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/Disabling%20Security%20Tools%20-%20T1089/Screenshots/Disabling-Antivirus.PNG">
</p>

<b>Test 2 - Unloading the Sysmon Driver:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/Disabling%20Security%20Tools%20-%20T1089/Screenshots/Disabling-Sysmon.PNG">
</p>

# Detection
Detection is done by monitoring processes and command line arguments. we look for the arguments like taskkill and fltmc.exe unload which could indicate tools are being disabled.

## Splunk Filter
The following splunk query will allow us to detect these techniques

<b>Filter 1 - Splunk filter to detect command line argument of Antivirus being killed</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/Disabling%20Security%20Tools%20-%20T1089/Screenshots/Splunk-Antivirus.PNG">
</p>

<b>Filter 2 - Splunk filter to detect Process of Antivirus being killed</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/Disabling%20Security%20Tools%20-%20T1089/Screenshots/Splunk-Antivirus-2.PNG">
</p>

<b>Filter 3 - Splunk filter to detect Unloading Sysmon driver</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/Disabling%20Security%20Tools%20-%20T1089/Screenshots/Splunk-Sysmon.PNG">
</p>


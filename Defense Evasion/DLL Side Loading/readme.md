# Technique Description

## T1073 - DLL-Side-Loading
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1012/)
<blockquote>
Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

The Registry contains a significant amount of information about the operating system, configuration, software, and security. Some of the information may help adversaries to further their operation within a network.
</blockquote>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised, and that a vulnerable application was already compramised with the dll side loading to run commands.

# Execution

there is no Atomic module for this Technique , so to execute this, we modified the dll used and checked the hash of the dll to see if any changes where made. to the dll that the programe was using.

# Detection
Detection is done by monitoring processes of services and creating a baseline of dlls their where using once the dll was changes we comepare the hash found in the baseline and the one with the dll side loading and if they don't match that means the dll has been modified.

<b>Test 1: compare the dll with the baseline no changes made</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/DLL-Side-Loading-T1073/Pictures/same.png">
</p>

<b>Test 2: compare the dll with the side loaded dll (i.e changes) the test shows failed</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/DLL-Side-Loading-T1073/Pictures/Windows7_Victim-2019-04-09-19-07-31.png">
</p>



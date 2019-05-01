# Technique Description

## T1039 - Data from Network Shared Drive
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1039/)
<blockquote>
Sensitive data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that are accessible from the current system prior to Exfiltration.

Adversaries may search network shares on computers they have compromised to find files of interest. Interactive command shells may be in use, and common functionality within cmd may be used to gather information.
</blockquote>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised, and that copying of files from the network shared drive was an attempt by attacker to collect data. We also asume that benign users do not use the command line to copy files from the network share.

# Execution
This technique did not have a red atomic module. On the MITRE ATT&CK framework it said that the threat group menuPass used the net use command as well as robocopy to access files from a network shared drive. Therefore, we will simulate this activity and detect it using splunk.

<b>Test 1 - Using net use to map a drive:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Collection/Data%20from%20Network%20Shared%20Drive%20-%20T1039/Screenshots/NetUse.PNG">
</p>

<b>Test 2 - Using robocopy to copy files:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Collection/Data%20from%20Network%20Shared%20Drive%20-%20T1039/Screenshots/Robocopy.PNG">
</p>

# Detection
Detection is done by monitoring processes and command line arguments. we look for the arguments like net use and robocopy which could indicate that shares are being accessed.

## Splunk Filter
The following splunk query will allow us to detect these techniques

<b>Filter 1 - Splunk filter to detect net use:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Collection/Data%20from%20Network%20Shared%20Drive%20-%20T1039/Screenshots/Splunk-NetUse.PNG">
</p>

<b>Filter 2 - Splunk filter to detect robocopy:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Collection/Data%20from%20Network%20Shared%20Drive%20-%20T1039/Screenshots/Splunk-Robocopy.PNG">
</p>


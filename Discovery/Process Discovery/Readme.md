# Technique Description

## T1057 - Process Discovery
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1057/)
<blockquote>
Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software running on systems within the network.
</blockquote>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised, and that any command line tools that were used to gather information about process was done by the attacker to discover what is running on the system. Begning users would not use the tasklist utility from command line.

# Execution
This technique did not have any red atomic modules. The way we simulated process discovery was by running the tasklist command on the victim and looked for ways to detect it on splunk. 

<b>Test 1 - Running tasklist:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Discovery/Process%20Discovery%20-%20T1057/Screenshots/tasklist.png">
</p>

# Detection
Detection is done by monitoring processes and command line arguments. we look for the arguments like tasklist which could indicate that information gathering is taking place.

## Splunk Filter
The following splunk query will allow us to detect these techniques

<b>Filter 1 - Splunk filter to detect process discovery</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Discovery/Process%20Discovery%20-%20T1057/Screenshots/Splunk-tasklist.png">
</p>



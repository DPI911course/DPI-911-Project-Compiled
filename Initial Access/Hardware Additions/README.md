# Technique Description
## T1200 - Hardware Additions
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1200/)
<blockquote> Computer accessories, computers, or networking hardware may be introduced into a system as a vector to gain execution. While public references of usage by APT groups are scarce, many penetration testers leverage hardware additions for initial access. Commercial and open source products are leveraged with capabilities such as passive network tapping [1], man-in-the middle encryption breaking [2], keystroke injection [3], kernel memory reading via DMA [4], adding new wireless access to an existing network [5], and others.</blockquote>

# Assumption
Assumption taken for this end point is that it sits in a corporate network where hardware additions are not permitted without prior approval.

# Execution
To execute this we inserted USB drives into a an endpoint in our test environment.

# Detection

## Visibility
Sysmon must be enabled on the end point and Splunk Forwarder must be forwarding events from DriverFrameworks-Usermode/Operational.
The EventID 2100 indicates new hardware additions, therefore this is the EvendID analysts need to look out for.
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Initial-Access/Hardware%20Additions-T1200/Screenshots/1.png">
</p>

## Splunk Filter
The Splunk filter we used to find this event on our end point: 
host=SPLUNKFWD sourcetype="XMLWinEventLog:Microsoft-Windows-DriverFrameworks-UserMode/Operational" EventID 2101
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Initial-Access/Hardware%20Additions-T1200/Screenshots/2.png">
</p>

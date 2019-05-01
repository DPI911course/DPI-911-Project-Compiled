# Technique Description
##  Custom Command and Control Protocol - T1094
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1094/)
<blockquote>
Adversaries may communicate using a custom command and control protocol instead of encapsulating commands/data in an existing Standard Application Layer Protocol. Implementations include mimicking well-known protocols or developing custom protocols (including raw sockets) on top of fundamental protocols provided by TCP/IP/another standard network stack.
</blockquote>

# Detection
<blockquote>
Analyze network traffic for ICMP messages or other protocols that contain abnormal data or are not normally seen within or exiting the network.

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. [32]

Monitor and investigate API calls to functions associated with enabling and/or utilizing alternative communication channels.
</blockquote>

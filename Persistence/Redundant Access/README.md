# Technique Description

## T1108 - Redundant Access 
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1108/)
<blockquote>
Adversaries may use more than one remote access tool with varying command and control protocols as a hedge against detection. If one type of tool is detected and blocked or removed as a response but the organization did not gain a full understanding of the adversary's tools and access, then the adversary will be able to retain access to the network. Adversaries may also attempt to gain access to Valid Accounts to use External Remote Services such as external VPNs as a way to maintain access despite interruptions to remote access tools deployed within a target network. [1]

Use of a Web Shell is one such way to maintain access to a network through an externally accessible Web server.
</blockquote>

# Assumption
This technique is difficult to monitor with the tools we have available because it involves analyzing network traffic. This technique involves the adversary using multiple access channels to a compromised endpoint. This would be after persistence is established, therefore network traffic analysis the primary detection method.

# Execution

# Detection

## Visibility

## Splunk Filter

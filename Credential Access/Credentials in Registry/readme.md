# Technique Description

## T1214 - Credentials in Registry
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1214/)

The Windows Registry stores configuration information that can be used by the system or other programs. Adversaries may query the Registry looking for credentials and passwords that have been stored for use by other programs or services. Sometimes these credentials are used for automatic logons.

Example commands to find Registry keys related to password information: [1]

Local Machine Hive: <code>reg query HKLM /f password /t REG_SZ /s</code>
Current User Hive: <code>reg query HKCU /f password /t REG_SZ /s</code>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised, and that any queries that were made to registries were done by the attacker in an attempt to gather information. We also asume that regular users do not make queries to the registry from command line.

# Execution
The Atomic-Red-Team T1214 module describes the test for this technique (https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1214/T1214.md)

<br/>
## Enumeration for Credentials in Registry
Queries to enumerate for credentials in the Registry.

**Supported Platforms:** Windows

#### Run it with `command_prompt`!
```
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```
<br/>

# [Detection](https://attack.mitre.org/techniques/T1214/)

Monitor processes for applications that can be used to query the Registry, such as Reg, and collect command parameters that may indicate credentials are being searched. Correlate activity with related suspicious behavior that may indicate an active intrusion to reduce false positives.

## Splunk Filter
The following splunk query will allow us to detect these techniques

## reg query HKCU
<b>Filter 1:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Credential-Access/Credentials-in-Registry-T1214/Pictures/HKCU.png">
</p>

## reg query HKLM
<b>Filter 2:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Credential-Access/Credentials-in-Registry-T1214/Pictures/regqueryHKLMpassword%20REGSZ%20.png">
</p>

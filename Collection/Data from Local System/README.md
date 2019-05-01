# Technique Description
##  Data from Local System - T1005
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1005/)
<blockquote>
Sensitive data can be collected from local system sources, such as the file system or databases of information residing on the system prior to Exfiltration.

Adversaries will often search the file system on computers they have compromised to find files of interest. They may do this using a Command-Line Interface, such as cmd, which has functionality to interact with the file system to gather information. Some adversaries may also use Automated Collection on the local system.
</blockquote>

# Detection
<blockquote>
Monitor processes and command-line arguments for actions that could be taken to collect files from a system. Remote access tools with built-in features may interact directly with the Windows API to gather data. Data may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.
</blockquote>

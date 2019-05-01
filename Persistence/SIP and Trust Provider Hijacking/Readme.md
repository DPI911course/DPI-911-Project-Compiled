# Technique Description

## T1198 - SIP and Trust Provider Hijacking
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1198/)
<blockquote>
In user mode, Windows Authenticode digital signatures are used to verify a file's origin and integrity, variables that may be used to establish trust in signed code (ex: a driver with a valid Microsoft signature may be handled as safe). The signature validation process is handled via the WinVerifyTrust application programming interface (API) function, which accepts an inquiry and coordinates with the appropriate trust provider, which is responsible for validating parameters of a signature.

Because of the varying executable file types and corresponding signature formats, Microsoft created software components called Subject Interface Packages (SIPs) to provide a layer of abstraction between API functions and files. SIPs are responsible for enabling API functions to create, retrieve, calculate, and verify signatures. Unique SIPs exist for most file formats (Executable, PowerShell, Installer, etc., with catalog signing providing a catch-all) and are identified by globally unique identifiers (GUIDs).

Similar to Code Signing, adversaries may abuse this architecture to subvert trust controls and bypass security policies that allow only legitimately signed code to execute on a system. Adversaries may hijack SIP and trust provider components to mislead operating system and whitelisting tools to classify malicious (or any) code as signed
</blockquote>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised, and that regular users do not manually add keys to the specific cryptographic registries. Any attempts to do so are considered attempts by attackers to gain persistance. 

# Execution
The Atomic-Red-Team T1089 module describes the test for this technique (https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1089/T1089.md)

<b>Test 1 - Adding keys to the registry 1</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/SIP%20and%20Trust%20Provider%20Hijacking%20-%20T1198/Screenshots/Reg1.PNG">
</p>

<b>Test 2 - Adding keys to the registry 2</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/SIP%20and%20Trust%20Provider%20Hijacking%20-%20T1198/Screenshots/Reg2.PNG">
</p>

<b>Test 3 - Adding keys to the registry 3</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/SIP%20and%20Trust%20Provider%20Hijacking%20-%20T1198/Screenshots/Reg3.PNG">
</p>

<b>Test 4 - Adding keys to the registry 4</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/SIP%20and%20Trust%20Provider%20Hijacking%20-%20T1198/Screenshots/Reg4.PNG">
</p>

# Detection
Detection is done by monitoring processes and command line arguments. we look for the addition or deletion of keys to the specified regisrties (Sysmon Event ID 12)

## Splunk Filter
The following splunk query will allow us to detect these techniques

<b>Filter 1 - Splunk filter to detect registry changes 1</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/SIP%20and%20Trust%20Provider%20Hijacking%20-%20T1198/Screenshots/Splunk-Reg1.PNG">
</p>

<b>Filter 2 - Splunk filter to detect registry changes 2</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/SIP%20and%20Trust%20Provider%20Hijacking%20-%20T1198/Screenshots/Splunk-Reg2.PNG">
</p>

<b>Filter 3 - Splunk filter to detect registry changes 3</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/SIP%20and%20Trust%20Provider%20Hijacking%20-%20T1198/Screenshots/Splunk-Reg3.PNG">
</p>

<b>Filter 4 - Splunk filter to detect registry changes 4</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/SIP%20and%20Trust%20Provider%20Hijacking%20-%20T1198/Screenshots/Splunk-Reg4.PNG">
</p>



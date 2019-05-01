# Technique Description

## T1053 - Pass the Hash
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1075/)
<blockquote>
Pass the hash (PtH) is a method of authenticating as a user without having access to the user's cleartext password. This method bypasses standard authentication steps that require a cleartext password, moving directly into the portion of the authentication that uses the password hash. In this technique, valid password hashes for the account being used are captured using a Credential Access technique. Captured hashes are used with PtH to authenticate as that user. Once authenticated, PtH may be used to perform actions on local or remote systems.
</blockquote>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised. and the attacker has access to user memory.

# [Execution](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1075/T1075.md)
<br/>

## Atomic Test #1 - Mimikatz Pass the Hash
Note: must dump hashes first
[Reference](https://github.com/gentilkiwi/mimikatz/wiki/module-~-sekurlsa#pth)

**Supported Platforms:** Windows


#### Inputs
| Name | Description | Type | Default Value | 
|------|-------------|------|---------------|
| user_name | username | string | Administrator|
| domain | domain | string | atomic.local|
| ntlm | ntlm hash | string | cc36cf7a8514893efccd3324464tkg1a|

#### Run it with `command_prompt`!
```
mimikatz # sekurlsa::pth /user:#{user_name} /domain:#{domain} /ntlm:#{ntlm}
```
<br/>

<b>Mimikatz Pass the Hash</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Lateral-Movement/Pass-the-Hash-T1075/passthehass/Windows7_Victim-2019-04-07-20-43-33.png">
</p>

# [Detection](https://attack.mitre.org/techniques/T1053/)
<blockquote>
Audit all logon and credential use events and review for discrepancies. Unusual remote logins that correlate with other suspicious activity (such as writing and executing binaries) may indicate malicious activity. NTLM LogonType 3 authentications that are not associated to a domain login and are not anonymous logins are suspicious.
</blockquote>

it is hard to detect in our small environment, so on splunk we just looked for the process that was running mimikatz.

## Visibility 

## Splunk Filter
The following splunk query will allow us to detect these techniques

<b>the mimikatz process</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Lateral-Movement/Pass-the-Hash-T1075/passthehass/Windows%20Server%202012-2019-04-07-21-30-54.png">
</p>

<b>the mimikatz is the parent-process for the cmd process that is spawns</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Lateral-Movement/Pass-the-Hash-T1075/passthehass/Windows%20Server%202012-2019-04-07-21-37-55.png">
</p>

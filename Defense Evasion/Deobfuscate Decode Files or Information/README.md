# Technique Description

## T1140 -  Deobfuscate/Decode Files or Information 
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1129/)
<blockquote>
Adversaries may use Obfuscated Files or Information to hide artifacts of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending on how they intend to use it. Methods for doing that include built-in functionality of malware, Scripting, PowerShell, or by using utilities present on the system.

One such example is use of certutil to decode a remote access tool portable executable file that has been hidden inside a certificate file. [1]
</blockquote>

# Assumption
The assumption we took is that the end point here sits in a corporate environment where the "certutil" utility is not used by the end user. Therefore any use of the tool is an attempt to hide artifacts by a adversary already on the network or an insider threat.

# Execution
The Atomic-Red-Team T1140 module describes the test for this technique (https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.md)

# Detection

## Visibility
Detection is done by monitoring process and command line for the malicious behavior mentioned in the assumption section for the “certutil” utility. Using the “-encode” and the “-decode” options with this utility indicate malicious behavior. 
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/DeobfuscateDecode%20Files%20or%20Information-T1140/Screenshots/1.png">
</p>

## Splunk Filter
The following splunk query will allow us to detect this technique: host=SPLUNKFWD "C:\\Windows\\System32\\certutil"
<p>
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Defense-Evasion/DeobfuscateDecode%20Files%20or%20Information-T1140/Screenshots/2.png">
</p>

# Technique Description

## T1022 - Data Encrypted
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1022/)
<blockquote>
Data is encrypted before being exfiltrated in order to hide the information that is being exfiltrated from detection or to make the exfiltration less conspicuous upon inspection by a defender. The encryption is performed by a utility, programming library, or custom algorithm on the data itself and is considered separate from any encryption performed by the command and control or file transfer protocol. Common file archive formats that can encrypt files are RAR and zip.

Other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration Over Command and Control Channel and Exfiltration Over Alternative Protocol
</blockquote>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised, and that any encryption or compressing tools that were used were by an attacker looking to secretly exfiltrate this data.

# Execution
The Atomic-Red-Team T1089 module describes the test for this technique (https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1022/T1022.md)

<b>Test 1 - Locking the file with winrar:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Exfiltration/Data%20Encrypted%20-%20T1022/Screenshots/WinRar.PNG">
</p>

<b>Test 2 - Locking the file with winzip:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Exfiltration/Data%20Encrypted%20-%20T1022/Screenshots/Winzip.PNG">
</p>

<b>Test 3 - Locking the file with 7zip:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Exfiltration/Data%20Encrypted%20-%20T1022/Screenshots/7zip.PNG">
</p>

<b>Test 4 - Encrypting the file with Cipher:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Exfiltration/Data%20Encrypted%20-%20T1022/Screenshots/Cipher.PNG">
</p>

# Detection
Detection is done by monitoring processes and command line arguments. we look for tools such as winrar, winzip, 7zip and cipher which could be used to encrypt, compress and lock files.

## Splunk Filter
The following splunk query will allow us to detect these techniques

<b>Filter 1 - Splunk filter to detect winrar:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Exfiltration/Data%20Encrypted%20-%20T1022/Screenshots/Splunk-Winrar.PNG">
</p>

<b>Filter 2 - Splunk filter to detect winzip:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Exfiltration/Data%20Encrypted%20-%20T1022/Screenshots/Splunk-winzip.PNG">
</p>

<b>Filter 3 - Splunk filter to detect 7zip:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Exfiltration/Data%20Encrypted%20-%20T1022/Screenshots/7zip-Splunk.PNG">
</p>

<b>Filter 4 - Splunk filter to detect Cipher:</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Exfiltration/Data%20Encrypted%20-%20T1022/Screenshots/Cipher-Splunk.PNG">
</p>


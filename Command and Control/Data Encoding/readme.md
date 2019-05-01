# Technique Description

## T1132 - Data Encoding
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1132/)

<blockquote>
"Command and control (C2) information is encoded using a standard data encoding system. Use of data encoding may be to adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64, MIME, UTF-8, or other binary-to-text and character encoding systems. [1] [2] Some data encoding systems may also result in data compression, such as gzip."
</blockquote>

# Assumption



# Execution

 

# [Detection](https://attack.mitre.org/techniques/T1132/)
<blockquote>
"Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used."
"
</blockquote>

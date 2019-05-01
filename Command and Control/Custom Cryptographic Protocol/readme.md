# Technique Description

## T1024 - Custom Cryptographic Protocol
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1024/)

<blockquote>
"Adversaries may use a custom cryptographic protocol or algorithm to hide command and control traffic. A simple scheme, such as XOR-ing the plaintext with a fixed key, will produce a very weak ciphertext.

Custom encryption schemes may vary in sophistication. Analysis and reverse engineering of malware samples may be enough to discover the algorithm and encryption key used.

Some adversaries may also attempt to implement their own version of a well-known cryptographic algorithm instead of using a known implementation library, which may lead to unintentional errors."
</blockquote>

# Assumption



# Execution

 

# [Detection](https://attack.mitre.org/techniques/T1024/)
<blockquote>
"If malware uses custom encryption with symmetric keys, it may be possible to obtain the algorithm and key from samples and use them to decode network traffic to detect malware communications signatures.

In general, analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect when communications do not follow the expected protocol behavior for the port that is being used.
"
</blockquote>



# Web Service

# Technique Description

ID: T1102

Tactic: Command and Control, Defense Evasion

Description:
The Web Service technique is used by many threat groups and esentially is the process of utilizing online web services such as dropbox, Google Drive, Microsoft one drive to upload malicious files or scripts and then use the public link to download and execute the scripts or malicious programs from the web service. This is not only limited to file storage servicews but also other web services such as Google Calendar, Google Sheets, Google App Scripts, Pastebin, and more. 

# Assumptions

Permissions Required: User

Data Sources: Host network interface, Netflow/Enclave netflow, Network protocol analysis, Packet capture, SSL/TLS inspection

# Execution
Not applicable as web services such as dropbox or google drive are used for this technique.

# Detection

A technique that can be used to detect the usage of online Web Services after a malicious event or attack would be to use Wireshark to analyze the raw packets that are going through the network. You can then pinpoint what link was used and what file was downloaded to detemrine if it is malicious or not. 

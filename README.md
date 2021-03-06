# Compiled DPI911-Project

## Coruse Outline
Despite best efforts, evolving computer threats mean that network defenses are frequently penetrated and security incidents have become a regular occurrence in our I.T. infrastructures. It is accepted that it is a matter of when, rather than if, an incident will occur. This course covers various aspects of computer incident response. Topics include incident response preparedness, incident detection and characterization, data collection, data analysis and remediation.<sup>[1](https://apps.senecacollege.ca/ssos/findOutline.do?subjectCode=DPI911)</sup>
  
The course exposes you to various tools used in incident response industry such as: 
- OsQuery
- Splunk
- Volatility
- Redline
- Sysmon

### Learning Outcomes
Upon successful completion of this subject the student will be able to:<sup>[1](https://apps.senecacollege.ca/ssos/findOutline.do?subjectCode=DPI911)</sup>
- Explain the steps required to create incident response processes for security breaches in information systems  
- Assemble and analyze data from a security incident to determine the nature and scope of the incident to formulate and execute remediation plans  
- Create a plan for containment, eradication and improved controls to alleviate harm incurred by a security incident  
- Implement containment, eradication and improved controls to resume normal system operation after a security incident  
- Develop strategic recommendations from incident analysis which will initiate change in security policy

### Professor
Mohammad Reza Faghani, PhD

### Disclaimer
This project is not intended for production use. It was created to demonstrate potential solutions for the detection and alerting of adversary tactics and techniques related to the [MITRE ATT&CK™](https://attack.mitre.org/).

## Tactics and Techniques
### Initial Access
- [x] [Exploit Public-Facing Application](Initial%20Access/Exploit%20Public-Facing%20Application/README.md)
- [x] [Hardware Additions](Initial%20Access/Hardware%20Additions/README.md)
- [x] [Replication Through Removable Media](Initial%20Access/Replication%20Through%20Removable%20Media/README.md)
- [x] [Supply Chain Compromise](Initial%20Access/Supply%20Chain%20Compromise/Supply%20Chain%20Compromise.md)
- [ ] [Spearphishing Link](Initial%20Access/Spearphishing%20Link/README.md)

### Execution
- [x] [Control Panel Items](Execution/Control%20Panel%20Items/README.md)
- [x] [Dynamic Data Exchange](Execution/Dynamic%20Data%20Exchange/README.md)
- [ ] [Execution through API](Execution/Execution%20through%20API/README.md)
- [ ] [Execution through Module Load](Execution/Execution%20through%20Module%20Load/README.md)
- [ ] [Exploitation for Client Execution](Execution/Exploitation%20for%20Client%20Execution/T1203.md)
- [ ] [Graphical User Interface](Execution/Graphical%20User%20Interface/Readme.md)
- [x] [InstallUtil](Execution/InstallUtil/README.md)
- [x] [LSASS Driver](Execution/LSASS%20Driver/README.md)
- [x] [Mshta](Execution/Mshta/README.md)
- [x] [PowerShell](Execution/PowerShell/README.md)
- [x] [Regsvcs-Regasm](Execution/Regsvcs-Regasm/README.md)
- [x] [Rundll32](Execution/Rundll32/README.md)
- [x] [Scripting](Execution/Scripting/README.md)
- [x] [Scheduled Task](Execution/Scheduled%20Task/README.md)
- [x] [Service Execution](Execution/Service%20Execution/Service%20Execution.md)
- [x] [Signed Binary Proxy Execution](Execution/Signed%20Binary%20Proxy%20Execution/T1218%20-%20Signed%20Binary%20Proxy%20Execution.md)
- [x] [Signed Script Proxy Execution](Execution/Signed%20Script%20Proxy%20Execution/T1216%20-%20Signed%20Script%20Proxy%20Execution.md)
- [x] [Third-Party Software](Execution/Third-Party%20Software/Third-Party%20Software%20-%20Execution.md)


### Persistence
- [x] [AppInit DLLs](Persistence/AppInit%20DLLs/README.md)
- [x] [Application Shimming](Persistence/Application%20Shimming/README.md)
- [ ] [Authentication Package](Persistence/Authentication%20Package/README.md)
- [x] [BITS Jobs](Persistence/BITS%20Jobs/README.md)
- [x] [Browser Extensions](Persistence/Browser%20Extensions/Browser%20Extensions%20-%20Persistence.md)
- [x] [Change Default File Association](Persistence/Change%20Default%20File%20Association/Change%20Default%20File%20Association.md)
- [x] [Create Account](Persistence/Create%20Account/T1136%20-%20Create%20Account.md)
- [x] [DLL Search Order Hijacking](Persistence/DLL%20Search%20Order%20Hijacking/T1038%20-%20DLL%20Search%20Order%20Hijacking.md)
- [ ] [External Remote Services](Persistence/External%20Remote%20Services/T1133%20-%20External%20Remote%20Services.md)
- [ ] [File System Permissions Weakness](Persistence/File%20System%20Permissions%20Weakness/T1044%20-%20File%20System%20Permissions%20Weakness.md)
- [x] [Hidden Files and Directories](Persistence/Hidden%20Files%20and%20Directories/T1158%20-%20Hidden%20Files%20and%20Directories.md)
- [x] [Hypervisor](Persistence/Hypervisor/README.md)
- [x] [Logon Scripts](Persistence/Logon%20Scripts/README.md)
- [x] [Modify Existing Service](Persistence/Modify%20Existing%20Service/README.md)
- [x] [Netsh Helper DLL](Persistence/Netsh%20Helper%20DLL/README.md)
- [x] [New Service](Persistence/New%20Service/README.md)
- [x] [Office Application Startup](Persistence/Office%20Application%20Startup/README.md)
- [x] [Path Interception](Persistence/Path%20Interception/README.md)
- [x] [Port Monitors](Persistence/Port%20Monitors/README.md)
- [ ] [Redundant Access](Persistence/Redundant%20Access/README.md)
- [x] [Registry Run Keys and Startup Folder](Persistence/Registry%20Run%20Keys%20and%20Startup%20Folder/README.md)
- [x] [SIP and Trust Provider Hijacking](Persistence/SIP%20and%20Trust%20Provider%20Hijacking/Readme.md)
- [x] [Scheduled Task](Persistence/Scheduled%20Task/readme.md)
- [x] [Screensaver](Persistence/Screensaver/README.md)
- [x] [Security Support Provider](Persistence/Security%20Support%20Provider/README.md)
- [x] [Service Registry Permissions Weakness](Persistence/Service%20Registry%20Permissions%20Weakness/README.md)
- [x] [Shortcut Modification](Persistence/Shortcut%20Modification/README.md)
- [ ] [System Firmware](Persistence/System%20Firmware/README.md)

### Privilege Escalation
- [x] [Exploitation for Privilege Escalation](Privilege%20Escalation/Exploitation%20for%20Privilege%20Escalation/README.md)
- [ ] [Extra Window Memory Injection](Privilege%20Escalation/Extra%20Window%20Memory%20Injection/README.md)
- [x] [File System Permissions Weakness](Privilege%20Escalation/File%20System%20Permissions%20Weakness/README.md)
- [ ] [Hooking](Privilege%20Escalation/Hooking/readme.md)
- [x] [Image File Execution Options Injection](Privilege%20Escalation/Image%20File%20Execution%20Options%20Injection/README.md)
- [x] [New Service](Privilege%20Escalation/New%20Service/README.md)
- [x] [Path Interception](Privilege%20Escalation/Path%20Interception/README.md)
- [x] [Port Monitors](Privilege%20Escalation/Port%20Monitors/README.md)
- [x] [Process Injection](Privilege%20Escalation/Process%20Injection/README.md)
- [x] [Scheduled Task](Privilege%20Escalation/Scheduled%20Task/README.md)
- [x] [Valid Accounts](Privilege%20Escalation/Valid%20Accounts/README.md)
- [x] [Web Shell](Privilege%20Escalation/Web%20Shell/Web%20Shell.md)

### Defense Evasion
- [x] [Compiled HTML File](Defense%20Evasion/Compiled%20HTML%20File/README.md)
- [ ] [Component Firmware](Defense%20Evasion/Component%20Firmware/README.md)
- [x] [Component Object Model Hijacking](Defense%20Evasion/Component%20Object%20Model%20Hijacking/README.md)
- [x] [Control Panel Items](Defense%20Evasion/Control%20Panel%20Items/README.md)
- [x] [DCShadow](Defense%20Evasion/DCShadow/README.md)
- [x] [DLL Search Order Hijacking](Defense%20Evasion/DLL%20Search%20Order%20Hijacking/README.md)
- [x] [DLL Side Loading](Defense%20Evasion/DLL%20Side%20Loading/readme.md)
- [x] [Deobfuscate Decode Files or Information](Defense%20Evasion/Deobfuscate%20Decode%20Files%20or%20Information/README.md)
- [x] [Disabling Security Tools](Defense%20Evasion/Disabling%20Security%20Tools/Readme.md)
- [ ] [Extra Window Memory Injection](Defense%20Evasion/Extra%20Window%20Memory%20Injection/README.md)
- [x] [File Deletion](Defense%20Evasion/File%20Deletion/Readme.md)
- [x] [File Permissions Modification](Defense%20Evasion/File%20Permissions%20Modification/README.md)
- [x] [File System Logical Offset](Defense%20Evasion/File%20System%20Logical%20Offset/README.md)
- [x] [Hidden Files and Directories](Defense%20Evasion/Hidden%20Files%20and%20Directories/README.md)
- [x] [Image File Execution Options Injection](Defense%20Evasion/Image%20File%20Execution%20Options%20Injection/README.md)
- [ ] [Indicator Blocking](Defense%20Evasion/Indicator%20Blocking/README.md)
- [x] [Indicator Removal from Tools](Defense%20Evasion/Indicator%20Removal%20from%20Tools/README.md)
- [x] [Indicator Removal on Host](Defense%20Evasion/Indicator%20Removal%20on%20Host/README.md)
- [x] [Indirect Command Execution](Defense%20Evasion/Indirect%20Command%20Execution/README.md)
- [x] [InstallUtil](Defense%20Evasion/InstallUtil/README.md)
- [x] [Masquerading](Defense%20Evasion/Masquerading/README.md)
- [x] [Mshta](Defense%20Evasion/Mshta/README.md)
- [x] [NTFS File Attributes](Defense%20Evasion/NTFS%20File%20Attributes/README.md)
- [x] [Network Share Connection Removal](Defense%20Evasion/Network%20Share%20Connection%20Removal/README.md)
- [ ] [Process Doppelganging](Defense%20Evasion/Process%20Doppelganging/README.md)
- [x] [Process Hollowing](Defense%20Evasion/Process%20Hollowing/README.md)
- [ ] [Obfuscated Files or Information](Defense%20Evasion/Obfuscated%20Files%20or%20Information/README.md)
- [x] [Process Injection](Defense%20Evasion/Process%20Injection/T1055%20-%20Process%20Injection.md)
- [ ] [Redundant Access](Defense%20Evasion/Redundant%20Access/T1108%20-%20Redundant%20Access.md)
- [x] [Regsvcs & Regasm](Defense%20Evasion/Regsvcs%20&%20Regasm/T1121%20-%20Regsvcs%20&%20Regasm.md)
- [x] [Regsvr32](Defense%20Evasion/Regsvr32/T1117%20-%20Regsvr32.md)
- [ ] [Rootkit](Defense%20Evasion/Rootkit/T1014%20-%20Rootkit.md)
- [x] [Rundll32](Defense%20Evasion/Rundll32/T1085%20-%20Rundll32.md)
- [x] [Scripting](Defense%20Evasion/Scripting/Scripting%20-%20Defense%20Evasion.md)

### Credential Access
- [x] [Credential Dumping](Credential%20Access/Credential%20Dumping/README.md)
- [x] [Credentials in Files](Credential%20Access/Credentials%20in%20Files/README.md)
- [x] [Credentials in Registry](Credential%20Access/Credentials%20in%20Registry/readme.md)
- [ ] [Exploitation for Credential Access](Credential%20Access/Exploitation%20for%20Credential%20Access/readme.md)
- [x] [Forced Authentication](Credential%20Access/Forced%20Authentication/README.md)
- [x] [Hooking](Credential%20Access/Hooking/README.md)
- [x] [Network Sniffing](Credential%20Access/Network%20Sniffing/README.md)
- [ ] [LLMNR/NBT-NS Poisoning](Credential%20Access/LLMNR%20NBT-NS%20Poisoning/README.md)
- [ ] [Password Filter DLL](Credential%20Access/Password%20Filter%20DLL/T1174%20-%20Password%20Filter%20DLL.md)
- [ ] [Two-Factor Authentication Interception](Credential%20Access/Two-Factor%20Authentication%20Interception/Two-Factor%20Authentication%20Interception.md)

### Discovery
- [x] [Network Service Scanning](Discovery/Network%20Service%20Scanning/Network%20Service%20Scanning.md)
- [ ] [Peripheral Device Discovery](Discovery/Peripheral%20Device%20Discovery/README.md)
- [x] [Permission Groups Discovery](Discovery/Permission%20Groups%20Discovery/README.md)
- [x] [Process Discovery](Discovery/Process%20Discovery/Readme.md)
- [x] [Query Registry](Discovery/Query%20Registry/Readme.md)
- [x] [Remote System Discovery](Discovery/Remote%20System%20Discovery/README.md)
- [x] [Security Software Discovery](Discovery/Security%20Software%20Discovery/README.md)
- [x] [System Information Discovery](Discovery/System%20Information%20Discovery/README.md)
- [x] [System Network Configuration Discovery](Discovery/System%20Network%20Configuration%20Discovery/README.md)
- [x] [System Network Connections Discovery](Discovery/System%20Network%20Connections%20Discovery/README.md)
- [x] [System Owner/User Discovery](Discovery/System%20Owner%20User%20Discovery/README.md)
- [x] [System Service Discovery](Discovery/System%20Service%20Discovery/T1007%20-%20System%20Service%20Discovery.md)
- [x] [System Time Discovery](Discovery/System%20Time%20Discovery/T1124%20-%20System%20Time%20Discovery.md)

### Lateral Movement
- [x] [Exploitation of Remote Services](Lateral%20Movement/Exploitation%20of%20Remote%20Services/README.md)
- [x] [Logon Scripts](Lateral%20Movement/Logon%20Scripts/README.md)
- [x] [Pass the Hash](Lateral%20Movement/Pass%20the%20Hash/readme.md)
- [ ] [Pass the Ticket](Lateral%20Movement/Pass%20the%20Ticket/readme.md)
- [x] [Remote Desktop Protocol](Lateral%20Movement/Remote%20Desktop%20Protocol/README.md)
- [x] [Remote File Copy](Lateral%20Movement/Remote%20File%20Copy/README.md)
- [ ] [Third-party Software](Lateral%20Movement/Third-party%20Software/T1072%20-%20Third-party%20Software.md)
- [ ] [Shared Webroot](Lateral%20Movement/Shared%20Webroot/README.md)
- [ ] [Taint Shared Content](Lateral%20Movement/Taint%20Shared%20Content/README.md)

### Collection
- [x] [Clipboard Data](Collection/Clipboard%20Data/Clipboard%20Data.md)
- [ ] [Data from Local System](Collection/Data%20from%20Local%20System/README.md)
- [x] [Data from Network Shared Drive](Collection/Data%20from%20Network%20Shared%20Drive/Readme.md)
- [x] [Input Capture](Collection/Input%20Capture/T1056%20-%20Input%20Capture.md)
- [x] [Screen Capture](Collection/Screen%20Capture/README.md)
- [ ] [Email Collection](Collection/Email%20Collection/README.md)

### Exfiltration
- [x] [Data Compressed](Exfiltration/Data%20Compressed/README.md)
- [x] [Data Encrypted](Exfiltration/Data%20Encrypted/Readme.md)
- [x] [Data Transfer Size Limits](Exfiltration/Data%20Transfer%20Size%20Limits/README.md)
- [ ] [Exfiltration Over Other Meduim](Exfiltration/Exfiltration%20Over%20Other%20Meduim/T1011%20-%20Exfiltration%20Over%20Other%20Meduim.md)
- [ ] [Exfiltration Over Command and Control Channel](Exfiltration/Exfiltration%20Over%20Command%20and%20Control%20Channel/README.md)

### Command and Control
- [x] [Connection Proxy](Command%20and%20Control/Connection%20Proxy/README.md)
- [ ] [Custom Command and Control Protocol](Command%20and%20Control/Custom%20Command%20and%20Control%20Protocol/README.md)
- [ ] [Custom Cryptographic Protocol](Command%20and%20Control/Custom%20Cryptographic%20Protocol/readme.md)
- [ ] [Data Encoding](Command%20and%20Control/Data%20Encoding/readme.md)
- [ ] [Multilayer Encryption](Command%20and%20Control/Multilayer%20Encryption/T1079%20-%20Multilayer%20Encryption.md)
- [ ] [Remote Access Tools](Command%20and%20Control/Remote%20Access%20Tools/T1219%20-%20Remote%20Access%20Tools.md)
- [ ] [Web Service](Command%20and%20Control/Web%20Service/Web%20Service%20-%20Command%20and%20Control.md)
- [ ] [Multi-hop Proxy](Command%20and%20Control/Multi-hop%20Proxy/README.md)
- [ ] [Multiband Communication](Command%20and%20Control/Multiband%20Communication/README.md)
- [x] [Uncommonly Used Port](Command%20and%20Control/Uncommonly%20Used%20Port/README.md)


## Reference

This repo is a compiled version of the following group projects for the DPI911 Winter Class of 2019.  
[kwburns](https://github.com/kwburns/DPI911-Project/)  
[ayusuf15](https://github.com/ayusuf15/DPI911SSA-Project-Group3)  
[kaegeh](https://github.com/kaegeh/DPI911-Project)  
[drjgrant](https://github.com/drjgrant/Mitre-Att-ck-Detection-with-Splunk)  
[myu31](https://github.com/myu31/dpi911/blob/master/dpi911.md)  
[ammcconnell2](https://github.com/ammcconnell2/DPI911---MITRE-ATT-CK-Project)  
[rpanchal93](https://github.com/rpanchal93/DPI911-Project)


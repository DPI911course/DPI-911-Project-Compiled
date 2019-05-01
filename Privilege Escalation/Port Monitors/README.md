# Port Monitors- T1013

## Technique Description 
Spoolsv.exe can be used to load a DLL located in System32 folder that is ran under SYSTEM permissions or by writing the pathname of the DLL to HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors. These techniques can be used to load malicious code at start-up which are persistent and will execute as SYSTEM.   
To demonstrate this technique we edit the registry of HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors. 

## Assumptions
Malicious code should be run at start-up.

## Execution
![port monitors](https://user-images.githubusercontent.com/36422282/55608850-531cb780-574d-11e9-840c-4c3c325ccdc2.JPG)

## Detection
### Splunk Filter
Splunk Filter = host="DESKTOP-EHTEINI" source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=13

### Splunk Capture
![pm](https://user-images.githubusercontent.com/36422282/55976763-31469780-5c5b-11e9-9d25-cf0c5f1dc527.png)

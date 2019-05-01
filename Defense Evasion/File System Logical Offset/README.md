# File System Logical Offsets- T1006

## Technique Description
Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This bypasses techniques Windows file access controls as well as file system monitoring tools.   
To demonstrate this technique we are going to use Powersploit’s Invoke-ninjacopy command. 

## Assumption
NinjaCopy should be able to copy files that are specified. 

## Execution
![file system logical offsets- ninja copy](https://user-images.githubusercontent.com/36422282/55609089-ddfdb200-574d-11e9-9d6b-a8ddd27e5f6d.JPG)

## Detection
### Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

Splunk Filter = host="DESKTOP-EHTEINI" source="XmlWinEventLog:Microsoft-Windows-PowerShell/Operational" EventCode=4104 "invoke-ninjacopy"

### Splunk Capture
![ninjacopy](https://user-images.githubusercontent.com/36422282/55975220-7c5eab80-5c57-11e9-9bdc-41179663cade.png)


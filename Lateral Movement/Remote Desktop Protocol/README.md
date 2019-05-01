# Remote Desktop Protocol- T1076

## Technique Description
Adversaries my connect to a device which has RDP/RDS using accounts that they have credentials for to so they can expand their access.  
Adversaries can perform session hijacking using tscon.exe without any need of credentials or prompts to the user. Typically the user would be notified if someone tried to steal the session ut using this, the user will not be notified. This can be done locally or remotely and with active or disconnected sessions.  
To demonstrate this technique we use tscon to hijack a session.

## Assumptions
The sessions should be hijacked and the adversary should be connected via RDP

## Execution
![remote desktop protocol](https://user-images.githubusercontent.com/36422282/55610082-303fd280-5750-11e9-8960-b7a61c092f3d.JPG)

## Detection
### Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

Splunk Filter = host="DESKTOP-EHTEINI" source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" ParentCommandLine="cmd.exe /k *" OR ParentCommandLine="cmd.exe /c *" tscon.exe 

### Splunk Capture
![rdp](https://user-images.githubusercontent.com/36422282/55976747-25f36c00-5c5b-11e9-94de-268119876eab.png)

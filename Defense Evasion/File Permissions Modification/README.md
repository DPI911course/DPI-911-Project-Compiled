
# File Permissions Modification - T1222

## Technique Description

Attackers change file permissions to enable malicious activity using those files.

To demonstrate this technique, we are going to use Cacls to try to modify permissions for a DLL file in Windows/System32. Access was denied, but the event should still be logged.

## Assumptions

Attacker had used the cacls command on a compromised host, which forwards events to Splunk. The execution of this command should be captured in Splunk.

## Execution

![File Permissions Modification 1](https://user-images.githubusercontent.com/36422282/55605146-2498df80-5741-11e9-8de8-4451edfe8794.PNG)

We can see the event in Event Viewer, Windows Security Log:
![File Permissions Modification 2](https://user-images.githubusercontent.com/36422282/55605152-2f537480-5741-11e9-8196-dd38b23ae189.PNG)

## Detection

### Splunk Filter

To detect this technique, we should monitor Windows Security Log for event ID 4670 (permissions on an object were changed/attempted to be changed)

NOTE: This filter is specific and relates to the specific attack technique itself.

### Splunk Capture

host="AGENT-2" source="WinEventLog:Security" EventCode=4670
![File Permissions Modification](https://user-images.githubusercontent.com/36422282/55605117-092dd480-5741-11e9-9b61-ad92717f760e.png)

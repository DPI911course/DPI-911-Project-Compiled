# Image Indicator Removal from Tools - T1066

## Technique Description

Attackers remove indicators (signatures) from their tools in order to evade detection by anti-viruses or other detection software. 
To demonstrate this technique, we ran PowerSploit's Find-AVSignature module. This module searches through file contents and locates single-byte AV signatures inside it.

## Assumptions

Attacker had used the Find-AVSignature powershell command on a compromised host, which forwards events to Splunk. The execution of this command should be captured in Splunk.

## Execution

![Indicator Removal from Tools](https://user-images.githubusercontent.com/36422282/55608999-a7c03280-574d-11e9-84fe-02ebae0198a3.PNG)

## Detection

### Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

To detect the technique we demonstrated, we should monitor Microsoft-Windows-PowerShell/Operational Event ID 4104 (command executed) events that contain the "Find-AVSignature" string, which would indicate execution of the PowerSploit module with the same name.

host="AGENT-2" source="WinEventLog:Microsoft-Windows-PowerShell/Operational" EventCode="4104" "Find-AVSignature"

### Splunk Capture

![Indicator Removal from Tools - 2](https://user-images.githubusercontent.com/36422282/55609040-be668980-574d-11e9-8900-ce8f7877331b.png)

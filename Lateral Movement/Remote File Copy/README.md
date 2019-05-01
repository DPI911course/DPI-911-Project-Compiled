
# Remote File Copy - T1105

## Technique Description

Attackers will very likely attempt to enumerate security software, such as firewalls, anti-viruses or IDS software, installed on the system.

To demonstrate this technique, specifically using the certutil command, we are going to use this command to pull a file from the web (Atomic Test #7).

## Assumptions

Attacker had used the certutil command to pull a file from the web to the compromised host, the execution of this command had been logged and forwarded to Splunk.


## Execution

![Remote File Copy](https://user-images.githubusercontent.com/36422282/55614179-7437d500-575a-11e9-92e6-325f7c800ae7.PNG)

## Detection

### Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

To detect the technique we demonstrated, we should monitor Microsoft-Windows-Sysmon/Operational for certutil commands that have a URL as an argument.

host="AGENT-2" source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" CommandLine="certutil* http*"

### Splunk Capture

![Remote File Copy](https://user-images.githubusercontent.com/36422282/55614168-70a44e00-575a-11e9-9c9e-d3c81743b74f.png)

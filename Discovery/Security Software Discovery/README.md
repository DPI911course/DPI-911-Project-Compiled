
# Security Software Discovery - T1063

## Technique Description

Attackers will very likely attempt to enumerate security software, such as firewalls, anti-viruses or IDS software, installed on the system.

To demonstrate this technique, specifically firewall enumeration, we are going to use the netsh advfirewall command.

## Assumptions
Attacker had used the netsh advfirewall command on a compromised host, which forwards events to Splunk. The execution of this command should be captured in Splunk.

## Execution

![Security Software Discovery](https://user-images.githubusercontent.com/36422282/55613328-7436d580-5758-11e9-90d9-a9f1a544e26c.PNG)

## Detection

### Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

To detect the technique we demonstrated, we should monitor Microsoft-Windows-Sysmon/Operational for netsh advfirewall commands.

host="AGENT-2" source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" CommandLine="netsh* advfirewall*"

### Splunk Capture

![Security Software Discovery](https://user-images.githubusercontent.com/36422282/55613457-bcee8e80-5758-11e9-9e31-a60fe7db5095.png)

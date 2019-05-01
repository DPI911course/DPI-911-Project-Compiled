
# Remote System Discovery - T1018

## Technique Description

Attackers will very likely attempt to conduct reconnaisance and get a listing of other systems on the network for lateral movement or pivoting.

To demonstrate this technique, we are going to use the net view command.

## Assumptions
Attacker had used the net view command on a compromised host, which forwards events to Splunk. The execution of this command should be captured in Splunk.

## Execution

![Remote System Discovery](https://user-images.githubusercontent.com/36422282/55612770-0342ee00-5757-11e9-9f07-3088c12ae069.PNG)

## Detection

### Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

To detect the technique we demonstrated, we should monitor Microsoft-Windows-Sysmon/Operational for net view commands.

host="AGENT-2" source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" CommandLine="net* view*"

### Splunk Capture

![Remote System Discovery](https://user-images.githubusercontent.com/36422282/55612957-78162800-5757-11e9-840c-af131d9dbf44.png)

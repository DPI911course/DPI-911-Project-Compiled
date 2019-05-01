
# Hidden Files and Directories - T1158

## Technique Description

Attackers make files and directories they use hidden in order to evade accidental detection by the user of the compromised machine.

To demonstrate this technique, we are going to use the Attrib command to make a simple text file hidden.

## Assumptions

Attacker had used the attrib command on a compromised host, which forwards events to Splunk. The execution of this command should be captured in Splunk.

## Execution

![Hidden Files and Directories](https://user-images.githubusercontent.com/36422282/55605827-434ca580-5744-11e9-9764-f76fb3ccf1e9.PNG)

## Detection

### Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

To detect the technique we demonstrated, we should monitor Microsoft-Windows-Sysmon/Operational for attrib commands with the +h flag set.

host="DESKTOP-H25LQ8L" source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" CommandLine="attrib*+h*"

### Splunk Capture

![Hidden Files and Directories](https://user-images.githubusercontent.com/36422282/55605835-4f386780-5744-11e9-8f06-97292b3fdcc8.png)

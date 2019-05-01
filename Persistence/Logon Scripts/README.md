
## Technique Description

Windows allows logon scripts to be run whenever a specific user or group of users log into a system. [1] The scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server.

If adversaries can access these scripts, they may insert additional code into the logon script to execute their tools when a user logs in. This code can allow them to maintain persistence on a single system, if it is a local script, or to move laterally within a network, if the script is stored on a central server and pushed to many systems. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary.


## Execution (test script used)

**Potential Attacks:** ```REG.exe ADD HKCU\Environment /v UserInitMprLogonScript /t REG_MULTI_SZ /d “cmd.exe /c calc.exe”```

![](../images/T1037_Execute.PNG)


## Detection -- Visibility -- Filter/ Correlation Rule

**Filter:** ```(source="wineventlog:microsoft-windows-sysmon/operational" OR cmd.exe OR powershell.exe ) AND ("reg.exe" ADD HKCU\\Environment /v UserInitMprLogonScript"") ```

An attacker can use cmd or powershell to use regedit/reg.exe to add a LogonScript under the HKCU\\Environment key. 

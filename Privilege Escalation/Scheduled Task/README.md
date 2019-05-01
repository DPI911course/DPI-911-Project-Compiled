## Technique Description

Utilities such as at and schtasks, along with the Windows Task Scheduler, can be used to schedule programs or scripts to be executed at a date and time. A task can also be scheduled on a remote system, provided the proper authentication is met to use RPC and file and printer sharing is turned on. Scheduling a task on a remote system typically required being a member of the Administrators group on the the remote system. 

An adversary may use task scheduling to execute programs at system startup or on a scheduled basis for persistence, to conduct remote Execution as part of Lateral Movement, to gain SYSTEM privileges, or to run a process under the context of a specified account.


## Execution (test script used)

**Potential Attacks:** ```SCHTASKS /Create /SC ONCE /TN spawn /TR C:\windows\system32\cmd.exe /ST 12:00```

![](../images/T1053_Execute.PNG)


## Detection -- Visibility -- Filter/ Correlation Rule

**Filter:** ```("cmd.exe" OR "powershell.exe" OR source="wineventlog:microsoft-windows-sysmon/operational" ) AND (“SCHTASKS /Create /SC ONCE /TN spawn /TR)```

The attacker can use the SCHTASKS command to schedule a task at system start up. This command can be exectued in both cmd or powershell. 


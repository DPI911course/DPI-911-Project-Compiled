Technique Description: Scheduled Task (T1053)
------------------------------------
Scheduled tasks are used so that programs or scripts can be executed at a specific date and/or time. It allows users to set a time or date for the program or script to run automatically. An attacker could use scheduled task to execute program/scripts or can be used to keep persistence in the system.

Assumptions 
-------------
We assume that the attacker already has access to the system to launch a command prompt. 

Execution 
-------------
SCHTASKS /Create /SC ONCE /TN spawn /TR “C:\windows\system32\cmd.exe” /ST 11:20:00

 Detection 
-------------
Monitor for scheduled task creating used by common utilities that use command line. Should also monitor for process execution by svchost.exe and taskend.exe. Also monitor %systemroot%\System32\Tasks for any changes or being removed. Using sysinternals autoruns can help detect and scheduled tasks that are used for persistence. Monitor for procesess and command line for creation of scheduled tasks.
https://attack.mitre.org/techniques/T1053/

Visibility 
-------------

### Filter/ Correlation Rule ###
EventCode=4698 OR EventCode=4699 OR EventCode=4700 OR EventCode=4701 OR EventCode=4702
![sch](https://user-images.githubusercontent.com/32250546/55593349-702f9700-5709-11e9-8ecd-f40e0b8d0ccf.png)

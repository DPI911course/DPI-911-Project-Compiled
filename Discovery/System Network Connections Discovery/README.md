Technique Description: System Network Connections Discovery (T1049)
------------------------------------
The attacker attempts to get all the network connections to or from the victims system that they are accessing.  

Assumptions 
-------------

Execution 
-------------
In CMD line:
netstat
Net use
sessions

 Detection 
-------------
Monitor for process and command line for any arguments that can be used to gather system or network information.

 Visibility 
-------------

### Filter/ Correlation Rule ###
EventID=1 AND cmdline="netstat" OR cmdline="net use" OR cmdline="sessions"

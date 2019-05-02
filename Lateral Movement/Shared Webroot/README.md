Technique Description: Shared Webroot (T1051)
------------------------------------
Attackers may use the webroot of a website to set the webroot as their payload to infect machines. This is used to laterally move within the network and infect other machines.

Assumptions 
-------------
N/A

Execution 
-------------
Not feasible

 Detection 
-------------
monitor file and process to find files that are written to Web server by a process that isnt normal. process monitor to find normal processes that are on the Wev server and find process that are not.

 Visibility 
-------------

### Filter/ Correlation Rule ###

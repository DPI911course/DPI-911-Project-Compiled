Technique Description: Scripting (T1064)
------------------------------------
Technical Description: Attackers can use scripts to assist and create actions that could possibly done manually. Scripting allows for the attacks to be run faster which enables them to be able to gain access to the victim faster. Scripting can also bypass process monitoring devices by working with the operating system at the API level [2]. 

Assumptions 
-------------
We assume that, malicious code has been injected through Spearphishing link as its initial access into the end point.

Execution (test script used) 
-------------
From cmd line: .\testscript.ps1

 Detection 
-------------
Scripting is more likely to perform by admin, developer, or power user systems. Running script for an non-authorized person or end point is highly suspicious. Monitoring processes and arguments for scrip execution is highly recommended [2].

 Visibility 
-------------
A powershell script run

### Filter/ Correlation Rule ###

![scripting](https://user-images.githubusercontent.com/32250546/55583929-0c996f80-56f1-11e9-9ae8-7acb09cccf3d.png)

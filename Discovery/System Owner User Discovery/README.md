Technique Description:	System Owner/User Discovery (T1033)
------------------------------------
Attacker attempts to find the primary users, logged in users, set of users that use system, or if user is actively on the system. The information are collected in many ways with Discovery techniques.  

Assumptions 
-------------
We assume the attacker has gotten access to a machine with an exploit which they then use to collect information about system users. 

Execution 
-------------
From cmd line:
cmd.exe /C whoami
wmic useraccount get /ALL
quser /SERVER:"#{computer_name}"
quser
qwinsta.exe" /server:#{computer_name}
qwinsta.exe
for /F "tokens=1,2" %i in ('qwinsta /server:#{computer_name} ^| findstr "Active Disc"') do @echo %i | find /v "#" | find /v "console" || echo %j > usernames.txt
@FOR /F %n in (computers.txt) DO @FOR /F "tokens=1,2" %i in ('qwinsta /server:%n ^| findstr "Active Disc"') do @echo %i | find /v "#" | find /v "console" || echo %j > usernames.txt

Detection 
-------------
Monitor for process and command line for any arguments that can be used to gather system or network information.
 
 Visibility 
-------------

### Filter/ Correlation Rule ###
(EventCode=4658 OR EventCode=4656 OR EventCode=4648) AND (Quser.exe OR Qwinsta.exe OR wmic.exe)
![owner](https://user-images.githubusercontent.com/32250546/55592388-46c13c00-5706-11e9-91c3-3975e54ff268.png)

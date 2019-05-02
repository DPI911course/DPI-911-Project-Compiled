Technique Description: Valid Accounts (T1078)
------------------------------------
Attackers can use valid accounts to steal credentials of specific useror service accounts by using social engineering process. They can also use those accounts to keep persistence within the victims system.

Assumptions 
-------------
We assume that the attacker has socially engineeered an employee to get their credentials and then uses them to create other valid accounts.

Execution
-------------
net user /add hacker p@ssw0rd!2d
 Detection 
-------------
Monitor for suspicious account activities within the network and perform audits of the domain and local system accounts to find accounts that could be created and used by attacker for persistence

 Visibility 
-------------

### Filter/ Correlation Rule ###

EventCode=4720 OR EventCode=4738 OR EventCode=4722
![vaild](https://user-images.githubusercontent.com/32250546/55599264-e1307800-5724-11e9-9aeb-2ebd28ec64bc.png)

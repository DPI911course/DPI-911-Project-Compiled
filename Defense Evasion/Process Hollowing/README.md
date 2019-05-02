Technique Description:	Process Hollowing (T1093)
------------------------------------
This happens when there is a process being created during a suspended state where the memory is unmapped and replaced. 

Assumptions 
-------------
We assume that there is a suspeneded process and that the attacker has already gained access to the system.

Execution 
-------------
Osquery:
select DISTINCT p.name, p.path, pos.remote_address, pos.remote_port from process_open_sockets pos LEFT JOIN processes p ON pos.pid = p.pid WHERE pos.remote_port != 0 AND p.name != '';

 Detection 
-------------
Monitor API calls that create large amount of data and monitor process behaviour to see if process is performing actions.

 Visibility 
-------------
![processhollowing](https://user-images.githubusercontent.com/32250546/55599369-63b93780-5725-11e9-8400-5d23830b1b41.png)

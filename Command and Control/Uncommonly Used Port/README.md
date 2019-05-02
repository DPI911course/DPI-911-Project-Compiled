Technique Description: Uncommonly Used Port (T1065)
------------------------------------
Attackers may use uncommon ports to bypass firewalls or other access controls to establish their C2 channel.

Assumptions 
-------------
We assume that the attacker has access to the system already and is using an uncommon port from within to reach out to C2.

Execution 
-------------
test-netconnection -ComputerName #{google.com} -port #{8081}

![uncommon](https://user-images.githubusercontent.com/32250546/55599520-3b7e0880-5726-11e9-9dc0-0c1ce25b76cb.png)
 
 Detection 
-------------
Analyze network data flows for odd ammounts of data flowing on ports that are not commonly used.

 Visibility 
-------------

### Filter/ Correlation Rule ###
![uncommon2](https://user-images.githubusercontent.com/32250546/55599525-446eda00-5726-11e9-8f86-856b70027116.png)

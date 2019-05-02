Technique Description: Network Sniffing (T1040)
------------------------------------
Network sniffing is to monitor or capture information that is going through the wired or wireless connection. The attacker may put a network interface in promiscuous mode so that they can access data when the data is in transit over network. 

Assumptions 
-------------
We assume the attacker already has Administrator privilleges otherwise most OS's do not allow interface capturing/sniffing.

Execution 
-------------
From cmd line:  c:\Program Files\Wireshark\tshark.exe -i #{interface} -c 5c:\windump.exe

 Detection 
-------------
Looking for events that may lead to network sniffing traffic such as traffic from one source IP to multiple ports within a timeframe. Monitor ARP spoofing and audit admin logs, changes, and device images.

 Visibility 
-------------

### Filter/ Correlation Rule ###
4646 file system or 4658 look for dumpcap.exe or tshark.exe
![network](https://user-images.githubusercontent.com/32250546/55592342-22655f80-5706-11e9-9755-c2c78652248f.png)

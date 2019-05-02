Technique Description: LLMNR/NBT-NS Poisoning (T1171)
------------------------------------
LLMNR/NBT-NS is an alternative to DNS in the sense of identity, and attackers can spoof the authoritative source of the responses to point victims to a host that is malicious.

Assumptions 
-------------

Execution 
-------------


 Detection 
-------------
Use LLMNR/NBT-NS spoofing detection tool and monitor data going through UDP ports 5355 and 137. Also monitor for chanes n the DWORD value in HKLM\Software\Policies\Microsoft\Windows NT\DNSClient registry.

 Visibility 
-------------
(try responder)

### Filter/ Correlation Rule ###

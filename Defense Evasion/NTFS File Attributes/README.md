Technique Description: NTFS File Attributes (T1096)
------------------------------------
Adversaries can store payloads in NTFS alternate data streams to avoid detection and then can run the payload using a number of different ways. 

Assumptions 
-------------
We assume that the attacker already has access to the system and can use an already existing file's alternate data stream.

Execution
-------------
From CMD line:
![cmd](https://user-images.githubusercontent.com/32250546/55584579-82520b00-56f2-11e9-8a56-ce758844268a.png)

 Detection 
-------------
Using forensic tools to identify information about NTFS attributes.

Visibility 
-------------

### Filter/ Correlation Rule ###
EventCode=1 AND *:payload.exe    ---> ideally a filter for ":" would find all instances of this attack, however Splunk cannot filter for this character on its own.
![payload](https://user-images.githubusercontent.com/32250546/55584649-b5949a00-56f2-11e9-82d7-5cd27e08b4c4.png)

Technique Description: Application Shimming (T1138)
------------------------------------
The Microsoft Windows Application Compatibility Infrastructure/Framework (Application Shim) is used to allow for backward compatibility for software. Once it is executed, a shim cache is used to find if the program needs to use the shim database .sdb. If it is needed then the shim database uses a hook to redirect code so that the software can communicate with the operating system.

Assumptions 
-------------
We assume that the attacker already has access to the system.

Execution
-------------
From cmd line:  sdbinst.exe AtomicShimx86.sdb
![cmd](https://user-images.githubusercontent.com/32250546/55592444-753f1700-5706-11e9-961e-3d3f0a10abad.png)

 Detection 
-------------
Use public tools to detect application shimming, some tools are Shim-Process-Scanner, Shim-Detector-Lite, Shim-Guard, ShimScanner, and ShimCacheMem.
 
 Visibility 
-------------

### Filter/ Correlation Rule ###
EventCode=4688 AND sdbinst.exe
![app](https://user-images.githubusercontent.com/32250546/55592461-7c662500-5706-11e9-8c7d-b2b266fe0ef6.png)

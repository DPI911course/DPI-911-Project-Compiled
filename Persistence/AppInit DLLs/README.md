Technique Description: AppInit DLLS (T1103)
------------------------------------
DLLS specified in AppInit DLL values which are in the registry keys. The keys are run by user32.dll. 

Assumptions 
-------------
We assume, after initial access through Spearphishing link a malware is running script to make malware persistent through Applnit DLLs technique. 

Execution 
-------------
From cmd line: reg import handler.reg

 Detection 
-------------
Monitoring DDL that are loaded by user32.dll and looking for abnormal DLLs that are loaded into process. We can also monitor AppInit_DLLs registry for any changes that aren’t correlated with software [3].

 Visibility 
-------------
Regmon.exe

### Filter/ Correlation Rule ###

EventCode=4688 OR EventCode=1 AND reg.exe
![appinit DLLS](https://user-images.githubusercontent.com/32250546/55584086-71ed6080-56f1-11e9-9908-17df1f321070.png)

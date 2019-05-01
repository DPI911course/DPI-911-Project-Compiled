## Technique Description

This occurs when a payload or any malicious file is modified so that its location or name seems legitimate. Its success is due to tools trusting certain filepaths or filenames as non-malicious entities. An example of this is storing a malicious file within a directory that is considered a trusted resource. In Windows machines the ```C:\Windows\System32``` is a trusted location, while in Linux the ```/bin``` directory is trusted. 

## Execution (test script used)

**Potential Attacks:** ```cmd.exe /c copy %SystemRoot%\System32\cmd.exe %SystemRoot%\Temp\lsass.exe```

![](../images/T1036_Execute.PNG)

## Detection -- Visibility -- Filter/ Correlation Rule

**Filter:** ```(source="wineventlog:microsoft-windows-sysmon/operational" OR source="wineventlog:microsoft-windows-powershell/operational" OR "cmd.exe") AND cmd.exe /c copy AND NOT ("UserID='S-1-5-21domain'")```



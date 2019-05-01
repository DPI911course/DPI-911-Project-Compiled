## Technique Description

InstallUtil is a command line tool used for installations as well as uninstallation of different types of resources with the help of executing specific installer components within the .NET binaries. They can be found within the .NET directory of the windows file systems. A second use case for InstallUtil is to bypass process whitelisting while using attributes from binary which execute the class decorated with the attribute ```[System.CompnetModel.RunInstaller(true)]```


## Execution (test script used)

**Potential Attacks:** 
Attack 1: ```C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /target:library T1118.cs```

Attack 2: ```C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /U #{filename}```

![](../images/T1118_Execute.PNG)

## Detection -- Visibility -- Filter/ Correlation Rule

**Filter:** 
Filter 1: ```((source="wineventlog:microsoft-windows-powershell/operational" OR cmd.exe OR source="wineventlog:microsoft-windows-sysmon/operational" )  AND ("csc.exe  /target:library")) OR ((source="wineventlog:microsoft-windows-powershell/operational" OR cmd.exe OR source="wineventlog:microsoft-windows-powershell/operational" ) AND ("InstallUtil.exe  /logfile= /LogToConsole=false /U"))```

Filter 2: ```(source="wineventlog:microsoft-windows-powershell/operational" OR cmd.exe OR source="wineventlog:microsoft-windows-powershell/operational" ) AND ("InstallUtil.exe  /logfile= /LogToConsole=false /U")```

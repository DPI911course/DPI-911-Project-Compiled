## Technique Description
On Windows machines it is possible to execute commands without directly calling cmd.exe.

## Execution (test script used)

**Potential Attacks:** 
```pcalua.exe -a cmd.exe```
and

```forfiles /p c:\windows\system32 /m notepad.exe /c cmd.exe```

![](../images/T1202_Execute.PNG)

## Detection -- Visibility -- Filter/ Correlation Rule

**Filter:** 
```(source="wineventlog:microsoft-windows-sysmon/operational" OR source="wineventlog:microsoft-windows-powershell/operational" OR cmd.exe OR powershell.exe ) AND "pcalua.exe" -a"" ```
and 
```(source="wineventlog:microsoft-windows-sysmon/operational" OR powershell.exe OR cmd.exe) AND (forfiles /p AND /m AND /c)```

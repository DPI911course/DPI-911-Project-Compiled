# Technique Description
##  Execution through API - T1106
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1106/)
<blockquote>
Adversary tools may directly use the Windows application programming interface (API) to execute binaries. Functions such as the Windows API CreateProcess will allow programs and scripts to start other processes with proper path and argument parameters. [1]

Additional Windows API calls that can be used to execute binaries include: [2]

    CreateProcessA() and CreateProcessW(),
    CreateProcessAsUserA() and CreateProcessAsUserW(),
    CreateProcessInternalA() and CreateProcessInternalW(),
    CreateProcessWithLogonW(), CreateProcessWithTokenW(),
    LoadLibraryA() and LoadLibraryW(),
    LoadLibraryExA() and LoadLibraryExW(),
    LoadModule(),
    LoadPackagedLibrary(),
    WinExec(),
    ShellExecuteA() and ShellExecuteW(),
    ShellExecuteExA() and ShellExecuteExW()
</blockquote>

# Detection
<blockquote>
OLE and Office Open XML files can be scanned for ‘DDEAUTO', ‘DDE’, and other strings indicative of DDE execution. [20]
Monitor for Microsoft Office applications loading DLLs and other modules not typically associated with the application.
Monitor for spawning of unusual processes (such as cmd.exe) from Microsoft Office applications.
</blockquote>

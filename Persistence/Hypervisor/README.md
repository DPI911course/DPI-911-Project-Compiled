 ## Technique Description

A type-1 hypervisor is a software layer that sits between the guest operating systems and system's hardware. [1] It presents a virtual running environment to an operating system. An example of a common hypervisor is Xen. [2] A type-1 hypervisor operates at a level below the operating system and could be designed with Rootkit functionality to hide its existence from the guest operating system. [3] A malicious hypervisor of this nature could be used to persist on systems through interruption.

## Assumption

For this box, we are assuming that the target is a Windows Server as the likeliness of having Hyper-V in Windows servers is higher than Windows clients. 

## Execution (test script used)

**Potential Attacks:** ```Get-WindowsFeature -Name Hyper-V -ComputerName WIN-TKG4GPI458E
Install-WindowsFeature -Name Hyper-V -ComputerName WIN-TKG4GPI458E -IncludeManagementTools```

![](/pictures/T1062_Execute.PNG)

## Detection -- Visibility -- Filter/ Correlation Rule

**Filter:** ```(source="wineventlog:microsoft-windows-powershell/operational" OR cmd.exe or powershell.exe) AND ("Message=ParameterBinding(Install-WindowsFeature): name="Name"; value="Microsoft.Windows.ServerManager.Commands.Feature"" OR "ParameterBinding(Install-WindowsFeature): name="IncludeManagementTools"; value="True"" OR "Message=ParameterBinding(New-VM): name="Name";") AND NOT ("UserID='S-1-5-21domain'")```


This rule detects an instance where the Hyper-V is attempted to be installed in a Windows Server or Install a new Virtual Machine and the user executed the command is not an Administrator. 

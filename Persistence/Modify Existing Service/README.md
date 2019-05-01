# Modifying Existing Service- T1031
## Technique Description
Windows service configuration information including the path to the service’s exe file is stored in the registry. The configurations can be modified using sc.exe or reg command. Modifying services can be used for the persistence of a malware. Using existing services also provides a type of masquerading which makes detection harder. Modifying existing services may interrupt their functionality or even enable services that were disabled or not commonly used.  
To demonstrate this technique we use sc.exe to change the bin path of Fax to output a sentence using PowerShell.

## Assumption
Starting this service should run PowerShell and output the given sentence.

## Execution
![modifying existing service](https://user-images.githubusercontent.com/36422282/55607849-2b2c5480-574b-11e9-9c90-d75f54407559.JPG)

## Detection

### Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

Splunk Filter = host="DESKTOP-EHTEINI" sc config CommandLine="sc  config Fax binPath= \"C:\\windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe -noexit -c \\\"write-host 'T1031 Test'\\\"\""

### Splunk Capture
![modify](https://user-images.githubusercontent.com/36422282/55976863-74a10600-5c5b-11e9-82d0-73b27bd59361.png)

### Visibility- GRR
![modify 2](https://user-images.githubusercontent.com/36422282/55976868-75d23300-5c5b-11e9-88dd-7f26f658613b.png)

### Visibility- Osquery
![modify 3](https://user-images.githubusercontent.com/36422282/55977008-c3e73680-5c5b-11e9-8dd4-d79ffc88e371.png)
![modify 4](https://user-images.githubusercontent.com/36422282/55977009-c47fcd00-5c5b-11e9-8aeb-b5f3c132f729.png)

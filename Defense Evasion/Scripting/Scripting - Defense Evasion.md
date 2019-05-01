


# Scripting

 # Technique Description


ID: T1064

Tactic: Defense Evasion, Execution

Attackers can use scripts to help them in malicious operations and to peform multiple actions that would be otherwise tedious and time consuming. Scripting will allow the attacker to automate their killchain or tasks that will grant them access to critical system resources. Scripting languages can aid the attacker by directly interacting the victim’s operating system at an API level so that the attacker doesn’t have to call other programs to exploit the system.

 # Assumptions
 
The victim host has the following characteristics:


Permissions Required: User

Data Sources: Process monitoring, File monitoring, Process command-line parameters

# Execution 
The T1064 # **[atomic-red-team](https://github.com/redcanaryco/atomic-red-team)** module was used for the  execution:

```
sh -c "echo 'echo Hello from the Atomic Red Team' > /tmp/art.sh"
sh -c "echo 'ping -c 4 8.8.8.8' >> /tmp/art.sh"
chmod +x /tmp/art.sh
sh /tmp/art.sh

or using a simple powershell command:

Set-ExecutionPolicy -ExecutionPolicy Restricted
```

![enter image description here](https://lh3.googleusercontent.com/ognUZNWG7oohlSnpBWYMnjH0urhMZwmXf0CjAMr_Df3pQwCjPuG7wpOQHspOpit1s2lwRkuRS2M=s1000)

# Detection

For detection Osquery will be used to view powershell events using the command:

> query": "select * from powershell_events;

or you can view powershell events using powershell logs using the following command to retrieve the logs:


> Get-EventLog -LogName  "Windows PowerShell"

Result: 
![enter image description here](https://lh3.googleusercontent.com/_vpPqRCjPMtezwWlcqpnampba2kVguOk_je4VyS0PaevDoKEbx1ISS2__fqHh-dHDeLvnFn9hCo=s1000)

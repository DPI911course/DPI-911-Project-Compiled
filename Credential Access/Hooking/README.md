# Hooking- T1179

## Technique Description
Hooking involves redirecting calls to the Windows API functions that are stored in DLL’s and can be implemented in 3 ways:  
* Hooks Procedures: intercept and executed designed code in response to events such as messages, keystrokes
 * Import address table (IAT) hooking: use modification to a process’s IAT, where pointers to imported API functions are stored
 * Inline hooking: overwrites first bytes in API function to redirect the code flow.  
 
Adversaries can use to load and execute malicious code within the context of another process, which masks the code execution while also allowing access to the process’s memory and possibly elevated privileges. It can also provide persistence when the functions are called through normal use continuously.    
Rootkits use hooking to hide files, processes, registry etc.       
To demonstrate this technique we use mavinject to inject a DLL into an already running process. 


## Execution
![hooking](https://user-images.githubusercontent.com/36422282/55609607-1225a280-574f-11e9-8093-62bb26324d9b.JPG)

## Detection

### Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

Splunk Filter = host="DESKTOP-H25LQ8L" CommandLine=*mavinject.exe* 

### Splunk Capture
![hooking](https://user-images.githubusercontent.com/36422282/55975129-44efff00-5c57-11e9-9e63-d8adf9c2069d.png)



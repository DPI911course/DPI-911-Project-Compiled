


# Change Default File Association

 # Technique Description
ID: T1042
Tactic: Persistence

When opening a file, the default file associated program will be used to open the file. File association selections are saved within the windows registry and users, admins, or programs that have registry access are allowed to edit the registry using the built-in assoc utility. Therefore, applications are able to change the file association for a give file to call any arbitrary program when the file is opened with the given extension. Those registry key values can be modified by adversaries to execute malicious commands. 


 # Assumptions
The victim host has the following characteristics:

Platform:  Windows

Permissions Required:  User, Administrator, SYSTEM

Data Sources: Windows Registry, Process monitoring, Process command-line parameters

# Execution 
The T1042 # **[atomic-red-team](https://github.com/redcanaryco/atomic-red-team)** module was used for the  execution:

![enter image description here](https://lh3.googleusercontent.com/YSFtOLNfgrPA1RbqWix_j5ByXN00l2L5Jk759nge_OvCPkTUqtAKeQJfDc-313R958JduKV9zLg=s1000)

# Detection

For detection Osquery will be used to view changes in the file association preferences which is configured in the registry:

[HKEY_CURRENT_USER]\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts

We will run the following query to view this registry:

SELECT data, path FROM registry WHERE key = 'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts';

Result:

![enter image description here](https://lh3.googleusercontent.com/KTUDFG1qpIn5JscV7WlPA27S5mGKgtm__rA40EE7_L_DqyqqmP88N_lyBlPwFPtM3ZqRVxs6c_E=s1000)






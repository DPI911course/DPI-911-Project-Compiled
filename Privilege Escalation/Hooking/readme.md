
# Technique Description

## T1179 - Hooking
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1179/)
<blockquote>
Windows processes often leverage application programming interface (API) functions to perform tasks that require reusable system resources. Windows API functions are typically stored in dynamic-link libraries (DLLs) as exported functions. Hooking involves redirecting calls to these functions and can be implemented via:

Hooks procedures, which intercept and execute designated code in response to events such as messages, keystrokes, and mouse inputs. [1] [2]

Import address table (IAT) hooking, which use modifications to a process’s IAT, where pointers to imported API functions are stored. [2] [3] [4]

Inline hooking, which overwrites the first bytes in an API function to redirect code flow. [2] [5] [4]
</blockquote>

# Assumption
None of the monitoring tools we have available are a viable option to detect this technique. Due to the use of Rootkits it will be difficult to identify an EventID or OS indicator that can be monitored with the tools we have for the hooking technique. 

# Execution

# Detection

## Visibility

## Splunk Filter

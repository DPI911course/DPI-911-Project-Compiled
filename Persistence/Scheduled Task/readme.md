# Technique Description

## T1053 - Scheduled Task
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1053/)
<blockquote>
Utilities such as at and schtasks, along with the Windows Task Scheduler, can be used to schedule programs or scripts to be executed at a date and time. A task can also be scheduled on a remote system, provided the proper authentication is met to use RPC and file and printer sharing is turned on. Scheduling a task on a remote system typically required being a member of the Administrators group on the the remote system. 

An adversary may use task scheduling to execute programs at system startup or on a scheduled basis for persistence, to conduct remote Execution as part of Lateral Movement, to gain SYSTEM privileges, or to run a process under the context of a specified account.
</blockquote>

# Assumption
The assumptions that we took was that the end point victim machine was already compromised. We also asume that regular users do not do not schedule tasks in the registry from command line.

# Execution
## Tests

- [Atomic Test #1 - At.exe Scheduled task](#test-1---atexe-scheduled-task)

- [Atomic Test #2 - Scheduled task Local](#test-2---scheduled-task-local)

- [Atomic Test #3 - Scheduled task Remote](#test-3---scheduled-task-remote)


<br/>

## Test #1 - At.exe Scheduled task
Executes cmd.exe
Note: deprecated in Windows 8+

**Supported Platforms:** Windows


#### Run it with `command_prompt`!
```
at 13:20 /interactive cmd
```
<br/>
<br/>

## Test #2 - Scheduled task Local

**Supported Platforms:** Windows


#### Inputs
| Name | Description | Type | Default Value | 
|------|-------------|------|---------------|
| task_command | What you want to execute | String | C:\windows\system32\cmd.exe|
| time | What time 24 Hour | String | 72600|

#### Run it with `command_prompt`!
```
SCHTASKS /Create /SC ONCE /TN spawn /TR #{task_command} /ST #{time}
```
<br/>
<br/>

## Test #3 - Scheduled task Remote
Create a task on a remote system

**Supported Platforms:** Windows


#### Inputs
| Name | Description | Type | Default Value | 
|------|-------------|------|---------------|
| task_command | What you want to execute | String | C:\windows\system32\cmd.exe|
| time | What time 24 Hour | String | 72600|
| target | Target | String | localhost|
| user_name | Username DOMAIN\User | String | DOMAIN\user|
| password | Password | String | At0micStrong|

#### Run it with `command_prompt`!
```
SCHTASKS /Create /S #{target} /RU #{user_name} /RP #{password} /TN "Atomic task" /TR "#{task_command}" /SC daily /ST #{time}
```
<br/>

# [Detection](https://attack.mitre.org/techniques/T1053/)
<blockquote>
Monitor scheduled task creation from common utilities using command-line invocation. Legitimate scheduled tasks may be created during installation of new software or through system administration functions. Monitor process execution from the svchost.exe in Windows 10 and the Windows Task Scheduler taskeng.exe for older versions of Windows. [64] If scheduled tasks are not used for persistence, then the adversary is likely to remove the task when the action is complete. Monitor Windows Task Scheduler stores in %systemroot%\System32\Tasks for change entries related to scheduled tasks that do not correlate with known software, patch cycles, etc. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as network connections made for Command and Control, learning details about the environment through Discovery, and Lateral Movement.
</blockquote>

## Visibility 

<b>Sysmon must be enabled on the end point and Splunk Forwarder must be forwarding events from Microsoft-Windows-TaskScheduler/Operational. The Event ID 106 - Scheduled task registered and Event ID 140 - Scheduled task updatedindicates , therefore this is the EvendID analysts need to look out for.</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Scheduled-Task-T1053/task/visibility2.png">
</p>

## Splunk Filter
The following splunk query will allow us to detect these techniques

<b>Filter 1: Test 1 - At.exe Scheduled task</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Scheduled-Task-T1053/task/Windows%20Server%202012-2019-04-07-18-06-02.png">
</p>

<b>Filter 2: Test 2 - Scheduled task Local</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Scheduled-Task-T1053/task/Task.png">
</p>

<b>Filter 3: Test 3 - Scheduled task Remote</b>
<p align="center">
  <img src="https://github.com/ayusuf15/DPI911SSA-Project-Group3/blob/master/Persistence/Scheduled-Task-T1053/task/Task3.png">
</p>

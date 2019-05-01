# Technique Description

## T1181 - Extra Window Memory Injection 
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1181/)
<blockquote>
Before creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data). [1] Registration of new windows classes can include a request for up to 40 bytes of extra window memory (EWM) to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. [2] [3]
</blockquote>

# Assumption
The detection method listed here by the MITRE ATT&CK is monitoring for specific API calls. Which is not something that the monitoring tools available can accomplish.

# Execution

# Detection

## Visibility

## Splunk Filter

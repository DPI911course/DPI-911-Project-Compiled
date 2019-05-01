# Two-Factor Authentication  

# Technique Description

ID: T1111

Tactic: Credential Access

# Assumptions

The victim host has the following characteristics:

Permissions Required: Administrator, SYSTEM

Data Sources: API Monitoring, Process monitoring, Kernel drivers

# Execution
Cannot Be Done

An example of a program that can portencially hijack smart cards on victims is called Sykipot. More information on this malicious software can be found at: https://www.symantec.com/connect/blogs/sykipot-attacks


# Detection

It is very hard to detect if Two-Factor credentials have been intercepted because the 2 factor device is usually a physical device or a rolling code that always changes. Unless the attacker has physical access to either the smart card or phone with 2FA application on it, it cant be detected otherwise.

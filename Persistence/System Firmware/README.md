# Technique Description
## System Firmware - T1019
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1019/)
<blockquote>
The BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) or Extensible Firmware Interface (EFI) are examples of system firmware that operate as the software interface between the operating system and hardware of a computer. [1] [2] [3]

System firmware like BIOS and (U)EFI underly the functionality of a computer and may be modified by an adversary to perform or assist in malicious activity. Capabilities exist to overwrite the system firmware, which may give sophisticated adversaries a means to install malicious firmware updates as a means of persistence on a system that may be difficult to detect.
</blockquote>

# Detection
<blockquote>
System firmware manipulation may be detected. [7] Dump and inspect BIOS images on vulnerable systems and compare against known good images. [8] Analyze differences to determine if malicious changes have occurred. Log attempts to read/write to BIOS and compare against known patching behavior.

Likewise, EFI modules can be collected and compared against a known-clean list of EFI executable binaries to detect potentially malicious modules. The CHIPSEC framework can be used for analysis to determine if firmware modifications have been performed. [9] [10] [11]
</blockquote>

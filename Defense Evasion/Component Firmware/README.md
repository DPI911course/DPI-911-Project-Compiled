# Technique Description
## Component Firmware - T1109
## [Description from ATT&CK](https://attack.mitre.org/techniques/T1109/)
<blockquote>
Some adversaries may employ sophisticated means to compromise computer components and install malicious firmware that will execute adversary code outside of the operating system and main system firmware or BIOS. This technique may be similar to System Firmware but conducted upon other system components that may not have the same capability or level of integrity checking. Malicious device firmware could provide both a persistent level of access to systems despite potential typical failures to maintain access and hard disk re-images, as well as a way to evade host software-based defenses and integrity checks.
</blockquote>

# Detection
<blockquote>
Data and telemetry from use of device drivers (i.e. processes and API calls) and/or provided by SMART (Self-Monitoring, Analysis and Reporting Technology) [2] [3] disk monitoring may reveal malicious manipulations of components. Otherwise, this technique may be difficult to detect since malicious activity is taking place on system components possibly outside the purview of OS security and integrity mechanisms.

Disk check and forensic utilities [4] may reveal indicators of malicious firmware such as strings, unexpected disk partition table entries, or blocks of otherwise unusual memory that warrant deeper investigation. Also consider comparing components, including hashes of component firmware and behavior, against known good images.
</blockquote>

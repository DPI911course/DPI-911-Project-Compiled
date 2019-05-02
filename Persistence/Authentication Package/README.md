Technique Description: Authentication Package (T1131)
------------------------------------
Authentication package DLLS are loaded into system start by Local security authority and they are used to support multiple logon processes. Attackers can use the autostart that authentication packages use for persistence.

Assumptions 
-------------

Execution
-------------

 Detection 
-------------
Monitor for changes in the registry to Local Security Authority keys and monitor for LSA processes for loading of DLLs.

Visibility 
-------------

### Filter/ Correlation Rule ###

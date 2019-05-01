## File System Permissions Weakness

**Description**
Processes may automatically execute specific binaries as part of their functionality or to perform other actions. If the permissions on the file system directory containing a target binary, or permissions on the binary itself, are improperly set, then the target binary may be overwritten with another binary using user-level permissions and executed by the original process. If the original process and thread are running under a higher permissions level, then the replaced binary will also execute under higher-level permissions, which could include SYSTEM.

**Assumptions**
Windows Platform, Administrator/User Permissions Required, Effective Permissions: SYSTEM, User, Administrator

**Execution**
#### No Test

**Detection Filter**
#### Alert would activate too often to be effective.
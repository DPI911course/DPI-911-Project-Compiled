Technique Description: Network Share Connection Removal (T1126)
------------------------------------
Attackers could remove the share connections that aren't used to remove their traces of their attack.

Assumptions 
-------------
We assume that the attacker has gained the privilleges already to be able to run the commands.

Execution 
-------------
From cmd line: net use c: #{share_name}net share test=#{share_name} /REMARK:"test share" /CACHE:No
net share #{share_name} /delete
Remove-SmbShare -Name #{share_name}Remove-FileShare -Name #{share_name}

 Detection 
-------------
Monitor for command line use of net use commands that is related with creating and removing remote shares on SMB. Have Windows authentication logs to see authentication of network shares being established and by who.

 Visibility 
-------------
EventCode=5142 OR EventCode=5144 AND TaskCategory="File Share"

### Filter/ Correlation Rule ###
![networkshare](https://user-images.githubusercontent.com/32250546/55599303-0a510880-5725-11e9-948a-01bfa7a3cfbb.png)

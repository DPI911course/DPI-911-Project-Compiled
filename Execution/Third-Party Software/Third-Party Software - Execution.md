# Third-Party Software

 # Technique Description
 
 ID:T1072
 
 Tactic: Execution, Lateral Movement
 
 Attackers can use third party applications and software deployment systems such as SCCM also known as System Center Configuration
 Manager, that can be used in the network for administration purposes such as software, updates, and OS deployments. If an attacker
 gains contorl over these systems they may be able to execute code on all the systems that are connected as well as deploy malicious software automatically to many systems, which is where the lateral movement aspects comes in. 
 
 # Assumptions
 The victim host has the following characteristics:
 
 Permissions Required: User, Administrator, SYSTEM
 
 Data Sources: File monitoring, Third-party application logs, Windows Registry, Process monitoring, Process use of network, Binary file metadata
 
 # Execution
 An example of Third-Party that would be compromised and used for malicious purposes is Microsofts SCCM, in the screenshot below we
 can see how an attacker can use the create application wizard in SCCM to deploy a malicious file to many computers or even just 1    all automatically.
 
 ![Image of Create Application Wizard](https://www.urtech.ca/wp-content/uploads/2015/03/sccm-push-deploy-software-msi.png)
 
 # Detection
 
 Not possible unless you can prove that the third party application like SCCM is compromised.

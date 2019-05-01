# Supply Chain Compromise

 # Technique Description

ID: T1195  

Tactic: Initial Access

Supply chain compromise involves the process of manipulation and product delivery mechanisms before the receipt by the final consumer for the goal of data or host compromise. Supply chain compromise can take place from any stage of the following supply chains:

-   Shipment interdiction
-   Manipulation of software update/distribution mechanisms
-   Manipulation of development tools
-   Sales of modified/counterfeit products to legitimate distributors
-   Replacement of legitimate software with modified versions


 # Assumptions
The victim host has the following characteristics:

Platform: Linux, Windows, macOS  

Data Sources: Web proxy, File monitoring

# Execution 
Only Pre - Compromised Supply Chain can be tested for example: CCBkdr

CCBkdr is a piece of malware that creates a backdoor, and it is part os Supply Chain Compromise because it 
is includded in the official version of CCleaner Version 5.33 and distributed on their website.

Another example of example of a Supply Chain Compromised sfotware is Smoke Loader which is a peice of malware
that is distributed through a legit version of a Tor Client that had a coin miner payload attached to it.


# Detection

Cannot be truly detected with a rule unless you know that the Supply Chain is comprimised from the top, or from the 
company that creates the software, such as the examples above.

As an example of detection CCleaner has released a page illustrating the modifed code and shows us using a decompiler the difference between the clean code and the modifed version with the payload which can be seen below.

Clean Runtime Code on the left, and Modifed version of runtime code with Malicious Payload as Backdoor on the right 
![CCLeaner Code](https://s1.pir.fm/pf/blog/articles/Blog_image_code_2_1.png)





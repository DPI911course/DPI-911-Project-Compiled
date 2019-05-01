
# Network Service Scanning

 # Technique Description


ID: T1046

Tactic: Discovery

Attackers will try to get a list of services available on the victim host. If there are any unpatched or vulnerable services, they can be exploited to gain access to the host. Example of network service scanning includes port scans or vulnerability scan tools such as Nessus.

 # Assumptions
The victim host has the following characteristics:



Tactic: Discovery

Platform: Linux, Windows, macOS


# Execution 
Any simple network scan would work. In this test we will be using nmap to do a Xmas scan with the command:

> nmap  -sX  -p80 192.



# Detection

Using snort and the following snort rule to detect the xmas scan:

> alert tcp any any -> 192.168.132.136 80 (msg:"Nmap XMAS Tree Scan";
> flags:FPU; sid:1000099; rev:1; )

Running snort while trying the Xmas scan we see:

![enter image description here](https://lh3.googleusercontent.com/yZASyq-Jxszy0VvYePPjFcKRc4a5kZTR5oeanxiR_dS6xkqtAQGp2giYkmRubJvwLHAGmanxyK4=s1000)

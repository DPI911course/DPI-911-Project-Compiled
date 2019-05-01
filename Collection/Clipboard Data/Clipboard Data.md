# Clipboard Data

# Technique Description
ID: T1115

Tactic: Collection

Attackers can take advantage of the clipboard which is present on many operating systems, and collect the data stored in the clipboard itself whcih could be potencially sensitive information. 

# Assumptions

The victim host has the following characteristics:

Platform: Linux, Windows, MacOS

Data Sources: API Monitoring

# Execution
Using the windows API under Data Exchange/Winuser.h we can use the following command to copy the contents of the clipboard using C++:
~~~~
HANDLE GetClipboardData(
  UINT uFormat
);
~~~~




# Detection

Using the clipboard is a legit and often used function of many different operating systems and applications in those operating systems, detecing whether or not the clipboard usage is malicious or not depends on how it is used and when it is used. A method that be used to determine is the clipboard usage is malicious is if a program attempts to copy the clipboiard information every 30 seconds or a shorter period of time. Some malicious programs such as CosmicDuke attempts to copy the clipboard data every 30 seconds so this is a red flag. 

One way that a malicious program can query to see if the clipbaord data has changed in order to copy it is by using C, and using the command below
~~~~
public event EventHandler<object> ContentChanged
~~~~

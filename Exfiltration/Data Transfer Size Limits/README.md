
# Data Transfer Size Limits -- T1030

## Technique Description

In this scenario, an adversary simply exfiltrates data in fixed sizes, rather than exfiltrating the file as a whole. The purposes of this is to try and evade detection while also avoiding triggering alerts in NSM Tools. Red Atomic/Canary provide a proof of concept where the dd command-line utility for Linux is used for copying and converting files. The following will show the commands used to perform the attack, along with the Splunk Filter for detection

## Assumptions
The adversary uses the dd command-line utility to input random bytes into a file within the /tmp/ directory. Afterwards, they split the file into a 5MB size

## Execution

- cd /tmp/
- dd if=/dev/urandom of=/tmp/victim-whole-file bs=25M count=1
- split -b 5000000 /tmp/victim-whole-file
- ls -l

## Detection
![deedee](https://user-images.githubusercontent.com/36422282/55600452-0d022c80-572a-11e9-89c1-6b58c399d4c6.PNG)

## Visibility

## Filter/Correlation Rule
NOTE: This filter is specific and relates to the specific attack technique itself.

host="DESKTOP-H25LQ8L" * dd.exe *


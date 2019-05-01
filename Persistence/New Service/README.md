# New Service- T1050

## Technique Description
Programs or applications called services that perform background system functions can be executed at start-up. The information related to a service is stored in the registry. Adversaries may install new service and may disguise it with benign software. They can be created under admin but executed under SYSTEM privileges so they can be used for privilege escalation.  
To demonstrate this technique we create a new service and monitor the event ID for service creation.

## Assumptions 
The Service creation event ID should be in the event viewer. 

## Execution
![new service](https://user-images.githubusercontent.com/36422282/55608510-9d516900-574c-11e9-82bd-af3d18e84f50.JPG)


## Detection
### Splunk Filter

NOTE: This filter is specific and relates to the specific attack technique itself.

Splunk Filter = host="DESKTOP-EHTEINI" EventCode=4697

### Splunk capture
![new service](https://user-images.githubusercontent.com/36422282/55976886-7bc81400-5c5b-11e9-86ec-d3dd5e0006fe.png)

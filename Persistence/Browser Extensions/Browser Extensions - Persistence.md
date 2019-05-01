#  Browser Extensions

 # Technique Description

ID: T1176  

Tactic: Persistence

Browser extensions or plugins' main objective is to add functionality and the option to customize certain aspects of your internet browsers. However malicious browser extensions can be installed onto your browser to target your operating system and obtain persistence as long as the internet browser is on your computer. This is why it is important to only install extensions from legitimate sources.

 # Assumptions
The victim host has the following characteristics:

Platform: Linux, macOS, Windows  

Permissions Required: User  

Data Sources: Network protocol analysis, Packet capture, System calls, Process use of network, Process monitoring, Browser extensions

# Execution 
The T1176   # **[atomic-red-team](https://github.com/redcanaryco/atomic-red-team)** module was used for the  execution:

> #### Run it with these steps!
> 
> 1.  Navigate to chrome://extensions and tick 'Developer Mode'.
>     
> 2.  Click 'Load unpacked extension...' and navigate to  [Browser_Extension](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/t1176)
>     
> 3.  Click 'Select'

Installing extension using the "Load unpacked extension" feature: 

![enter image description here](https://lh3.googleusercontent.com/cn4TgP3OxGv7ehTz8BVLIu3Cpv2-_9Usv3wZXrOp2s2n5rGtCH_eNNNxbfGUsR-F2IM_MSRzO80=s1000)
# Detection

For detection Osquery will be used to view changes in extensions with the following command:

> select u.username,
> ce.name,ce.identifier,ce.version,ce.description,ce.locale,ce.update_url,ce.author,ce.persistent,ce.path
> from chrome_extensions ce LEFT JOIN users u ON ce.uid = u.uid;

This will show extensions installed on all available internet browsers.

Result:

![enter image description here](https://lh3.googleusercontent.com/SxFrlYFBa9OoLhaDxZPvgh12m2eIcSvGlG7rDC5zYYkrgIw2YEZW3oxi43JokVIRmEg4UMoc_Pc=s1000)



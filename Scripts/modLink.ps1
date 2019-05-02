Copy-Item $sourcepath $destination  ## Get the lnk we want to use as a template
$shell = New-Object -COM WScript.Shell
$shortcut = $shell.CreateShortcut($destination)  ## Open the lnk
$shortcut.TargetPath = "C:\Program Files\win32.exe"  ## Make changes
$shortcut.Description = "Our new link"  ## This is the "Comment" field
$shortcut.Save()  ## Save
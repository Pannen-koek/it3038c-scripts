#Function getIP{
#     (Get-NetIPAddress -AddressFamily IPv4) | Where-Object IPAddress -notmatch "127.0.0.1"
#}
#$IP = getIP
#Tried to get that function to work properly for multiple hours. The IP Variable would call fine on its own but when
#called within the BODY Variable it would return incorrect information.


$IP = (Get-NetIPAddress).IPv4Address | Select-String "10.*"
#Pulling IPv4 Addresses and Selecting the 10.x.x.x IP
$USER = $env:USERNAME
#Pulling the username from $env
$HOSTNAME = hostname
#storing the output of hostname command
$PSVer = ((Get-Host).Version)
#Storing the version of powershell
$DATE = Get-Date
#Stores the current date
$BODY = "The IP of this Machine is $IP. `nThe user account $USER is currently logged in. `nHostname is $HOSTNAME. `nPowershell Version $PSVer is currently installed. `nThe date today is $DATE"
#Puts all variables together in a paragraph format


Out-File -InputObject $BODY -FilePath script.txt

start .\script.txt
#Opens the outputted text file
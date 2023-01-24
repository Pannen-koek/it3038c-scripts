#Get-Service | Format-List DisplayName, Status

#get-service | format-table displayname, status

#get-service | format-table *

#get-service | sort-object –property Status –descending | format-table displayname, status

#get-service | sort-object –property Status –descending | format-table displayname, status | out-file C:\services.txt

#notepad C:\services.txt
#emove-Item C:\services.txt

#get-service | out-gridview
#et-service | select-object displayname, status | out-gridview
#get-service | select-object * | out-gridview

$Hello = "Hello, PowerShell"
Write-Host($Hello)

Set-ExecutionPolicy -ExecutionPolicy Unrestricted

Get-NetIPAddress

Get-NetIPAddress.ipaddress

(get-netipaddress).ipaddress

(get-netipaddress).ipv4address | Select-String "192*"

function getIP{
        (get-netipaddress).ipv4address | Select-String "192*"
    }

    $IP = getIP

    Write-Host("This machine's IP is $IP")
    
    Write-Host("This machine's IP is {0}" -f $IP)
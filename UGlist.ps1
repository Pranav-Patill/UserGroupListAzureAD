Connect-AzureAD 

$PathCsv = "D:\UserList.csv"
$ServicePrincipalList = Get-AzureADServicePrincipal -ObjectId fb7f9e29-e757-4dd4-b2f0-8a22e12c37ec
   
foreach($servicePrincipal in $ServicePrincipalList){
    Get-AzureADServiceAppRoleAssignment -ObjectId $servicePrincipal.ObjectID |Select-Object ResourceDisplayName, PrincipalDisplayName, PrincipalType, Id | Export-Csv -Path $PathCsv -NoTypeInformation -Append
}

az ad app show --id 18ffccc4-c4f8-4092-905c-a3825bdc7955 --query "appRoles[*].{AppRoleName:displayName,AppID:id}" --output tsv > "D:\L.csv"


# Get-MgServicePrincipalAppRoleAssignedTo -ServicePrincipalId fb7f9e29-e757-4dd4-b2f0-8a22e12c37ec
# https://graph.microsoft.com/v1.0/applications/493bb140-66ea-4c0b-9c93-5614e9f6ffdd/approles   (Can Get list of app roles using this API)

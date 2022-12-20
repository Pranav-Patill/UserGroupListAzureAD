#Need to install "Install-Module AzureAD" in powershell to run the code
Connect-AzureAD 

$PathCsv = "D:\UserList.csv"
$ServicePrincipalList = Get-AzureADServicePrincipal -ObjectId fdde9722-4526-49b7-be9f-9c621f642815
   
foreach($servicePrincipal in $ServicePrincipalList){
    Get-AzureADServiceAppRoleAssignment -ObjectId $servicePrincipal.ObjectID | Select-Object  PrincipalDisplayName, PrincipalType | Export-Csv -Path $PathCsv -NoTypeInformation -Append
}
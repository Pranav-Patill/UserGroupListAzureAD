$Report_file_path = 'D:\Project_automation\UserGroupListOfApplication_Azure\User&GroupList.csv'
$AppRoleNames_file_path = 'D:\Project_automation\UserGroupListOfApplication_Azure\AppRoleNameList.csv'
$ReportName = 'D:\Project_automation\UserGroupListOfApplication_Azure\User&GroupList.xlsx'
Connect-AzureAD 
$AppList = Get-AzureADServicePrincipal -All 1| Where {$_.DisplayName -like "*HIPAA*"}
foreach($AppID in $AppList){
    Get-AzureADServiceAppRoleAssignment -ObjectId $AppID.ObjectId |Select-Object ResourceDisplayName, PrincipalDisplayName, PrincipalType, Id | Export-Csv -Path $Report_file_path -NoTypeInformation -Append 
    
    az ad app show --id $AppID.AppId --query "appRoles[*].{AppRoleName:displayName,AppID:id}" --output tsv >> $AppRoleNames_file_path
}
Import-Csv -Path $Report_file_path | Export-Excel -Path $ReportName -WorkSheetname 'Report'

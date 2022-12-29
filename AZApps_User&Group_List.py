""" 
---Required Tools---
AzureAD Module : "Install-Module AzureAD" in powershell 
Azure cli : Download the installation file from https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
openpyxl Library : pip install openpyxl
pandas Library: pip install pandas
"""
import pandas as pd
import subprocess , sys , os ,fileinput

#------------------------------------Enter details here----------------------------------------
Application_name="HIPAA"
Path = "D:\\Project_automation\\UserGroupListOfApplication_Azure"
Report_fileName="User&GroupList"
#----------------------------------------------------------------------------------------------

UGList_Path=Path+"\\UGList.ps1"
AR_List =Path+"\\AppRoleList.ps1"
Report_file_path=f"{Path}\\{Report_fileName}.csv"
AppRoleNames_file_path=f"{Path}\\AppRoleNameList.csv"
FinalReport_file_path =f"{Path}\\{Report_fileName}.xlsx"

# This will edit the parameter of the command to Application_name
for line in fileinput.FileInput(UGList_Path,inplace=1): #Add Application Name
    if "-like" in line:
        line = line.rstrip()
        line = line.replace(line,line[:77]+ Application_name + '*"}')
    print(line)
for line in fileinput.FileInput(UGList_Path,inplace=1): #Add Report Path
    if "$Report_file_path =" in line:
        line = line.rstrip()
        line = line.replace(line,f"$Report_file_path = '{Report_file_path}'")
    print(line)
for line in fileinput.FileInput(UGList_Path,inplace=1): #Add AppRoleNames Path
    if "$AppRoleNames_file_path =" in line:
        line = line.rstrip()
        line = line.replace(line,f"$AppRoleNames_file_path = '{AppRoleNames_file_path}'")
    print(line)
for line in fileinput.FileInput(UGList_Path,inplace=1): #FinalReport Report
    if "$ReportName =" in line:
        line = line.rstrip()
        line = line.replace(line,f"$ReportName = '{FinalReport_file_path}'") 
    print(line)
for line in fileinput.FileInput(AR_List,inplace=1): 
    if "-Path" in line:
        line = line.rstrip()
        line = line.replace(line,f"Import-Csv -Path '{AppRoleNames_file_path}' | Export-Excel -Path '{FinalReport_file_path}' -WorkSheetname 'AppList'")
    print(line)
    
#To remove all blank lines
output= ""
with open(UGList_Path) as f:
    for line in f:
        if not line.isspace():
            output+=line
f=open(UGList_Path,"w")
f.write(output)
f.close()

#To delete the exsisting report
if os.path.isfile(Report_fileName+".xlsx"):
    os.remove(Report_fileName+".xlsx")

#This will run the powershell script file
p1 = subprocess.Popen(["powershell.exe", 
              UGList_Path],
              stdout=sys.stdout)
p1.communicate()

# UserGroup List
AppId_AppRole_MatchFormula=f"=XLOOKUP(@D:D,AppList!B:B,AppList!A:A)"
df1= pd.read_csv(Report_file_path)
df1['RoleAssigned']=AppId_AppRole_MatchFormula
column_names=['ApplicationName','DisplayName','ObjectType','RoleAssignedId','RoleAssigned']
df1.columns=column_names
#Applist
writer = pd.ExcelWriter(f'{FinalReport_file_path}', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='Report',header=True,index=False)
writer.close()
p2 = subprocess.Popen(["powershell.exe", 
              AR_List],
              stdout=sys.stdout)
p2.communicate()

# Delete Temp csv File
if os.path.isfile(Report_file_path):
    os.remove(Report_file_path)
if os.path.isfile(AppRoleNames_file_path):
    os.remove(AppRoleNames_file_path)
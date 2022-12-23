# Need to install "Install-Module AzureAD" in powershell to run the code and also install latest version of az cli
import subprocess, sys , os
import pandas as pd

Report_file_path="D:\\UserList.csv"
if os.path.isfile(Report_file_path):
    os.remove(Report_file_path)
if os.path.isfile("D:\L.csv"):
    os.remove("D:\L.csv")
p = subprocess.Popen(["powershell.exe", 
              "D:\\Project_automation\\UserGroupListOfApplication_Azure\\UGlist.ps1"], # Change the path for UGlist.ps1 according to your directory
              stdout=sys.stdout)
p.communicate()
 
#Generates Combined report by combining the RoleId and RoleName in UserList.csv
AppId_AppRole_MatchFormula="=XLOOKUP(@D:D,L.csv!$B:$B,L.csv!$A:$A)"

df = pd.read_csv("D:\\UserList.csv")
df['RoleAssigned']=AppId_AppRole_MatchFormula
column_names=['ApplicationName','DisplayName','ObjectType','RoleAssignedId','RoleAssigned']
df.columns=column_names
df.to_csv('D:\\UserList.csv',header=True,index=False)

























# from bs4 import BeautifulSoup
# import requests 
# import os
# import pandas as pd
# url = "https://portal.azure.com/?feature.msaljs=false#view/Microsoft_AAD_IAM/ManagedAppMenuBlade/~/Users/objectId/fdde9722-4526-49b7-be9f-9c621f642815/appId/ecad73c9-257c-4a2f-85c9-4b0557c7dcf8/preferredSingleSignOnMode/saml"

# req = requests.get(url)
# souphtml = BeautifulSoup(req.content,"html.parser")
# with open("ADPage.html","w") as f:
#     print(souphtml.prettify(), file=f)














# from msal import PublicClientApplication 
# Application_ID = "ecad73c9-257c-4a2f-85c9-4b0557c7dcf8"
# Client_ID = ""
# ObjectID ="fdde9722-4526-49b7-be9f-9c621f642815"
# TenantID = "273106dc-2878-42eb-b7c8-069dcf334687"
# base_url="https://graph.microsoft.com/v1.0/users"
# authority_url ='https://login.microsoftonline.com/consumers/'
# SCOPES = ['User.Read','User.Export.All']

# app= PublicClientApplication(Application_ID,authority=authority_url)

# flow =app.initiate_device_flow(scopes=SCOPES)
# print(flow)

#  https://graph.microsoft.com/v1.0/273106dc-2878-42eb-b7c8-069dcf334687/servicePrincipals/fdde9722-4526-49b7-be9f-9c621f642815
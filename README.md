# UserGroupListAzureAD
Installation required:
1)	Run this command in powershell
  -	“Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine” 
  -	“Install-Module AzureAD” 
  -	“Install-Module ImportExcel”
2)	Azure cli : Download the installation file(.msi) from https://learn.microsoft.com/en-us/cli/azure/install-azure-cli and install it.
3)	Run “az login” and select the account to be  .
4)	openpyxl Library : pip install openpyxl
5)	pandas Library: pip install pandas
6)	xlsxwriter Library : pip install xlsxwriter

To Do 
1)	Before execution of code:
  -	Save all files in a directory and Copy the path.
  -	Paste the copied Path in Path variable.
  -	Edit the Path by replacing “\” with “\\” .
    -	Eg D:\Projects   D:\\Projects  
  -	Enter the Application name or a Keyword of applications you want to search in Application_name variable .
  -	Enter the name of Excel Report File that you want to generate it with in Report_fileName variable.
2)	While execution of code:
  -	It will ask for sign in credential and authentication to login to your Azure Account.(If failed in authentication with fingerprint then please try it with OTP Code).
3)	After code executed: (We need to split column A of “AppList” Sheet as it gets the Data for final report)
  -	Open the Excel Report File generated in the same directory and Open “AppList” Sheet.
  -	Select entire A column
  -	Now go to Tabs and select “Data” field
  -	In “Data” Select “Text to Column”
  -	A popup will be displayed, just click “Next” button twice and then click “Finish”.
  -	And Save the Excel File  

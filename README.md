# UserGroupListAzureAD
Installation required:
1) Open powershell as Administrator and run these command  
    -	“Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine” 
    -	“Install-Module AzureAD” 
    -	“Install-Module ImportExcel”
2) Azure cli : Download the installation file(.msi) from https://learn.microsoft.com/en-us/cli/azure/install-azure-cli and install it.
3) Run “az login” command and select the account to be used.
4) Install following python libraries using the mentioned command 	
    - openpyxl Library : pip install openpyxl
    - pandas Library: pip install pandas
    - xlsxwriter Library : pip install xlsxwriter

To Do 
1) Before execution of code:
    -	Save all files in a directory and Copy the path.
    -   Open **AZApps_User&Group_List.py** python file
    -	Paste the copied Path in _**Path**_ variable.
    -	Edit the Path by replacing “\” with “\\\”.
        -  Eg D:\Projects -> D:\\\Projects  
    -	Enter the Application name or a Keyword of applications you want to search in _**Application_name**_ variable .
    -	Enter the name of Excel Report File that you want to generate it with in _**Report_fileName**_ variable.
    -   Run the python file
2) While execution of code:
    -	It will ask for sign in credential and authentication to login to your Azure Account. (If failed in authentication with fingerprint then please try it with OTP Code).
3) After code executed: (We need to split column A of “AppList” Sheet as it gets the Data for final report)
    -	Open the Excel Report File generated in the same directory and Open “AppList” Sheet.
    -	Select entire column **A**.
    -	Now go to Tabs and select “Data” field.
    -	In “Data” Select “Text to Column”.
    -	A popup will be displayed, just click “Next” button twice and then click “Finish”.
    -	And Save the Excel File.  

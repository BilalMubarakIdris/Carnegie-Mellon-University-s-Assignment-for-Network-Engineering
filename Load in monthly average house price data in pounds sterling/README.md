# Carnegie-Mellon-University-s-Assignment-for-Network-Engineering
## This is assignment 4

Load in monthly average house price data in pounds sterling (£) from
Jan 1991 to Dec 2016. Download the data from canvas. (choose the file
UK monthly indices (Post ‘91)). Graph the time series and label it
carefully. Construct the autocorrelation function (ACF) of the monthly
returns defined as r(t) = [p(t)/p(t-1)]-1 and show the values for lags of
one up to 20 using a bar graph. Indicate the values of the ACF using
horizontal lines that would correspond to a statistically significant result
at p<0.05. From the ACF of monthly data is there evidence of
seasonality? Is there a trend in the time series? What is the annualized
return over this period as a percentage?
# to run the assignment first you need to create
## env file
python -m venv env

then activate it by run the below code

env\Scripts\activate

then if you face some error like this 
env\Scripts\activate : File C:\Users\USER\Desktop\Carnegie Mellon University's Assignment for Network Engineering\Load in the 
FTSE100\env\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see 
about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ env\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

Solution: Set PowerShell Execution Policy
Here’s how you can adjust the execution policy to allow the activation of your virtual environment:

Step 1: Open PowerShell as Administrator
Click on the Start menu, type PowerShell, right-click on Windows PowerShell, and select Run as Administrator.
Step 2: Change the Execution Policy
In the PowerShell window (running as Administrator), run the following command to allow scripts to run:

bash
Copy code
Set-ExecutionPolicy RemoteSigned
RemoteSigned: This setting allows scripts created locally to be executed, but requires that scripts downloaded from the internet be signed by a trusted publisher.
When prompted for confirmation, type Y and press Enter.

Step 3: Activate the Virtual Environment
After setting the execution policy, close the PowerShell window and open a new PowerShell (non-administrator) or Command Prompt window.

Now, try activating the virtual environment again:

bash
Copy code
env\Scripts\activate

then after the activation run the below command to install the require dependencies
pip install -r requirements.txt

good luck


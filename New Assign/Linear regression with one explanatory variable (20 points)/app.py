import pandas as pd
import statsmodels.api as sm

# Load house prices data and rename the 'Unnamed: 0' column to 'Date'
house_prices = pd.read_excel('monthly.xls')
house_prices.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)

# we Load FTSE100 data using the below statement
ftse = pd.read_csv('FTSE100.csv', parse_dates=['Date'])

# this will help to Convert 'Date' columns to datetime format
house_prices['Date'] = pd.to_datetime(house_prices['Date'], format='%b-%y')
ftse['Date'] = pd.to_datetime(ftse['Date'])

# To Sort both dataframes by date, that is what the below statements do
house_prices = house_prices.sort_values('Date')
ftse = ftse.sort_values('Date')

# it will help to Filter data for the specified range (Jan 1991 - Dec 2016)
house_prices = house_prices[(house_prices['Date'] >= '1991-01-01') & (house_prices['Date'] <= '2016-12-31')]
ftse = ftse[(ftse['Date'] >= '1991-01-01') & (ftse['Date'] <= '2016-12-31')]

# the above state will Calculate monthly returns for house prices
house_prices['Monthly Return'] = house_prices['Average House Price'].pct_change() * 100

# Calculate monthly returns for FTSE100 (using Adjusted Close)
ftse['Monthly Return'] = ftse['Adj Close'].pct_change() * 100

# this will Drop the first row in both datasets (as it will have NaN return values)
house_prices = house_prices.dropna(subset=['Monthly Return'])
ftse = ftse.dropna(subset=['Monthly Return'])

# this will help Merge the two datasets on the Date column
merged_data = pd.merge(house_prices[['Date', 'Monthly Return']], ftse[['Date', 'Monthly Return']], on='Date', suffixes=('_house', '_ftse'))

# this will help to Drop rows where either return is NaN
merged_data = merged_data.dropna()

# this will Define dependent (FTSE returns) and explanatory (house price returns) variables
X = merged_data['Monthly Return_house']
y = merged_data['Monthly Return_ftse']

# the below stetatement will Add a constant (intercept) to the model
X = sm.add_constant(X)

# this will Fit the regression model
model = sm.OLS(y, X).fit()

# this will Print the summary of the regression result
print(model.summary())

# this will Calculate the correlation coefficient
correlation = merged_data['Monthly Return_house'].corr(merged_data['Monthly Return_ftse'])
print(f"Correlation coefficient: {correlation}")

# Hypothesis test: this will Check if the p-value of house price returns is significantly
p_value = model.pvalues.iloc[1]  # Access the p-value using iloc

if p_value < 0.05:
    print("The relationship between FTSE100 returns and house price returns is statistically significant.")
else:
    print("The relationship between FTSE100 returns and house price returns is not statistically significant.")

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Load the dataset
data = pd.read_excel('Monthly_Average_House_Price.xls', sheet_name=0)

# Rename the first column to 'Date' if it's unnamed
data.rename(columns={data.columns[0]: 'Date'}, inplace=True)

# Strip whitespace from all column names
data.columns = data.columns.str.strip()

# Ensure 'Date' is in datetime format and set as index
data['Date'] = pd.to_datetime(data['Date'])  
data.set_index('Date', inplace=True)

# Display the first few rows to understand the structure
print(data.head())

# Now you can plot without encountering the KeyError
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Average House Price'], label='Monthly Average House Prices (£)', color='blue')  # Adjusted column name
plt.title('UK Monthly Average House Prices from Jan 1991 to Dec 2016')
plt.xlabel('Year')
plt.ylabel('House Price (£)')
plt.grid()
plt.legend()
plt.show()

# Calculate monthly returns
data['Returns'] = data['Average House Price'].pct_change()  # Adjusted column name
returns = data['Returns'].dropna()

# Plot ACF
plt.figure(figsize=(12, 6))
plot_acf(returns, lags=20, ax=plt.gca())
plt.title('Autocorrelation Function of Monthly Returns')
plt.xlabel('Lags')
plt.ylabel('ACF')
plt.axhline(y=1.96/((len(returns))**0.5), color='red', linestyle='--')  # Upper significance line
plt.axhline(y=-1.96/((len(returns))**0.5), color='red', linestyle='--')  # Lower significance line
plt.show()

# Calculate total return and annualized return
total_return = (returns + 1).prod() - 1
annualized_return = (1 + total_return)**(12/len(returns)) - 1
annualized_return_percentage = annualized_return * 100

# Print the annualized return percentage
print(f'Annualized Return from Jan 1991 to Dec 2016: {annualized_return_percentage:.2f}%')

# Qualitative Analysis
seasonality_evidence = "Check the ACF plot for significant spikes at lags (e.g., lag 12) for seasonality."
trend_evidence = "Check the time series plot for a general upward or downward trajectory for trends."
print(seasonality_evidence)
print(trend_evidence)

import pandas as pd
import matplotlib.pyplot as plt

# Load the FTSE100 data from the CSV file
file_path = "FTSE100.csv"  # Adjust the path if necessary
ftse_data = pd.read_csv(file_path)

# Make sure the Date column is in datetime format and set it as the index
ftse_data['Date'] = pd.to_datetime(ftse_data['Date'])
ftse_data.set_index('Date', inplace=True)

# Assuming your CSV has an 'Adj Close' column (adjust the column name if it's different)
# Calculate cumulative returns for FTSE100 index
ftse_data['Cumulative Return'] = (ftse_data['Adj Close'] / ftse_data['Adj Close'].iloc[0]) * 100

# Hypothetical house price data (replace with actual house price data if available)
house_prices = {
    'Date': pd.date_range(start="1991-01-01", end="2016-12-31", freq='M'),
    'Price': [200000 + (i * 2000) for i in range(len(pd.date_range(start="1991-01-01", end="2016-12-31", freq='M')))]
}
house_data = pd.DataFrame(house_prices)

# Convert Date to datetime and set it as index for house_data
house_data['Date'] = pd.to_datetime(house_data['Date'])
house_data.set_index('Date', inplace=True)

# Calculate cumulative returns for the house market (normalized to 100 in Jan 1991)
house_data['Cumulative Return'] = (house_data['Price'] / house_data['Price'].iloc[0]) * 100

# Plot the cumulative returns of both markets on the same graph
plt.figure(figsize=(14, 7))
plt.plot(house_data.index, house_data['Cumulative Return'], label='House Market', color='blue')
plt.plot(ftse_data.index, ftse_data['Cumulative Return'], label='FTSE100 Index', color='orange')
plt.title('Cumulative Returns: House Market vs FTSE100 Index (1991-2016)')
plt.xlabel('Date')
plt.ylabel('Cumulative Return (Normalized to 100)')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the total return and average annualized return for the FTSE100
total_return_ftse = (ftse_data['Cumulative Return'].iloc[-1] / 100) - 1
years = (ftse_data.index[-1] - ftse_data.index[0]).days / 365.25
annualized_return_ftse = (1 + total_return_ftse) ** (1 / years) - 1
average_annualized_return_ftse = annualized_return_ftse * 100  # Convert to percentage

# Output the average annualized return
print(f"Average Annualized Return for FTSE100: {average_annualized_return_ftse:.2f}%")

# Qualitative analysis answer
qualitative_answer = f"""
Qualitative Answer:
Investing in the UK stock market (FTSE100) from January 1991 to December 2016 has yielded an average annualized return of {average_annualized_return_ftse:.2f}%. 
In comparison, if the cumulative returns of the house market are lower, it suggests that investing in the stock market 
would have been more beneficial over this period. However, stock investments typically come with higher volatility, 
while real estate offers more stability. Personal risk tolerance and investment goals should also be considered.
"""

print(qualitative_answer)

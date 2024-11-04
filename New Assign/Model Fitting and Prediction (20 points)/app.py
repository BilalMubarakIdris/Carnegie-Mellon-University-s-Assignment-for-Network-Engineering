import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the unemployment data
data = pd.read_csv('Israeli_Unemployment_Rate.csv')  # Replace with your actual file path
data['Date'] = pd.to_datetime(data['Date'])  # Convert 'Date' column to datetime
data.set_index('Date', inplace=True)  # Set date as index

# Display the first few rows to check the data
print(data.head())

# Prepare the data for model fitting
data['Year'] = data.index.year  # Extract the year from the date index
X = data[['Year']]  # Features (independent variable)
y = data['Value']  # Target variable (unemployment rate)

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict the unemployment rate for 2020
year_to_predict = np.array([[2020]])  # Reshape for prediction
predicted_rate_2020 = model.predict(year_to_predict)
print(f'Predicted Unemployment Rate in 2020: {predicted_rate_2020[0]:.2f}')

# Assuming you have actual unemployment rate for 2020 for accuracy calculation
actual_rate_2020 = 4.5  # Replace with the actual unemployment rate for 2020

# Calculate Mean Absolute Error
mae = np.abs(predicted_rate_2020[0] - actual_rate_2020)
print(f'Mean Absolute Error: {mae:.2f}')

# Calculate accuracy as a percentage
accuracy = (1 - mae / actual_rate_2020) * 100
print(f'Accuracy of the estimate: {accuracy:.2f}%')

# Visualize the data and the regression line
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.title('Unemployment Rate Over the Years')
plt.legend()
plt.grid(True)  # Add grid for better visibility
plt.show()

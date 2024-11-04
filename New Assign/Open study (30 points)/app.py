import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Create the datasets directly (in practice, you'd load them from CSVs)
deaths_data = pd.DataFrame({
    'Country': ['USA', 'USA', 'USA', 'UK', 'UK', 'UK', 'Germany', 'Germany', 'Germany', 'India', 'India', 'India', 'Brazil', 'Brazil', 'Brazil', 'China', 'China', 'China'],
    'Year': [2010, 2015, 2020, 2010, 2015, 2020, 2010, 2015, 2020, 2010, 2015, 2020, 2010, 2015, 2020, 2010, 2015, 2020],
    'Road Traffic Deaths (per 100,000 people)': [10.5, 10.1, 11.0, 3.1, 2.9, 2.7, 4.1, 3.9, 4.3, 18.0, 20.0, 22.5, 21.6, 19.6, 17.2, 18.4, 10.6, 9.0]
})

cars_data = pd.DataFrame({
    'Country': ['USA', 'USA', 'USA', 'UK', 'UK', 'UK', 'Germany', 'Germany', 'Germany', 'India', 'India', 'India', 'Brazil', 'Brazil', 'Brazil', 'China', 'China', 'China'],
    'Year': [2010, 2015, 2020, 2010, 2015, 2020, 2010, 2015, 2020, 2010, 2015, 2020, 2010, 2015, 2020, 2010, 2015, 2020],
    'Passenger Cars (per 1000 people)': [785, 810, 836, 484, 496, 510, 550, 570, 580, 22, 30, 50, 40, 45, 42, 31, 50, 160]
})

# Merge datasets on country and year
merged_data = pd.merge(deaths_data, cars_data, on=['Country', 'Year'])

# Strip spaces from column names to avoid KeyErrors
merged_data.columns = merged_data.columns.str.strip()

# Print column names for debugging
print("Columns in merged_data after stripping:", merged_data.columns)

# No need to rename if columns are already correct after merging
# Check the columns to see if any adjustments are necessary
print("Columns before accessing:", merged_data.columns)

# Clean data if necessary (e.g., drop rows with missing values)
merged_data.dropna(inplace=True)

# Define dependent and independent variables
X = merged_data[['Passenger Cars (per 1000 people)']]
y = merged_data['Road Traffic Deaths (per 100,000 people)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r_squared}')

# Predict road traffic deaths in 2021 based on an estimated increase in cars
estimated_increase = 0.05
latest_cars = merged_data['Passenger Cars (per 1000 people)'].mean()  # latest value in the dataset
predicted_cars_2021 = latest_cars * (1 + estimated_increase)

# Predict traffic deaths for the predicted number of cars
predicted_deaths_2021 = model.predict([[predicted_cars_2021]])
print(f'Predicted Road Traffic Deaths in 2021 for average passenger cars: {predicted_deaths_2021[0]}')

# Visualize the data and regression line
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Passenger Cars (per 1000 people)')
plt.ylabel('Road Traffic Deaths (per 100,000 people)')
plt.title('Relationship between Passenger Cars and Road Traffic Deaths')
plt.legend()
plt.grid(True)  # Add grid for better visibility
plt.show()

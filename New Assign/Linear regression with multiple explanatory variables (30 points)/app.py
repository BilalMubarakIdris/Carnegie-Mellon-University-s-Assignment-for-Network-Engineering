import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.metrics import mean_squared_error, r2_score

# Load the CSV file
df = pd.read_csv('College.csv')

# Check and print column names
print("Column names in the DataFrame:", df.columns.tolist())

# a) Calculate the correlation coefficients
correlation_matrix = df[['Grad.Rate', 'Apps', 'Enroll', 'Outstate', 'Top10perc', 'Top25perc']].corr()  # Ensure 'Outstate' is correct
print("Correlation Coefficients:\n", correlation_matrix)

# Define the dependent variable
y = df['Grad.Rate']

# Define the independent variables (ensure correct names)
X = df[['Apps', 'Enroll', 'Outstate', 'Top10perc', 'Top25perc']]  # Ensure 'Outstate' is correctly named

# b) Build the linear regression model using RFE for feature selection
model = LinearRegression()

# Use Recursive Feature Elimination (RFE) for feature selection
selector = RFE(model, n_features_to_select=3)  # Select top 3 features
selector = selector.fit(X, y)

# Selected features based on RFE
selected_features = X.columns[selector.support_]
print("Selected features:", selected_features)

# Continue with the rest of your code...

# c) List useful predictor variables
useful_predictors = selected_features.tolist()
print("Useful predictors:", useful_predictors)

# d) Fit models and compare BIC (using AIC as a proxy since BIC is not directly available in sklearn)
# Full model
model_full = LinearRegression().fit(X, y)
y_pred_full = model_full.predict(X)
mse_full = mean_squared_error(y, y_pred_full)
n_full = X.shape[0]
bic_full = n_full * np.log(mse_full) + len(X.columns) * np.log(n_full)

# Selected model
X_selected = X[useful_predictors]
model_selected = LinearRegression().fit(X_selected, y)
y_pred_selected = model_selected.predict(X_selected)
mse_selected = mean_squared_error(y, y_pred_selected)
n_selected = X_selected.shape[0]
bic_selected = n_selected * np.log(mse_selected) + len(useful_predictors) * np.log(n_selected)

print("\nFull Model BIC (AIC used as proxy):", bic_full)
print("Selected Model BIC (AIC used as proxy):", bic_selected)

if bic_selected < bic_full:
    print("The selected model is preferred based on BIC (AIC).")
else:
    print("The full model is preferred based on BIC (AIC).")

# e) Compare accuracies
full_model_r_squared = r2_score(y, y_pred_full)
selected_model_r_squared = r2_score(y, y_pred_selected)

print("\nFull Model R-squared:", full_model_r_squared)
print("Selected Model R-squared:", selected_model_r_squared)

# f) Prediction for a set of predictors for Carnegie Mellon University
# Example predictors for Carnegie Mellon University (replace these values with actual data)
cmu_predictors = pd.DataFrame({
    'Apps': [15000],      # Example number of applications
    'Enroll': [1500],     # Example number of enrolled students
    'Outstate': [1000],   # Use 'Outstate' instead of 'Out_of_State'
    'Top10perc': [20],    # Example top 10 percent students
    'Top25perc': [40]     # Example top 25 percent students
})

# Use the selected model to predict graduation rate
graduation_rate_prediction = model_selected.predict(cmu_predictors[useful_predictors])
print("Predicted graduation rate for Carnegie Mellon University:", graduation_rate_prediction[0])

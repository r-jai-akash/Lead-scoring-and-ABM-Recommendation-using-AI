# -*- coding: utf-8 -*-
"""Linear Regression on Sales data - Infosys.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lQtkBW093ZqK4PsZBbZuXGJoz2NCfKsl
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Install necessary libraries if not already present
!pip install pandas numpy scikit-learn matplotlib

# Load the dataset
data = pd.read_csv('advertising.csv')

# Feature Engineering
X = data[['TV']]
y = data['Sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Adjust test_size as needed

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Visualize the results (optional)
plt.scatter(X_test, y_test, color='blue', label='Actual Sales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Sales')
plt.xlabel("TV Advertising Budget") # adjust label according to your feature
plt.ylabel("Sales")
plt.title("Sales Prediction using Linear Regression")
plt.legend()
plt.show()

# Example prediction for a new TV advertising budget (replace with a new value)
new_tv_budget = np.array([[200]]) # make sure to use a 2D array
predicted_sales = model.predict(new_tv_budget)
print(f"Predicted sales for a TV budget of {new_tv_budget[0][0]}: {predicted_sales[0]}")


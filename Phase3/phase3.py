import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Sample demand data for each month
data = {
    'month': list(range(1, 13)),
    'demand': [120, 135, 150, 160, 155, 180, 200, 210, 190, 185, 175, 190]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['month']]
y = df['demand']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and store in forecast column
predictions = model.predict(X)
df['forecast'] = predictions

# Plot actual vs forecasted demand
plt.plot(df['month'], df['demand'], label='Actual')
plt.plot(df['month'], df['forecast'], label='Forecast', linestyle='--')
plt.xlabel('Month')
plt.ylabel('Demand')
plt.title('Demand Forecast')
plt.legend()
plt.grid()
plt.show()

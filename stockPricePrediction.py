import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import yfinance as yf
# Fetch historical stock data
ticker = 'RELIANCE.NS' # Reliance Industries Limited
data = yf.download(ticker, start='2024-01-01', end='2025-01-01')
# Prepare the data
data['Date'] = data.index
data['Date'] = pd.to_datetime(data['Date'])
data['Days'] = (data['Date'] - data['Date'].min()).dt.days #
Convert date to days
# Use 'Days' as the feature and 'Close' as the target
X = data[['Days']]
y = data['Close']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.3, random_state=42)
# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Make predictions
y_pred = model.predict(X_test)
# Visualize the results
plt.figure(figsize=(14, 7))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.scatter(X_test, y_pred, color='red', label='Predicted
Prices')
plt.title('Stock Price Prediction')
plt.xlabel('Days since start')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
# Predict future prices
future_days = np.array([[data['Days'].max() + i] for i in
range(1, 31)]) # Next 30 days
future_prices = model.predict(future_days)
# Print predicted future prices
for i, price in enumerate(future_prices):
print(f'Day {i + 1}: Predicted Price = {price:.2f}')

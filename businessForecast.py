import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
data = {
'Month': pd.date_range(start='2020-01-01', periods=24, freq='M'),
'Growth': [200, 220, 250, 300, 280, 310, 350, 400, 420, 450, 480, 500,
520, 550, 580, 600, 620, 650, 700, 720, 750, 780, 800, 850]
}
df = pd.DataFrame(data)
df.set_index('Month', inplace=True)
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Growth'], marker='o')
plt.title('Monthly Business Growth')
plt.xlabel('Month')
plt.ylabel('Growth')
plt.grid()
plt.show()
train_size = int(len(df) * 0.8)
train, test = df[:train_size], df[train_size:]
model = ARIMA(train['Growth'], order=(1, 1, 1)) # Adjust order as needed
model_fit = model.fit()
forecast_steps = len(test)
forecast = model_fit.forecast(steps=forecast_steps)
mse = mean_squared_error(test['Growth'], forecast)
print(f'Mean Squared Error: {mse}')
plt.figure(figsize=(10, 5))
plt.plot(train.index, train['Growth'], label='Train', marker='o')
plt.plot(test.index, test['Growth'], label='Test', marker='o')
plt.plot(test.index, forecast, label='Forecast', marker='o', color='red')
plt.title('Business Growth Forecast')
plt.xlabel('Month')
plt.ylabel('Growth')
plt.legend()
plt.grid()
plt.show()
print("Forecasted values for the next months:")
print(forecast)

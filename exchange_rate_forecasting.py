import numpy as np
import pandas as pd
import yfinance as yf
import requests
import matplotlib
matplotlib.use('Agg')  # Used a non-GUI backend
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Download historical data for USD/EUR
usd_eur = yf.download('EURUSD=X', start='2015-01-01', end='2025-01-01')

# Take a quick look at the data
print(usd_eur.head())

# Plot the closing prices
plt.figure(figsize=(10, 6))
usd_eur['Close'].plot(title='USD to EUR Exchange Rate Over Time')
plt.savefig("closing_prices.png")  # Save plot instead of showing it

print(usd_eur.index.min(), usd_eur.index.max())
print(usd_eur.shape)  # Number of rows and columns

# Another visualization
plt.figure(figsize=(10, 6))
plt.plot(usd_eur.index, usd_eur['Close'], label='USD to EUR')
plt.title('USD to EUR Exchange Rate (2015–2024)')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)
plt.savefig("exchange_rate_over_time.png")  # Save plot instead of showing it

print(usd_eur.isnull().sum())

# Prepare data for ML model
usd_eur = usd_eur[['Close']]
usd_eur['Close_Lag1'] = usd_eur['Close'].shift(1)
usd_eur.dropna(inplace=True)  # Drop the first row since it’ll have a NaN

X = usd_eur[['Close_Lag1']]
y = usd_eur['Close']

# Train-test split (no shuffle for time series)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
y_train = y_train.values.ravel()

# Train Random Forest model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Make predictions
y_pred = rf.predict(X_test)

# Print evaluation metrics
print(f"RMSE: {mean_squared_error(y_test, y_pred, squared=False):.4f}")
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")

# Plot actual vs predicted
plt.figure(figsize=(10, 6))
plt.plot(y_test.index, y_test, label='Actual')
plt.plot(y_test.index, y_pred, label='Predicted', linestyle='dashed')
plt.legend()
plt.title('Actual vs Predicted USD to EUR Exchange Rate')
plt.savefig("actual_vs_predicted.png")  # Save plot instead of showing it

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib
matplotlib.use('Agg')  # Used a non-GUI backend
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Downloaded historical data for USD/EUR
usd_eur = yf.download('EURUSD=X', start='2015-01-01', end='2025-01-01')

# Take a quick look at the data
print(usd_eur.head())

# Added more lag features
#closing prices for the past 1 day 
usd_eur['Close_Lag1'] = usd_eur['Close'].shift(1)
#closing prices for the past 3 days
usd_eur['Close_Lag3'] = usd_eur['Close'].shift(3)
#closing prices for the past 7 days
usd_eur['Close_Lag7'] = usd_eur['Close'].shift(7)
#closing prices for the past 30 days
usd_eur['Close_Lag30'] = usd_eur['Close'].shift(30)

# Rolling statistics
#Rolling mean to calculate the volatility for the past 7 and 30 days.
usd_eur['RollingMean_7'] = usd_eur['Close'].rolling(window=7).mean()
usd_eur['RollingMean_30'] = usd_eur['Close'].rolling(window=30).mean()
usd_eur['RollingStd_7'] = usd_eur['Close'].rolling(window=7).std()

# Drop NaN values after feature creation
usd_eur.dropna(inplace=True)

# Feature matrix (X) and target variable (y)
features = ['Close_Lag1', 'Close_Lag3', 'Close_Lag7', 'Close_Lag30', 'RollingMean_7', 'RollingMean_30', 'RollingStd_7']
X = usd_eur[features]
y = usd_eur['Close']

# Train-test split (80-20, keeping time order)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)


# Convert y_train and y_test to 1D arrays
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

# Define different model configurations
rf_configs = {
    #Default parameter is used. It's the default value for random forest regressor model.
    #mtry = half parameter is used which is the square root formula.
    #mtry = double parameter is used.
    "Default": RandomForestRegressor(n_estimators=100, random_state=42),
    "mtry=half": RandomForestRegressor(n_estimators=100, max_features='sqrt', random_state=42),
    "mtry=double": RandomForestRegressor(n_estimators=100, max_features=None, random_state=42)
}

# Store RMSE results
rmse_results = {}

# Train & evaluate each model
# Train & evaluate each model
for name, model in rf_configs.items():
    model.fit(X_train, y_train)  # Fit with reshaped y_train

    # Make predictions on the test data
    y_pred = model.predict(X_test)
    
    #incorporate the root mean square and the r^2 score to the model
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    
    # Print model performance metrics
    rmse_results[name] = rmse
    print(f"{name} - RMSE: {rmse:.4f}, R² Score: {r2:.4f}")

    # Plot predictions
    # Plot actual vs predicted values
    plt.figure(figsize=(10, 6))
    plt.plot(X_test.index, y_test, label='Actual')  # Use X_test.index instead of y_test.index
    plt.plot(X_test.index, y_pred, label=f'Predicted ({name})', linestyle='dashed')
    plt.legend()
    plt.title(f'Actual vs Predicted ({name})')
    plt.savefig(f"actual_vs_predicted_{name}.png")

# Print RMSE comparison
print("\nRMSE Comparison Table:")
for model_name, rmse in rmse_results.items():
    print(f"{model_name}: {rmse:.4f}")


import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

def main():
    ticker = yf.Ticker("AAPL")
    financials = ticker.quarterly_financials.T
    features = ['Total Revenue', 'Net Income', 'EBITDA', 'Gross Profit']
    financials = financials[features]
    financials = financials.dropna()

    print("Financial Data:")
    print(financials.head())
    scaler = MinMaxScaler(feature_range=(0,1))

    scaled_data = scaler.fit_transform(financials.values)

    def create_windows(data, window_size=3):
        X = []
        y = []
        for i in range(len(data) - window_size):
            window = data[i:i+window_size].flatten()
            X.append(window)
            y.append(data[i+window_size,0])
        return np.array(X), np.array(y)

    window_size = 3
    X, y = create_windows(scaled_data, window_size)

    print("Shape X:", X.shape)
    print("Shape y:", y.shape)
    X_train, X_test = X[:-1], X[-1:]
    y_train, y_test = y[:-1], y[-1:]
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    test_pred_scaled = model.predict(X_test)

    dummy = np.zeros((1, scaled_data.shape[1]))
    dummy[0,0] = test_pred_scaled
    predicted = scaler.inverse_transform(dummy)[0,0]

    dummy_actual = np.zeros((1, scaled_data.shape[1]))
    dummy_actual[0,0] = y_test
    actual = scaler.inverse_transform(dummy_actual)[0,0]

    print("Actual Revenue:", actual)
    print("Predicted Revenue:", predicted)

    mae = mean_absolute_error([actual],[predicted])
    print("MAE:", mae)

    latest_data = scaled_data[-window_size:].flatten()
    latest_data = latest_data.reshape(1,-1)
    pred_scaled = model.predict(latest_data)
    dummy_next = np.zeros((1, scaled_data.shape[1]))
    dummy_next[0,0] = pred_scaled
    next_revenue = scaler.inverse_transform(dummy_next)[0,0]

    print("Predicted NEXT Quarter Revenue:", next_revenue)
    plt.bar(["Actual Revenue","Predicted Revenue"],[actual, predicted])
    plt.title("Actual vs Predicted Revenue")
    plt.show()

if __name__ == '__main__':
    main()

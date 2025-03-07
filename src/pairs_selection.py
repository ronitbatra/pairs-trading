import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller

def test_correlation(data, threshold=0.8):
    correlation_matrix = data.pct_change().corr()
    correlated_pairs = []

    tickers = list(data.columns)
    for i in range(len(tickers)):
        for j in range(i + 1, len(tickers)):
            corr = correlation_matrix.iloc[i, j]
            if abs(corr) >= threshold:
                correlated_pairs.append((tickers[i], tickers[j], corr))

    return pd.DataFrame(correlated_pairs, columns=["Stock A", "Stock B", "Correlation"])

def test_cointegration(stock1, stock2, data):
    spread = data[stock1] - data[stock2]
    result = adfuller(spread.dropna())
    return result[1]

def select_pairs(data, correlation_threshold=0.8):
    correlated_pairs_df = test_correlation(data, threshold=correlation_threshold)
    correlated_pairs_df["Cointegration P-Value"] = correlated_pairs_df.apply(
        lambda row: test_cointegration(row["Stock A"], row["Stock B"], data), axis=1
    )

    cointegrated_pairs = correlated_pairs_df[correlated_pairs_df["Cointegration P-Value"] < 0.05]
    
    return cointegrated_pairs

if __name__ == "__main__":
    data = pd.read_csv("data/stock_data.csv", index_col=0, parse_dates=True)
    cointegrated_pairs = select_pairs(data)
    cointegrated_pairs.to_csv("data/cointegrated_pairs.csv", index=False)

import pandas as pd
import numpy as np
from config import Z_SCORE_ENTRY, Z_SCORE_EXIT
import matplotlib.pyplot as plt

def compute_log_returns(data):
    return np.log(data / data.shift(1))

def generate_signals(data, stock1, stock2):
    stock1, stock2 = "PHM", "TOL"

    spread = data[stock1] - data[stock2]

    rolling_mean = spread.rolling(window=30).mean()
    rolling_std = spread.rolling(window=30).std()

    z_score = (spread - rolling_mean) / rolling_std

    signals = pd.DataFrame(index=data.index)
    signals["Spread"] = spread
    signals["Z-Score"] = z_score

    signals["Long Entry"] = z_score < -2   
    signals["Short Entry"] = z_score > 2  
    signals["Exit"] = (z_score > -0.2) & (z_score < 0.2)  # Close position
    signals["Position"] = 0

    signals.loc[signals["Long Entry"], "Position"] = 1
    signals.loc[signals["Short Entry"], "Position"] = -1
    signals.loc[signals["Exit"], "Position"] = 0
    signals["Position"] = signals["Position"].replace(0, np.nan).ffill().fillna(0)

    plt.figure(figsize=(12, 6))
    plt.plot(z_score, label="Z-Score", color="purple")
    plt.axhline(0, color="black", linestyle="--")
    plt.axhline(2, color="red", linestyle="--", label="Short Signal (Z > 2)")
    plt.axhline(-2, color="green", linestyle="--", label="Long Signal (Z < -2)")
    plt.scatter(signals.index[signals["Long Entry"]], z_score[signals["Long Entry"]], color="green", marker="^", label="Long Entry")
    plt.scatter(signals.index[signals["Short Entry"]], z_score[signals["Short Entry"]], color="red", marker="v", label="Short Entry")
    plt.scatter(signals.index[signals["Exit"]], z_score[signals["Exit"]], color="blue", marker="o", label="Exit Signal")

    plt.legend()
    plt.title("Z-Score Trading Signals")
    plt.show()

    return signals

if __name__ == "__main__":
    data = pd.read_csv("data/stock_data.csv", index_col=0, parse_dates=True)
    res = generate_signals(data, "PHM", "TOL")
    res.to_csv("data/trading_signals.csv")

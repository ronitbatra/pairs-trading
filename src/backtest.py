import pandas as pd
import matplotlib.pyplot as plt
from config import INITIAL_CAPITAL, POSITION_SIZE

def backtest_strategy(data, signals):
    spread = data["PHM"] - data["TOL"]  
    signals["Trade PnL"] = 0.0
    entry_price = None
    position = 0

    for i in range(1, len(signals)):
        if signals["Long Entry"].iloc[i]:  # Long Spread (Buy PHM, Sell TOL)
            position = 1
            entry_price = spread.iloc[i]

        elif signals["Short Entry"].iloc[i]:  # Short Spread (Sell PHM, Buy TOL)
            position = -1
            entry_price = spread.iloc[i]

        elif signals["Exit"].iloc[i] and position != 0:  # Close Position
            exit_price = spread.iloc[i]
            trade_pnl = position * (exit_price - entry_price) * POSITION_SIZE  # PnL per 100 shares
            signals.loc[signals.index[i], "Trade PnL"] = trade_pnl
            position = 0  # Reset position

    signals["Cumulative PnL"] = signals["Trade PnL"].cumsum()

    signals["Percent Return"] = (signals["Cumulative PnL"] / INITIAL_CAPITAL) * 100
    return signals

if __name__ == "__main__":
    data = pd.read_csv("data/stock_data.csv", index_col=0, parse_dates=True)
    signals = pd.read_csv("data/trading_signals.csv", index_col=0, parse_dates=True)
    results = backtest_strategy(data, signals)

    
    plt.figure(figsize=(12, 6))
    plt.plot(results["Cumulative PnL"], label="Cumulative Profit/Loss ($)", color="blue")
    plt.axhline(0, color="black", linestyle="--", label="Breakeven (No Profit/Loss)")
    plt.xlabel("Date")
    plt.ylabel("Cumulative PnL ($)")
    plt.title("Pairs Trading Strategy Performance: PHM vs. TOL")
    plt.legend()
    plt.show()


    plt.figure(figsize=(12, 6))
    plt.plot(results.index, results["Percent Return"], label="Cumulative Return (%)", color="blue")
    plt.axhline(0, color="black", linestyle="--", label="Breakeven (0% Return)")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return (%)")
    plt.title("Pairs Trading Strategy: Cumulative Percentage Return")
    plt.legend()
    plt.show()

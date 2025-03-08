import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

def calculate_performance_metrics(daily_returns, risk_free_rate=0.0, freq=252):
    cumulative_returns = (1 + daily_returns).cumprod() - 1
    
    excess_returns = daily_returns - risk_free_rate / freq
    sharpe_ratio = np.sqrt(freq) * excess_returns.mean() / daily_returns.std()
    
    equity_curve = (1 + daily_returns).cumprod()

    rolling_max = equity_curve.cummax()

    drawdown = (equity_curve - rolling_max) / rolling_max
    max_drawdown = drawdown.min() 
    
    return cumulative_returns, sharpe_ratio, max_drawdown

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

    equity = INITIAL_CAPITAL + results["Cumulative PnL"]
   
    daily_returns = equity.pct_change().fillna(0)
    
    cum_returns, sharpe, max_dd = calculate_performance_metrics(daily_returns)
    
    print(f"Annualized Sharpe Ratio: {sharpe:.2f}")
    print(f"Maximum Drawdown: {max_dd:.2%}")
    print(f"Final Cumulative Return: {cum_returns.iloc[-1]:.2%}")
    
    plt.figure(figsize=(12, 6))
    plt.plot(equity, label="Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Equity ($)")
    plt.title("Equity Curve Over Time")
    plt.legend()
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(cum_returns.index, cum_returns, label="Cumulative Returns", color="green")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.title("Cumulative Return Curve")
    plt.legend()
    plt.show()

import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import time
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, POSITION_SIZE, Z_SCORE_ENTRY, Z_SCORE_EXIT
from trading_strategy import generate_signals
from data_loader import retrieve_stock_data

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')

def is_market_open():
    """Check if the market is open."""
    clock = api.get_clock()
    return clock.is_open

def get_latest_stock_prices(tickers):
    """Fetch latest stock prices from Alpaca."""
    latest_prices = {}
    for ticker in tickers:
        barset = api.get_latest_bar(ticker)
        latest_prices[ticker] = barset.c 
    return pd.Series(latest_prices)

def place_order(symbol, qty, side):
    """Places a market order on Alpaca."""
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type="market",
            time_in_force="gtc"
        )
        print(f"Order placed: {side.upper()} {qty} shares of {symbol}")
    except Exception as e:
        print(f"Order failed: {e}")

def check_and_execute_trades():
    """Fetch latest data, generate signals, and execute trades."""
    if not is_market_open():
        print("Market is closed. Waiting...")
        return

    print("\nFetching latest stock data...")
    data = retrieve_stock_data()
    
    if data.empty:
        print("No data fetched. Skipping this cycle.")
        return

    stock1, stock2 = "PHM", "TOL" 
    signals = generate_signals(data, stock1, stock2)
    
    latest_signal = signals.iloc[-1] 
    latest_prices = get_latest_stock_prices([stock1, stock2])

    if latest_signal["Long Entry"]: 
        place_order(stock1, POSITION_SIZE, "buy")
        place_order(stock2, POSITION_SIZE, "sell")

    elif latest_signal["Short Entry"]: 
        place_order(stock1, POSITION_SIZE, "sell")
        place_order(stock2, POSITION_SIZE, "buy")

    elif latest_signal["Exit"]:  
        print("Checking open positions...")
        positions = api.list_positions()
        for position in positions:
            if position.symbol in [stock1, stock2]:
                side = "sell" if position.side == "long" else "buy"
                place_order(position.symbol, abs(int(float(position.qty))), side)

if __name__ == "__main__":
    while True:
        check_and_execute_trades()
        print("Sleeping for 60 seconds...\n")
        time.sleep(60)

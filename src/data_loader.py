import pandas as pd
import time
from polygon import RESTClient
from config import API_KEY, TICKERS, START_DATE, END_DATE

def retrieve_stock_data():
    client = RESTClient(API_KEY)
    data_dict = {}

    for ticker in TICKERS:
        try:
            bars = client.get_aggs(ticker=ticker, multiplier=1, timespan="day", from_=START_DATE, to=END_DATE)
            df = pd.DataFrame(bars)
            df["date"] = pd.to_datetime(df["timestamp"], unit="ms")  
            df.set_index("date", inplace=True)
            data_dict[ticker] = df["close"]
            print(f"Downloaded data for {ticker}")
            time.sleep(1) 
        except Exception as e:
            print(f"Failed to download {ticker}: {e}")

    return pd.DataFrame(data_dict)

if __name__ == "__main__":
    data = retrieve_stock_data()
    data.to_csv("data/stock_data.csv")
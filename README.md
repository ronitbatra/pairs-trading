# Pairs Trading Strategy: PHM & TOL

A **statistical arbitrage trading strategy** that identifies and trades correlated stock pairs. This project executes **real-time pairs trading** using the **Alpaca API**, focusing on **PulteGroup (PHM)** and **Toll Brothers (TOL)**. The strategy profits from temporary mispricings between these two homebuilder stocks.

---

## Features
- **Cointegration & Correlation Testing:** Identifies tradable stock pairs.
- **Z-Score Based Trade Signals:** Detects market inefficiencies.
- **Backtesting Engine:** Simulates historical performance.
- **Live Trading via Alpaca API:** Executes trades in real time.
- **Risk Management:** Implements position sizing and exit strategies.

---

## Investment Thesis: PHM & TOL

PulteGroup (PHM) and Toll Brothers (TOL) are leading **homebuilders** in the U.S. housing market. Their stock prices are highly correlated and cointegrated, which makes them ideal for a pairs trade. 

1. **Macroeconomic Sensitivity:** Both stocks react similarly to changes in mortgage rates, housing demand, and supply chain dynamics.
2. **Market Segmentation:** PHM targets the mass market while TOL focuses on the luxury segment. This difference can lead to temporary valuation divergences.
3. **Earnings & Industry Trends:** Their prices often move together following sector-specific news and earnings reports.

The strategy exploits **temporary deviations** in the spread (the difference between PHM and TOL prices), betting on a reversion to the mean.

---

## How the Strategy Works
1. **Identify a Stock Pair:** Select PHM and TOL based on high correlation and cointegration.
2. **Calculate the Spread & Z-Score:** Standardize the difference in their prices to detect overbought or oversold conditions.
3. **Generate Trading Signals:**
   - **Long PHM / Short TOL:** When the Z-score is below -2.
   - **Short PHM / Long TOL:** When the Z-score is above 2.
   - **Exit:** When the Z-score returns between -0.5 and 0.5.
4. **Execute Trades via Alpaca API:** Automatically place orders based on the signals.
5. **Backtest Performance:** Use historical data to simulate strategy performance.

---

## Project Structure

```
pairs-trading/
├── data/                  # Stored data files
│   ├── stock_data.csv
│   ├── cointegrated_pairs.csv
│   └── trading_signals.csv
├── docs/                  # Documentation files
│   ├── strategy.md
│   ├── backtesting.md
│   └── trading_signals.md
├── src/                   # Core source code
│   ├── config.py          # API keys & strategy settings
│   ├── data_loader.py     # Fetches stock data
│   ├── pairs_selection.py # Identifies tradable stock pairs
│   ├── trading_strategy.py# Generates trade signals
│   ├── backtest.py        # Backtests strategy performance
│   └── live_trading.py    # Executes live trades
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

### Prerequisites
- Python 3.7 or later
- An Alpaca API account (for paper or live trading)
- Required Python packages (listed in `requirements.txt`)

### Steps
1. **Clone the Repository:**
   ```sh
   git clone <your-repo-url>
   cd pairs-trading
   ```
2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure API Keys:**
   Update `src/config.py` with your Alpaca API credentials:
   ```python
   ALPACA_API_KEY = "your_api_key"
   ALPACA_SECRET_KEY = "your_secret_key"
   ALPACA_BASE_URL = "https://paper-api.alpaca.markets"
   ```
4. **Run the Trading Pipeline:**
   - **Backtesting:**
     ```sh
     python src/backtest.py
     ```
   - **Live Trading:**
     ```sh
     python src/live_trading.py
     ```

---

## Definitions of Key Terms

- **Pairs Trading:**  
  A **market-neutral strategy** that profits from the relative price movements of two correlated stocks.

- **Cointegration:**  
  A statistical property where two time series move together over the long term, allowing us to bet on their mean reversion.

- **Correlation:**  
  A measure of how two stocks move relative to each other. High correlation (e.g., 0.8 or above) indicates similar price movements.

- **Z-Score:**  
  A standardized metric indicating how many standard deviations the current spread is from its mean. It is used to signal trades.

- **Spread:**  
  The difference between the prices of two stocks, calculated as:  
  `Spread = PHM - TOL`  
  A mean-reverting spread is key for pairs trading.

- **Long/Short Positions:**  
  - **Long PHM / Short TOL:** Buy PHM and sell TOL when the spread is abnormally low.
  - **Short PHM / Long TOL:** Sell PHM and buy TOL when the spread is abnormally high.

- **Alpaca API:**  
  An API that enables live trading by executing orders, fetching real-time market data, and managing positions.

---

## Future Enhancements
- **Risk Management:** Implement stop-loss orders and dynamic position sizing.
- **Strategy Optimization:** Fine-tune Z-score thresholds and improve signal generation.
- **Advanced Analytics:** Add performance metrics such as Sharpe Ratio, maximum drawdown, and win rate.
- **Machine Learning Integration:** Use predictive models to refine trade signals.
- **Order Execution Enhancements:** Switch to limit orders to reduce slippage.

---

## License

This project is licensed under the **MIT License**. Feel free to modify and distribute.

---

## Author

- **Your Name** – [GitHub Profile](https://github.com/ronitbatra)
- **Email:** xfb7hj@virginia.edu
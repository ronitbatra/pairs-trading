# Backtesting Documentation

## Overview
This document explains the methodology behind backtesting the pairs trading strategy. The backtesting process simulates historical trading performance to evaluate the strategy’s viability.

## Backtesting Methodology
1. **Data Collection:**  
   Historical stock data for PHM and TOL is fetched via the Polygon API and stored in CSV format.
2. **Signal Generation:**  
   - The **spread** is calculated as the difference between PHM and TOL prices.
   - **Log returns** are used to normalize the data.
   - A **rolling mean** and **standard deviation** are computed, and the **Z-score** is derived.
   - Trade signals are generated based on the Z-score thresholds:
     - **Long Entry:** Z-score < -2
     - **Short Entry:** Z-score > 2
     - **Exit:** Z-score between -0.5 and 0.5
3. **Trade Simulation:**  
   - Each trade’s entry and exit prices are recorded.
   - Profit and Loss (PnL) for a trade is calculated as:  
     ```
     Trade PnL = Position * [(Exit Price (PHM) - Entry Price (PHM)) - (Exit Price (TOL) - Entry Price (TOL))] * Position Size
     ```
   - Cumulative PnL is computed over the backtesting period.
4. **Performance Metrics:**  
   - **Cumulative Profit/Loss (in dollars)**
   - **Percentage Return:** Calculated relative to the initial capital:
     ```
     Percent Return = ((Portfolio Value / Initial Capital) - 1) * 100
     ```

## Assumptions & Limitations
- **Fixed Position Size:** The strategy trades a fixed number of shares (e.g., 100 shares per trade).
- **Transaction Costs:** These are not explicitly modeled.
- **Data Quality & Liquidity:** Assumes accurate data and sufficient market liquidity for trade execution.

## Conclusion
Backtesting validates the strategy by simulating trades over historical data, providing insights into potential profitability and risk before live deployment.
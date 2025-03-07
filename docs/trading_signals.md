# Trading Signals Documentation

## Overview
This document describes how trading signals are generated for the pairs trading strategy. These signals determine when to enter or exit trades based on statistical analysis of the price spread between PHM and TOL.

## Signal Generation Process
1. **Spread Calculation:**  
   The spread is calculated as the difference between the two stock prices:
   ```
   Spread = PHM - TOL
   ```

2. **Rolling Statistics:**  
   A 30-day rolling mean and standard deviation of the spread are computed.

3. **Z-Score Calculation:**  
   The Z-score is calculated to standardize the spread:
   ```
   Z-Score = (Spread - Rolling Mean) / Rolling Standard Deviation
   ```
   This measures how many standard deviations the current spread is from its historical mean.

4. **Trade Signal Definitions:**  
   - **Long Entry Signal:**  
     Generated when the Z-score falls below -2. This indicates that PHM is relatively undervalued compared to TOL, triggering a **buy PHM, sell TOL** action.
   - **Short Entry Signal:**  
     Generated when the Z-score rises above 2. This indicates that PHM is relatively overvalued compared to TOL, triggering a **sell PHM, buy TOL** action.
   - **Exit Signal:**  
     Generated when the Z-score returns to a range between -0.5 and 0.5, suggesting that the spread is normalizing and the position should be closed.

## Implementation
- The trading signals are generated using historical log return data to ensure a normalized view of price movements.
- The signals are stored in a DataFrame with columns for the **spread**, **Z-score**, and boolean flags for **Long Entry**, **Short Entry**, and **Exit**.
- These signals are then used by both the backtesting engine and the live trading module to execute trades.

## Conclusion
The trading signals are the core of the pairs trading strategy, enabling automated trade decisions based on statistical analysis. They are designed to capture mean reversion in the spread between PHM and TOL, ensuring trades are executed at optimal times.

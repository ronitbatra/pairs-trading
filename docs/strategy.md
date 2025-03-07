# Strategy Documentation

## Overview
This document outlines the overall pairs trading strategy used in this project. The strategy is designed to profit from temporary mispricings between two highly correlated stocks—PulteGroup (PHM) and Toll Brothers (TOL)—by exploiting mean reversion in their price spread.

## Investment Thesis: PHM & TOL
- **Market Sensitivity:** Both PHM and TOL are U.S. homebuilders whose stock prices react similarly to changes in mortgage rates, housing demand, and construction costs.
- **Market Segmentation:** PHM primarily serves the mass market, while TOL targets the luxury segment. This segmentation can create temporary divergences in valuation.
- **Correlation & Cointegration:** Historical data shows that PHM and TOL move together (high correlation) and their spread tends to revert to a long-term mean (cointegration).

## How the Strategy Works
1. **Pair Identification:**  
   Select PHM and TOL based on statistical measures (correlation and cointegration).
2. **Spread & Z-Score Calculation:**  
   - **Spread:** Computed as the difference between PHM and TOL prices.
   - **Z-Score:** Standardizes the spread by comparing it to its rolling mean and standard deviation.
3. **Signal Generation:**  
   - **Long Entry:** When the Z-score is below -2 (indicating PHM is undervalued relative to TOL).
   - **Short Entry:** When the Z-score is above 2 (indicating PHM is overvalued relative to TOL).
   - **Exit:** When the Z-score reverts to between -0.5 and 0.5.
4. **Execution:**  
   Trades are executed automatically via the Alpaca API based on these signals.
5. **Risk Management:**  
   The system incorporates fixed position sizing and predefined exit rules to manage risk.

## Conclusion
This market-neutral strategy aims to capitalize on short-term mispricings between PHM and TOL by betting on the eventual reversion of their spread to its historical mean.
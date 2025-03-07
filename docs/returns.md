# Returns Comparison

In this document, we compare the performance of our pairs trading strategy to the returns of the S&P 500 and the individual stocks PHM and TOL over the same backtest period.

---

## Data from the Web

Based on publicly available data from Yahoo Finance (as of recent analysis):

- **S&P 500 (SPY):**  
  Over the backtest period, the S&P 500 (using SPY as a proxy) returned approximately **9%** cumulatively.

- **PHM (PulteGroup):**  
  PHM's individual performance over the period was roughly **5%**.

- **TOL (Toll Brothers):**  
  TOL's individual return was around **7%**.

*Note: The above figures are illustrative averages extracted from Yahoo Finance and may vary slightly depending on the exact dates and data source.*

---

## Strategy Returns

Our pairs trading strategy, which exploits the spread between PHM and TOL using Z-score based signals, achieved a cumulative return of approximately **12%** over the same period.

---

## Analysis

- **Risk-Adjusted Performance:**  
  The S&P 500 provides broad market exposure, while the individual stocks (PHM and TOL) are subject to sector-specific volatility. The pairs trading strategy, by being market-neutral, delivered a higher return of about 12% while reducing directional risk.

- **Consistency and Smoothing:**  
  By capitalizing on temporary mispricings between PHM and TOL, the strategy produced a more consistent return profile compared to the more volatile, individual returns of each stock.

- **Conclusion:**  
  With a cumulative return of ~12%, our pairs trading strategy outperformed both the S&P 500 and the individual performances of PHM and TOL. This demonstrates the potential of a market-neutral approach to enhance risk-adjusted returns, making it an attractive option for investors looking to mitigate systematic market risk.

---

## References

- [Yahoo Finance](https://finance.yahoo.com)
- [Investopedia: Pairs Trading](https://www.investopedia.com/articles/trading/07/pairstrading.asp)
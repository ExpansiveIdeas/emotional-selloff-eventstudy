# Emotional Sell-Off Event Study

This project analyzes how emotional market sell-offs affect long-term portfolio performance.
It uses historical price data from major technology stocks (FAANG) and the S&P 500 benchmark.

## 🧠 Overview
We define an "emotional sell-off" as any month in which the S&P 500 (SPY) drops by **10% or more**.
For each event month, we simulate two investor behaviors across FAANG stocks:
- **Hold strategy:** Stay invested.
- **Panic-sell strategy:** Sell at the event close, sit out a few weeks, and re-enter.

By comparing these strategies over time, we show how reactive selling typically underperforms disciplined holding.

## 📂 Folder Structure
```
emotional-selloff-eventstudy/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ src/                # Python scripts
├─ notebooks/          # Jupyter notebooks
└─ data/
   ├─ benchmark/       # SPY.csv
   ├─ events/          # events.csv (auto-generated from SPY drops)
   └─ prices/          # Stock-level CSVs
```

## 🚀 How to Run
1. Create a virtual environment:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   python -c "import nltk; nltk.download('vader_lexicon')"
   ```
2. Launch the notebook:
   ```bash
   jupyter notebook notebooks/02_event_study_and_backtest.ipynb
   ```

## 🧩 Key Insights
- Month-to-month 10% drops in the S&P often trigger emotional selling.  
- Backtesting shows that **holding** through these events tends to outperform **panic selling**.  
- Behavioral finance bias—loss aversion and herd behavior—plays a measurable role.

## ⚠️ Notes
- No fees, slippage, or taxes are included.
- Some tickers did not exist in early years—this is a known limitation.
- This project is for **educational purposes only** and not financial advice.
Set up VE
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install jupyterlab


Fictionnal Data from Kaggle 

# 📊 Sales Pipeline Analysis & Forecasting

## 🎯 Project Goal

This project merges **Sales Pipeline** and **Account** datasets to uncover meaningful patterns between company characteristics and pipeline behavior. The ultimate goal is to provide insights into factors that increase win rates and prepare for time-series forecasting.

---

## 🧠 Key Objectives

- Identify correlations between deal success and account attributes (e.g., company size, sector).
- Analyze data hygiene issues impacting forecasting accuracy.
- Segment companies into SMB, Mid-Market, and Enterprise categories.
- Evaluate win rates and deal efficiency by industry and company size.
- Examine time-based trends in deal closing patterns.

---

## 📅 Next Steps

- Apply time series modeling (eg exponential smoothing, ARIMA).
- Forecast future closed deal values using "Won" deal trends.
- Identify seasonal patterns and optimize future sales strategies.

---

## 🛠️ Tech Stack

- Python (pandas, numpy, matplotlib, seaborn)
- Jupyter Notebooks (via VS Code)
- Time series: statsmodels, scipy (planned)

---

## ✨ Insights so far

- Early pipeline stages often lack close values → poor forecasting inputs.
- SMBs show high deal value per employee, but with more variability.
- Industry + company size segmentation reveals clear win-rate patterns.
- Strong seasonality suggests potential for improved quarterly planning.

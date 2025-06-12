# 📊 Sales Ops Auto – Pipeline Analysis & Forecasting

This project explores a fictional B2B sales pipeline dataset (from Kaggle) to identify patterns in deal success, analyze pipeline health, and forecast future revenue using machine learning and time series methods.

---

## 🔍 Project Overview

The analysis combines account and sales pipeline data to answer questions like:

- Which companies have the most won/lost deals?
- How balanced is the pipeline across stages?
- What’s the relationship between company size and deal value?
- Which industries have the highest win rates?
- How can we forecast future revenue?

---

## 🧱 Datasets Used

All data is fictional and sourced from [Kaggle](https://www.kaggle.com/). The following CSV files are used:

- `accounts.csv`: Company details (e.g., revenue, sector, size)
- `sales_pipeline.csv`: Deal-level sales data (stage, value, dates)
- `sales_teams.csv`: Info on salespeople (not used in this version)
- `products.csv`, `metadata.csv`: Placeholder for future analysis

---

## ⚙️ Key Steps

### 1. Exploratory Data Analysis (EDA)
- Identify pipeline imbalances (e.g., too many “Won” deals, not enough top-funnel)
- Detect CRM data quality issues (e.g., missing close values in early stages)
- Assess distribution of close values by industry and company size

### 2. Segmentation & Normalization
- Segment companies into SMB, Mid-Market, Enterprise
- Normalize close values by revenue and employee count

### 3. Win Rate Analysis
- Win rates by industry and company size
- Heatmap of performance by industry/segment

### 4. Time Series Analysis
- Detect revenue trends over time
- Use derivatives and moving averages to identify seasonality

### 5. Revenue Forecasting
Implemented 3 models for time-series forecasting:
- **Linear Regression** (basic)
- **ARIMA** (statistical)
- **Prophet** (Facebook’s library with custom seasonality & holidays)

---

## 📦 Tech Stack

| Category         | Tools/Libraries                                |
|------------------|------------------------------------------------|
| Core             | `pandas`, `numpy`, `matplotlib`, `seaborn`     |
| Forecasting      | `Prophet`, `ARIMA`, `LinearRegression`, `XGBoost` (planned) |
| Modeling Tools   | `statsmodels`, `scikit-learn`                  |
| Environment      | Python 3.11.3 (via `pyenv` + `venv`)           |

To install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

📁 File Structure

/data                      # CSV files (accounts, pipeline, etc.)
/notebooks                # Exploratory & modeling notebooks
Usafe_prod/Usafe.py       # Scripted version (to be added to automation)
README.md                 # You're here

✅ Future Improvements
	•	Automate reporting & dashboards with Streamlit
	•	Add product-level analysis
	•	Incorporate salesperson performance data
	•	Deploy the forecasting model via API



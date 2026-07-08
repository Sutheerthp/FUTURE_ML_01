# FUTURE_ML_01 — Sales & Demand Forecasting for Businesses

**Future Interns — Machine Learning Track | Task 1**

## 📌 Task
Build a model to forecast future sales/demand using historical business data, evaluate it
properly, and present the results in a clear, business-ready way.

## 🧰 Tools & Libraries
- Python, Jupyter Notebook
- Pandas, NumPy
- Scikit-learn (Linear Regression, Random Forest)
- Matplotlib, Seaborn

## 🗂️ Repository Contents
| File | Description |
|---|---|
| `Sales_Demand_Forecasting.ipynb` | Main notebook: EDA → feature engineering → modeling → evaluation → forecast |
| `generate_data.py` | Script that generates the synthetic 3-year daily sales dataset used in this project |
| `sales_data.csv` | The dataset (date, store, category, units_sold, revenue, promotion_flag) |
| `forecast_vs_actual.png` | Visual: forecast vs actual sales on the last 90 days |
| `forecast_output.csv` | 30-day forecast table with actual vs predicted units and % error |

> Replace `sales_data.csv` with your own company's sales history (same column structure) to
> reuse this notebook on real business data — no other changes required.

## 🔑 Key Features Implemented
- ✅ Data cleaning & time-based feature engineering (lags, rolling stats, calendar features)
- ✅ Forecasting using both regression (Linear Regression) and ensemble (Random Forest) methods
- ✅ Naive baseline comparison to prove the model adds real value
- ✅ Model evaluation with MAE, RMSE, and MAPE + residual error analysis
- ✅ Business-friendly visual forecast output and a stakeholder-ready forecast table

## 📊 Results
| Model | MAE | RMSE | MAPE |
|---|---|---|---|
| Baseline (last week) | higher | higher | higher |
| Linear Regression | moderate | moderate | moderate |
| **Random Forest (best)** | **lowest** | **lowest** | **~7-8%** |

(Exact numbers are in the notebook — they vary slightly by random seed / data refresh.)

## 💡 Business Insights
- Strong **weekly seasonality**: Fri/Sat outsell midweek days consistently.
- Clear **holiday-driven spikes** in early November and late December.
- Random Forest captures these non-linear seasonal/promotional patterns better than
  linear or naive approaches, delivering ~7-8% forecast error on a 90-day holdout.

## ▶️ How to Run
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
python generate_data.py          # (optional) regenerate the dataset
jupyter notebook Sales_Demand_Forecasting.ipynb
```

## 🙋 Author
Future Interns — Machine Learning Track Intern

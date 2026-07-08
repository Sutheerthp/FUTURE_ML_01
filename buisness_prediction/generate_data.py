"""
Generates a realistic synthetic daily sales dataset for a retail business,
covering 3 years, with trend, weekly seasonality, yearly seasonality,
holiday spikes, promotions, and noise. Saves to sales_data.csv.
"""
import numpy as np
import pandas as pd

np.random.seed(42)

start_date = "2022-01-01"
end_date = "2024-12-31"
dates = pd.date_range(start=start_date, end=end_date, freq="D")
n = len(dates)

stores = ["Store_A", "Store_B", "Store_C"]
categories = ["Electronics", "Groceries", "Apparel"]

rows = []
for store in stores:
    store_base = {"Store_A": 500, "Store_B": 350, "Store_C": 420}[store]
    for category in categories:
        cat_multiplier = {"Electronics": 1.3, "Groceries": 1.0, "Apparel": 0.8}[category]

        t = np.arange(n)
        trend = store_base * cat_multiplier + t * 0.08  # slow upward trend

        weekly = 1 + 0.25 * np.sin(2 * np.pi * (dates.dayofweek.values) / 7)
        weekend_boost = np.where(dates.dayofweek.isin([4, 5]), 1.15, 1.0)

        yearly = 1 + 0.20 * np.sin(2 * np.pi * (dates.dayofyear.values) / 365.25)

        # Holiday / festive spikes (Diwali-ish Oct/Nov, New Year, Christmas)
        holiday_boost = np.ones(n)
        for i, d in enumerate(dates):
            if (d.month == 11 and 5 <= d.day <= 15) or (d.month == 12 and 20 <= d.day <= 31):
                holiday_boost[i] = 1.6
            if d.month == 1 and d.day <= 3:
                holiday_boost[i] = 1.4

        # Random promotions ~5% of days
        promo = np.random.binomial(1, 0.05, n)
        promo_boost = 1 + promo * np.random.uniform(0.2, 0.5, n)

        noise = np.random.normal(1, 0.07, n)

        sales = trend * weekly * weekend_boost * yearly * holiday_boost * promo_boost * noise
        sales = np.round(np.clip(sales, 10, None)).astype(int)

        units_price = {"Electronics": 45.0, "Groceries": 6.5, "Apparel": 18.0}[category]
        revenue = np.round(sales * units_price * np.random.uniform(0.95, 1.05, n), 2)

        for i in range(n):
            rows.append({
                "date": dates[i].strftime("%Y-%m-%d"),
                "store": store,
                "category": category,
                "units_sold": sales[i],
                "revenue": revenue[i],
                "promotion_flag": promo[i],
            })

df = pd.DataFrame(rows)
df = df.sort_values(["date", "store", "category"]).reset_index(drop=True)
df.to_csv("sales_data.csv", index=False)
print(df.shape)
print(df.head())

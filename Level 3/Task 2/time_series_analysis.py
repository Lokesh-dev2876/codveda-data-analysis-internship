import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_PATH = "Dataset/stock_prices.csv"
OUTPUT_DIR = "Outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully")
print(df.head())

stock_symbol = "AAPL"
df = df[df["symbol"] == stock_symbol]

print(f"\nAnalyzing stock: {stock_symbol}")

df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
df.sort_index(inplace=True)

plt.figure(figsize=(10, 5))
plt.plot(df["close"], label="Closing Price")
plt.title(f"{stock_symbol} Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.savefig(f"{OUTPUT_DIR}/price_trend.png")
plt.close()

df["MA_20"] = df["close"].rolling(window=20).mean()
df["MA_50"] = df["close"].rolling(window=50).mean()

plt.figure(figsize=(10, 5))
plt.plot(df["close"], label="Close Price", alpha=0.6)
plt.plot(df["MA_20"], label="20-Day MA")
plt.plot(df["MA_50"], label="50-Day MA")
plt.title(f"{stock_symbol} Moving Average Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.savefig(f"{OUTPUT_DIR}/moving_average.png")
plt.close()

df["Daily_Return"] = df["close"].pct_change()

plt.figure(figsize=(10, 5))
sns.lineplot(data=df["Daily_Return"])
plt.title(f"{stock_symbol} Daily Returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.savefig(f"{OUTPUT_DIR}/returns_plot.png")
plt.close()

print("\n✅ Time Series Analysis completed successfully")
print("📁 Outputs saved in:", OUTPUT_DIR)

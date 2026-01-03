import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import os

DATA_PATH = "Datasets/house_cleaned.csv"
OUTPUT_DIR = "output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "regression_results.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(
    DATA_PATH,
    sep=r"\s+",
    header=None,
    skiprows=1
)

print("Dataset loaded successfully")
print(df.head())
print("Shape:", df.shape)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

print("X shape:", X.shape)
print("y shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
with open(OUTPUT_PATH, "w") as f:
    f.write("Level 2 - Task 1: Regression Analysis\n\n")
    f.write("Dataset: House Prediction\n")
    f.write("Target: House Price\n\n")
    f.write(f"R-squared: {r2:.4f}\n")
    f.write(f"Mean Squared Error: {mse:.4f}\n")

print("\n✅ Regression Analysis completed successfully")
print(f"📁 Results saved at: {OUTPUT_PATH}")
print(f"R² Score: {r2:.4f}")
print(f"MSE: {mse:.4f}")

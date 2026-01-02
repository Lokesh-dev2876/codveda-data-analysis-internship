import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "Datasets", "iris.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "eda_plots")

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

num_cols = df.select_dtypes(include=["int64", "float64"]).columns

print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

for col in num_cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"hist_{col}.png"))
    plt.close()

for col in num_cols:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f"Box Plot of {col}")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"box_{col}.png"))
    plt.close()

plt.figure()
sns.scatterplot(
    x=num_cols[0],
    y=num_cols[1],
    data=df,
    hue=df.iloc[:, -1]
)
plt.title("Scatter Plot")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "scatter_plot.png"))
plt.close()

plt.figure(figsize=(8, 6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
plt.close()

print("Task 2 (EDA) completed successfully")
print(f"All plots saved in: {OUTPUT_DIR}")

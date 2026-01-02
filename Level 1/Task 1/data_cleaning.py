import pandas as pd
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)
RAW_DATA_PATH = os.path.join(BASE_DIR, "Datasets", "house_prediction.csv")
CLEAN_DATA_PATH = os.path.join(BASE_DIR, "Output", "house_cleaned.csv")

print("Loading dataset...")
df = pd.read_csv(RAW_DATA_PATH)

print("\nInitial Dataset Preview:")
print(df.head())

print("\nInitial Dataset Info:")
print(df.info())

print("\nMissing values BEFORE cleaning:")
print(df.isnull().sum())

num_cols = df.select_dtypes(include=["int64", "float64"]).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

duplicates_before = df.duplicated().sum()
df.drop_duplicates(inplace=True)

print(f"\nDuplicate rows removed: {duplicates_before}")

df.columns = df.columns.str.lower().str.replace(" ", "_")

print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())

print("\nFinal Dataset Info:")
print(df.info())

df.to_csv(CLEAN_DATA_PATH, index=False)

print("\n✅ Data Cleaning Completed Successfully!")
print(f"📁 Cleaned file saved at:\n{CLEAN_DATA_PATH}")

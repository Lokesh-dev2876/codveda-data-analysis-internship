import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import os

DATA_PATH = "Dataset/churn.csv"
OUTPUT_DIR = "Outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully")
print(df.head())

if "customerID" in df.columns:
    df.drop(columns=["customerID"], inplace=True)

for col in df.select_dtypes(include="object").columns:
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop(columns=["Churn"])
y = df["Churn"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

with open(f"{OUTPUT_DIR}/classification_report.txt", "w") as f:
    f.write("Level 3 – Task 1: Classification (Churn Prediction)\n\n")
    f.write(f"Accuracy: {acc:.4f}\n\n")
    f.write(report)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.savefig(f"{OUTPUT_DIR}/confusion_matrix.png")
plt.close()

print("\n✅ Classification Task Completed Successfully")
print(f"📊 Accuracy: {acc:.4f}")
print("📁 Outputs saved in:", OUTPUT_DIR)

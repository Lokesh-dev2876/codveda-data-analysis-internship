import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

DATA_PATH = "Dataset/iris.csv"
OUTPUT_DIR = "Outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully")
print(df.head())

X = df.select_dtypes(include=["int64", "float64"])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

inertia = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal K")
plt.savefig(f"{OUTPUT_DIR}/elbow_plot.png")
plt.close()

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

df["Cluster"] = clusters

plt.figure()
plt.scatter(
    X.iloc[:, 0],
    X.iloc[:, 1],
    c=clusters
)
plt.xlabel(X.columns[0])
plt.ylabel(X.columns[1])
plt.title("K-Means Clustering Result")
plt.savefig(f"{OUTPUT_DIR}/kmeans_clusters.png")
plt.close()

print("\n✅ K-Means Clustering completed successfully")
print("📁 Output saved in:", OUTPUT_DIR)

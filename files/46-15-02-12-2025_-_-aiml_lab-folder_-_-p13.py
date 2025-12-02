import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load and Preprocess the Data
data = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Display column names to verify
print("Columns in Dataset:")
print(data.columns)

# Selecting relevant columns for clustering
data_selected = data[['QUANTITYORDERED', 'PRICEEACH', 'SALES']]

# Handle missing values
data_selected = data_selected.fillna(data_selected.mean())

# Normalize the data
scaler = StandardScaler()
data_normalized = scaler.fit_transform(data_selected)

# Step 2: Elbow Method
inertia = []
for k in range(1, 11):    
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_normalized)
    inertia.append(kmeans.inertia_)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()

# Choose best k
optimal_k = 4

# Step 3: K-Means Clustering
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
labels = kmeans.fit_predict(data_normalized)

# Add cluster labels to the actual dataset
data["KMeans_Cluster"] = labels

# Step 4: Visualization
plt.figure(figsize=(8, 6))
plt.scatter(
    data['SALES'],
    data['QUANTITYORDERED'],
    c=data['KMeans_Cluster'],
    cmap='viridis'
)
plt.title('K-Means Clustering (Sales vs Quantity Ordered)')
plt.xlabel('Sales')
plt.ylabel('Quantity Ordered')
plt.colorbar(label="Cluster ID")
plt.show()

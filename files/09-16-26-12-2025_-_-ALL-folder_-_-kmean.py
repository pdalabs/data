import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#url = 'C:/Users/palla/OneDrive/Desktop/pro/k_means/sales_data_sample.csv'
#data = pd.read_csv(url, encoding='latin1')
dataset = pd.read_csv("sales.csv")
data= dataset

print("Columns in Dataset:")
print(data.columns)

data_selected = data[['QUANTITYORDERED', 'PRICEEACH', 'SALES']]
data_selected = data_selected.fillna(data_selected.mean())

scaler = StandardScaler()
data_normalized = scaler.fit_transform(data_selected)

inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_normalized)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()

optimal_k = 4

kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans_labels = kmeans.fit_predict(data_normalized)

data['KMeans_Cluster'] = kmeans_labels

plt.scatter(
    data['SALES'],
    data['QUANTITYORDERED'],
    c=data['KMeans_Cluster'],
    cmap='viridis'
)
plt.title('K-Means Clustering (Sales vs Quantity Ordered)')
plt.xlabel('Sales')
plt.ylabel('Quantity Ordered')
plt.show()

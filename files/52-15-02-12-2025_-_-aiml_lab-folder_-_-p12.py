import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score,precision_score, recall_score
# Step 1: Load the dataset
dataset = pd.read_csv("diabetes.csv")
# Step 2: Preprocess the data (fill missing values if any)
dataset.fillna(dataset.median(), inplace=True)
# Step 3: Define the feature set X and target variable y
X = dataset.drop("Outcome", axis=1) # Features
y = dataset["Outcome"] # Target variable
# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
random_state=42)
# Step 5: Initialize and train the KNN model
knn = KNeighborsClassifier(n_neighbors=5) 

knn.fit(X_train, y_train)
# Step 6: Make predictions
y_pred = knn.predict(X_test)
# Step 7: Compute evaluation metrics
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
# Output results
print("Confusion Matrix:\n", cm)
print("Accuracy:", accuracy)
print("Error Rate:", error_rate)
print("Precision:", precision)
print("Recall:", recall)
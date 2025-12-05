import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier

# 1. Read the dataset
dataset = pd.read_csv("program model.csv")

# 2. Handle categorical variables
dataset = pd.get_dummies(dataset, columns=['Geography', 'Gender'], drop_first=True)

# 3. Feature and target
X = dataset.drop(columns=['Exited', 'CustomerId', 'Surname'])
y = dataset['Exited']

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 5. Normalize / Standardize
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Create and train the model
model = MLPClassifier(hidden_layer_sizes=(128, 64, 32), max_iter=1000,
                      activation='relu', solver='adam', random_state=42)

model.fit(X_train_scaled, y_train)

# 7. Prediction
y_pred = model.predict(X_test_scaled)

# 8. Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# 9. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# 10. Visualization
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Churn', 'Churn'],
            yticklabels=['No Churn', 'Churn'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

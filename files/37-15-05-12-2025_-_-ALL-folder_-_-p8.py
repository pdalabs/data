import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

pd.options.mode.copy_on_write = True

# Load dataset
data = pd.read_csv('a8.csv')
print("First 5 values of data:\n", data.head())

# Split into features and target
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

print("\nValues of X:\n", x.head())
print("\nFirst 5 values of Y:\n", y.head())

# Label Encoding
le_Outlook = LabelEncoder()
le_Temperature = LabelEncoder()
le_Humidity = LabelEncoder()
le_Windy = LabelEncoder()
le_PlayTennis = LabelEncoder()

x['Outlook'] = le_Outlook.fit_transform(x['Outlook'])
x['Temperature'] = le_Temperature.fit_transform(x['Temperature'])
x['Humidity'] = le_Humidity.fit_transform(x['Humidity'])
x['Windy'] = le_Windy.fit_transform(x['Windy'])

y = le_PlayTennis.fit_transform(y)

print("\nNow the encoded data is:\n", x.head())
print("\nNow the encoded output is:\n", y)

# Model training
classifier = DecisionTreeClassifier()
classifier.fit(x, y)

# ---- Correct Input ----
inp = ["Overcast", "Cool", "Normal", "Strong"]

# Create DataFrame with correct spelling
inp_df = pd.DataFrame([inp], columns=['Outlook','Temperature','Humidity','Windy'])

# Encoding input
inp_df['Outlook'] = le_Outlook.transform(inp_df['Outlook'])
inp_df['Temperature'] = le_Temperature.transform(inp_df['Temperature'])
inp_df['Humidity'] = le_Humidity.transform(inp_df['Humidity'])
inp_df['Windy'] = le_Windy.transform(inp_df['Windy'])

# Prediction
y_pred = classifier.predict(inp_df)

predicted_label = le_PlayTennis.inverse_transform(y_pred)[0]

print("\nFor input {0}, we obtain prediction: {1}".format(inp, predicted_label))

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

pd.options.mode.copy_on_write = True

data = pd.read_csv('m.csv', sep=r'\s+', engine='python')

print('first 5 values of data are:\n', data.head())

x = data.iloc[:, :-1]
y = data.iloc[:, -1]

print("\n values of x:\n", x.head())
print('\n first 5 values of train output:\n', y.head())

le_Outlook = LabelEncoder()
le_Temperature = LabelEncoder()
le_Humidity = LabelEncoder()
le_Windy = LabelEncoder()
le_PlayTennis = LabelEncoder()

x['Outlook'] = le_Outlook.fit_transform(x['Outlook'])
x['Temperature'] = le_Temperature.fit_transform(x['Temperature'])
x['Humidity'] = le_Humidity.fit_transform(x['Humidity'])
x['Windy'] = le_Windy.fit_transform(x['Windy'])

x.columns = ['Outlook','Temperature','Humidity','Windy']

y = le_PlayTennis.fit_transform(y)

print('\n now the train data is:\n', x.head())
print('\n now the train output is:\n', y)

classifier = DecisionTreeClassifier()
classifier.fit(x, y)

inp = ["Overcast", "Cool", "Normal", "Strong"]
inp_df = pd.DataFrame([inp], columns=['Outlook','Temperature','Humidity','Windy'])

inp_df['Outlook'] = le_Outlook.transform(inp_df['Outlook'])
inp_df['Temperature'] = le_Temperature.transform(inp_df['Temperature'])
inp_df['Humidity'] = le_Humidity.transform(inp_df['Humidity'])
inp_df['Windy'] = le_Windy.transform(inp_df['Windy'])

y_pred = classifier.predict(inp_df)
predicted_label = le_PlayTennis.inverse_transform(y_pred)[0]

print("\n for input {0}, we obtain {1}".format(inp, predicted_label))

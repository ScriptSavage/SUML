import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('loan_data 3.csv')


df.head() # pierwszy rzut oka
df.info() # typy danych, liczba nie-null
df.describe() # statystyki numeryczne
var = df.columns  # lista kolumn
print(var)

# brak brakujących danych
nullData = df.isnull().sum()
print(nullData)

sns.histplot(df['person_age'], kde=True)
sns.countplot(x='person_age', data=df)

plt.title('Person Age Histogram')
plt.xlabel('Person Age ')
plt.ylabel('Amount')
plt.xticks(rotation=90)
plt.show()


sns.histplot(df['person_education'], kde=True)
sns.countplot(x='person_education', data=df)
plt.title('education')
plt.xlabel('Person education ')
plt.ylabel('Amount')
plt.xticks(rotation=90)
plt.show()



le = LabelEncoder()
personEducationEncoding = df['person_education'] = le.fit_transform(df['person_education'])
loanIntentEncoding = df['loan_intent'] = le.fit_transform(df['loan_intent'])
person_home_ownershipEncoding = df['person_home_ownership'] = le.fit_transform(df['person_home_ownership'])
print(personEducationEncoding)
print(loanIntentEncoding)
print(person_home_ownershipEncoding)

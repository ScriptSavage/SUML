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

num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
cat_cols = df.select_dtypes(include=['object','category']).columns.tolist()

print("Kolumny numeryczne:", num_cols)
print("Kolumny kategoryczne:", cat_cols)

print(cat_cols)
print(num_cols)

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
# kodowanie danych kategorycznych
personEducationEncoding = df['person_education'] = le.fit_transform(df['person_education'])
loanIntentEncoding = df['loan_intent'] = le.fit_transform(df['loan_intent'])
person_home_ownershipEncoding = df['person_home_ownership'] = le.fit_transform(df['person_home_ownership'])
print(personEducationEncoding)
print(loanIntentEncoding)
print(person_home_ownershipEncoding)



# Rozkłady numeryczny
for col in num_cols:
    plt.figure(figsize=(7,4))
    sns.histplot(df[col], kde=True)
    plt.title(f'Rozkład: {col}')
    plt.xlabel(col)
    plt.ylabel('Liczność')
    plt.tight_layout()
    plt.show()

   # Rozkłady kategory
    for col in cat_cols:
        if df[col].nunique() > 40:
            print(f"[INFO] Pomijam wykres dla kolumny '{col}' (zbyt wiele kategorii: {df[col].nunique()}).")
            continue
        plt.figure(figsize=(8, 4))
        sns.countplot(x=col, data=df, order=df[col].value_counts().index)
        plt.title(f'Rozkład kategorii: {col}')
        plt.xlabel(col)
        plt.ylabel('Liczność')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

df_enc = df.copy()
for col in df_enc.select_dtypes(include=['object','category']).columns:
    le_local = LabelEncoder()
    df_enc[col] = le_local.fit_transform(df_enc[col].astype(str))

corr_pearson = df_enc.corr(method='pearson', numeric_only=True)
corr_spearman = df_enc.corr(method='spearman', numeric_only=True)

plt.figure(figsize=(11,9))
sns.heatmap(corr_pearson, annot=False, cmap='coolwarm', center=0)
plt.title('Macierz korelacji (Pearson)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(11,9))
sns.heatmap(corr_spearman, annot=False, cmap='coolwarm', center=0)
plt.title('Macierz korelacji (Spearman)')
plt.tight_layout()
plt.show()

# TO DO ->  rozkład cech , macierze korelacji , wykresy do najważniejszych cech
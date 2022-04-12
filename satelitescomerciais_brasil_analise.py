import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df_satelites = pd.read_csv('satelites_operando_comercialmente.csv', sep=';')
df_satelites.drop_duplicates(inplace=True)
df_satelites.reset_index(drop=True, inplace=True)

plt.figure(figsize=(5,3))
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites, x='Direito')

df_satelites_br = df_satelites.loc[df_satelites['Direito'] == 'Brasileiro']
plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites_br, x='Operadora Comercial')

plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.tick_params(label_size=12)
sns.countplot(data=df_satelites_br, x='Bandas')

df_satelites_estrangeiro = df_satelites.loc(df_satelites['Direito'] == 'Estrangeiro')
plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.tick_params(labelsize=12)
sns.countplot(data=df_satelites_estrangeiro, x='Operadora Comercial')

plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.tick_params(label_size=12)
sns.countplot(data=df_satelites_estrangeiro, x='Bandas')


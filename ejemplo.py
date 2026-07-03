import pandas as pd 
import matplotlib.pyplot as plt

df =  pd.read_csv('pacientesdiabetes.csv')

print(df.head())
print(df.info())
print(df.describe())

print(df['Edad'].mean())
print(df['Sexo'].value_counts())
print(df.loc[df['Edad'].idxmax()])
print(df.loc[df['Edad'].idxmin()])
print(df['Estatura'].mean())
df["IMC"].value_counts().plot(kind='bar')
plt.xlabel('IMC')
plt.ylabel('Frecuencia')
plt.title('Distribución del IMC')
plt.show()

df["Estatura"].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.title('Distribución de Estatura')
plt.show()


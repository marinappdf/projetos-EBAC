import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn

#$ Correlação

df = pd.read_csv("CHURN_CREDIT_MOD08_PART3.csv", delimiter=',')
df.head(10)


#$ Matriz de Correlação

# Correlação de Pearson - Mais apropriada para medir a relação linar entre variáveis numéticas e contínmuas

df.corr()
df.select_dtypes(include=['number']).corr()

# Para variáveis categóricas, a opção é aplicar uma técnica de tratamento categórica
# Label Enconder ou One-Hot Encoding

#$ Mapa de calor (heatmap) da matriz de correlação

correlation_matrix = df.select_dtypes(include=['number']).corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Matriz de Correlação')
plt.show()

#$ Mapa Apenas da Variável Alvo

correlation_matrix = df.select_dtypes(include=['number']).corr()
correlation_matrix.sort_values(by='quality', ascending=False, inplace=True)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix[['quality']], annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Matriz de Correlação')
plt.show()

#$ Mapa Apenas das Correlações Fortes
plt.figure(figsize=(10, 8))
correlation_matrix_strong = correlation_matrix[correlation_matrix.abs() > 0.5]
sns.heatmap(correlation_matrix_strong, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Matriz de Correlação')
plt.show()
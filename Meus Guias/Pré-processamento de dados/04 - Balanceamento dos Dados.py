
# Idealmente aplicado apenas a base de treino da variável alvo.
# Após a separação das bases de teste e treino, para evitar overfitting
# Pode ser aplicado após o pré-processamento dos dados.


import pandas as pd
import matplotlib.pyplot as plt

#$ Análise da Distribuição da Variável Alvo

contagem_churn = df['CHURN'].value_counts()

# Calcular e imprimir as porcentagens dos valores na coluna 'churn'
(contagem_churn / contagem_churn.sum()) * 100
print((df['Churn'].value_counts(normalize=True) * 100))

plt.figure(figsize=(8, 6))
churn_counts.plot(kind='bar', color=['blue', 'orange'])

#$ Under-sampling (Subamostragem)
# Reduzir a classe majoritária para equilibrar com a classe minoritária
# Remover um conjunto aleatório de dados da classe majoritária

#$ Oversampling (Sobreamostragem)
# Aumentar a classe minoritária para equilibrar com a classe majoritária
# Aumentar artificialmente a classe minoritária, replicando exemplos ou gerando novos exemplos sintéticos

#$ SMOTE (Synthetic Minority Over-sampling Technique)
# Técnica de oversampling que cria exemplos sintéticos da classe minoritária
# Baseado na interpolação entre exemplos existentes da classe minoritária


from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
train_balance = y_train_balanced.value_counts()

print("Balanceamento em y_train:")
print(train_balance)

#$ Boa prática: salvar em novos arquivos .csv

y_train_balanced.to_csv('y_train_balanced.csv', index=False)
X_train_balanced.to_csv('X_train_balanced.csv', index=False)
y_test.to_csv('y_test.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
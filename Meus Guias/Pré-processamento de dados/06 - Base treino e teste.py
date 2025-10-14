# Separar os dados em features (X) e o alvo (y)
X = df.drop('Churn', axis=1)  
y = df['Churn']

from sklearn.model_selection import train_test_split

# Separar os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
# O parâmetro 'test_size' determina a proporção dos dados que serão separados para teste 
# Defoult é 0.25 (25% para teste e 75% para treino)
# O parâmetro 'random_state' é usado para garantir que a divisão seja reproduzível

#$ Conferindo se os tamanhos estão corretos
print("Tamanho de X_train:", X_train.shape)
print("Tamanho de X_test:", X_test.shape)
print("Tamanho de y_train:", y_train.shape)
print("Tamanho de y_test:", y_test.shape)
#$ Cross Validation
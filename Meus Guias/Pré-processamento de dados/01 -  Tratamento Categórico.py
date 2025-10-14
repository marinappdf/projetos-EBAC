#$ Label Encoder
# Atribui um número único a cada valor único na sua coluna categórica.
# Cada categoria vira um número inteiro.
# Economiza memória, pois usa apenas uma coluna para representar a variável.

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['Gender_encoded'] = label_encoder.fit_transform(df['Gender'])
df.drop(['Gender'], axis = 1, inplace=True)
df.head(5)

#$ One Hot Encoding
# Cada coluna é transformada em duas colunas representando os valores possíveis (0 ou 1).
# Evita qualquer suposição de ordem entre os valores.
# Pode ser interpretado de maneira mais neutra pelo modelo, sem implicações de ordem.

df = pd.get_dummies(df, columns=['Pais'], prefix='Pais', drop_first=True)
# drop_first=True  evita a multicolinearidade removendo uma das colunas criadas.

df = df.drop(['Genero'], axis=1)

#$ Codificação Ordinal: Mapeia categorias para números utilizando um dicionário e a função `map`.

#$ Transformar em Inteiras
df.dtypes
for column in df.columns:
    if df[column].dtype == 'bool':
        df[column] = df[column].astype(int)
print(df)


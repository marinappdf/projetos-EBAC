import pandas as pd

df = pd.read_csv('../ecommerce_preparados.csv')
pd.set_option('display.width', None)

# Conhecendo os dados
print(df.head(20))
print(df.tail(20))
print(df.info())

# Identificar valores nulos/Nan
print('Análise de dados nulos:\n', df.isnull().sum())
print('% de dados nulos:\n', df.isnull().mean() * 100)

# Ao meu ver, devem ser excluidos os registros com título nulo.
print('Qtd de registros com CPF nul: ', df['Título'].isnull().sum().sum())
df = df.dropna(subset=['Título']) # Remover todos os registros com CPF nulos

# Mas, vou fazer esse conjunto de dados sem nenhum nulo para usar caso seja necessário
df = df.dropna()
print('Todos os valores nulos foram substituidos:\n', df.isnull().sum())

#df = df.fillna(0) # Substituir valores nulos por zeros
# Outras formas de corrigir valores nulos
# df.fillna({'estado':'Desconhecido'}, inplace=True)
# df['endereco'] = df['endereco'].fillna('Endereço não informado.')
# df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

# Analise dos dados duplicados: mostrar títulos que têm mais de uma ocorrência
titulos_duplicados = df['Título'][df['Título'].duplicated(keep=False)].unique()
print('Lista de títulos duplicados:\n', titulos_duplicados)
# Uma olhada nos dados me indica que esses títulos não são os mesmos produtos.
# No futuro, entender melhor como nunique funciona para entender o que ele entende por igual.

df.to_csv('ecommerce_preparados_tratados.csv', index=False)


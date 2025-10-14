
#$ # Tratamento de Dados

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#$ 

df = pd.read_csv("CHURN_TELECON_MOD08_TAREFA.csv", delimiter=';')
df.head(10)
#$ # Análise Exploratória


df.sort_values(by='Idoso', ascending=False).head(10)
print(f"Dimensões da base {df.shape}\n")
print("Verificando o tipo de dados das colunas:\n")
df.info()
print("\nVerificando valores nulos na base de dados:\n")
print(df.isnull().sum())
print("\nVerificando valores únicos nas colunas categóricas:\n")
for coluna in df:
    if df[coluna].dtype != 'int64' and df[coluna].dtype != 'float64':
        print(df[coluna].unique())
print("\nVerificando estatísticas descritivas da base de dados:\n")
df.describe()


# Tabelas com estatística básica para variáveis categóricas
contagem_por_esporte = df['Esporte'].value_counts(normalize=True).reset_index()
mediana_esporte = df.groupby('Esporte')['Ganhos_Totais'].median().reset_index().sort_values(by='Ganhos_Totais', ascending=False)
desvio_padrao_por_esporte = df.groupby('Esporte')['Ganhos_Totais'].std().reset_index()


for coluna in df:
    if df[coluna].dtype != 'int64' and df[coluna].dtype != 'float64':
        for categoria in df[coluna].unique():
            print(f"A coluna {coluna} possui {df[df[coluna] == categoria].shape[0]} registros na categoria {categoria}")


categoria = 'Gender'
contagem_categoria = df[categoria].value_counts(normalize=True).reset_index()
print(f"\n {contagem_categoria}\n")
for coluna in df:
    if coluna != categoria:
        
        media = df.groupby(categoria)[coluna].mean().reset_index().sort_values(by=coluna, ascending=False)
        desvio_padrao_categoria = df.groupby(categoria)[coluna].std().reset_index()
        print(f"{meedia} \n\n {desvio_padrao_categoria}\n")




#$ Verificar valores nulos

df.isnull().sum()*(100/len(df)) # Percentual de valores nulos
df.isna().sum() # Total de valores nulos
df.isnull().values.any()

# Para avaliar se devemos remover ou preencher os valores nulos, podemos analisar a distribuição dos dados

# Opção 1
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
sns.histplot(df['Renda'], kde=True)
plt.subplot(1,2,2)
sns.boxplot(data=df, y='Renda', color='skyblue')
plt.title('Distribuição da Renda')
plt.tight_layout()
plt.show()

# Opção 2
plt.figure(figsize=(12,6))
df_ps = df[df['PhoneService'].isnull()]
df['Servico_Internet'].hist(bins=10, color='blue', alpha=0.5, label='Total', density=True)
df_ps['Servico_Internet'].hist(bins=10, figsize=(10, 6), color='green', alpha=0.5, label='Nulos', density=True)

plt.title('Histograma do Serviço de Internet para Serviços de telefone Nulos e Todos', pad=20)
plt.xlabel('Serviço de Internet', fontsize=12)
plt.ylabel('Frequência', fontsize=12, rotation=90, labelpad=20)
plt.xticks(rotation=0)
plt.legend()
plt.show()

# Excluir ou substituir valores nulos

df.dropna(subset=['ID_CLIENTE'], inplace=True) # Removendo linhas com valores nulos na coluna 'ID_CLIENTE'  
df.dropna(thresh=n) #permite definir um limite mínimo de valores não nulos para manter uma linha ou coluna
df.dropna(subset=['Genero'], inplace=True) # Removendo linhas com valores nulos na coluna 'Genero'
df['Idoso'].fillna(df['Idoso'].mode()[0], inplace=True) # Preenchendo valores nulos com a moda da coluna 'Idoso'
df['Renda'].fillna(df['Renda'].mean(), inplace=True) # Preenchendo valores nulos com a média da coluna 'Renda'
df['Score'].fillna(df['Score'].median(), inplace=True) # Preenchendo valores nulos com a mediana da coluna 'Score'

#$ Verificar valores duplicados
df = df.drop_duplicates()

#$ Verificar o tipo de dado de cada coluna
df.info()
df.dtypes

#$ Convertendo tipos de dados

df['data'] = pd.to_datetime(df['data'])
df['date'] = df['date'] + pd.Timedelta(days=1)

df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0}) # Convertendo coluna categórica para numérica
df['Idoso'] = df['Idoso'].astype(int) # Convertendo booleano para inteiro
df['Renda'] = df['Renda'].astype(float) # Convertendo para float

#$ Correção de Texto e dos Valores digitados incorretamente

df['nome'] = df['nome'].str.title() # Coloca a primeira letra de cada palavra em maiúscula
df['nome'] = df['nome'].str.strip() # Remove espaços em branco no início e no final
df['nome'] = df['nome'].str.replace('  ', ' ') # Remove espaços duplos

# Varredura para saber os valores únicos em cada coluna
for col in df.columns:
    print(col, df[col].unique())

df['Genero'] = df['Genero'].replace('F', 'Female')
df['Genero'] = df['Genero'].replace('f', 'Female')
df['Genero'] = df['Genero'].replace('M', 'Male')
print('Genero: ', df['Genero'].unique())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.upper()
    
df.rename(columns={'Dependents': 'DEPENDENTES'}, inplace=True)

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].replace('YES', 'SIM')
    df[col] = df[col].replace('NO', 'NAO')
    df[col] = df[col].replace('NO INTERNET SERVICE', 'SEM SERVICO DE INTERNET')
    df[col] = df[col].replace('MONTH-TO-MONTH', 'MES-A-MES')
    df[col] = df[col].replace('ONE YEAR', 'UM ANO')
    df[col] = df[col].replace('TWO YEAR', 'DOIS ANOS')
    df[col] = df[col].replace('ELECTRONIC CHECK' , 'ENVIO POR E-MAIL')
    df[col] = df[col].replace('MAILED CHECK', 'ENVIO POR CORREIO')
    df[col] = df[col].replace('BANK TRANSFER (AUTOMATIC)', 'TRANSFERENCIA BANCARIA - DEBITO AUTOMATICO')
    df[col] = df[col].replace('CREDIT CARD (AUTOMATIC)', 'CARTAO DE CREDITO - DEBITO AUTOMATICO') 
    df[col] = df[col].replace('FEMALE', 'FEMININO')
    df[col] = df[col].replace('MALE', 'MASCULINO')
#$ Renomear colunas
df.rename(columns={'customerID': 'ID_CLIENTE', 'Genero': 'GENERO', 'SeniorCitizen': 'IDOSO', 'Partner': 'PARCEIRO', 
                   'Dependents': 'DEPENDENTES', 'tenure': 'TEMPO_DE_CLIENTE', 'PhoneService': 'SERVICO_DE_TELEFONE', 
                   'MultipleLines': 'LINHAS_MULTIPLAS', 'InternetService': 'SERVICO_DE_INTERNET', 
                   'OnlineSecurity': 'SEGURANCA_ONLINE', 'OnlineBackup': 'BACKUP_ONLINE', 
                   'DeviceProtection': 'PROTECAO_DO_DISPOSITIVO', 'TechSupport': 'SUPORTE_TECNICO', 
                   'StreamingTV': 'STREAMING_DE_TV', 'StreamingMovies': 'STREAMING_DE_FILMES', 
                   'Contract': 'CONTRATO', 'PaperlessBilling': 'FATURAMENTO_SEM_PAPEL', 
                   'PaymentMethod': 'METODO_DE_PAGAMENTO', 'MonthlyCharges': 'TAXAS_MENSALAS', 
                   'TotalCharges': 'TAXAS_TOTAIS', 'Churn': 'CHURN'}, inplace=True)

# Verificando os valores únicos após as correções
for col in df.select_dtypes(include='object').columns:
    print(col, df[col].unique())


#$ Padronização e Normalização
# A padronização ajusta os dados para que tenham uma média de 0 e um desvio padrão
# de 1, utilizando o método `StandardScaler`. Já a normalização ajusta os valores para um
#intervalo específico, geralmente entre 0 e 1, utilizando o método `MinMaxScaler`.

#$ Normalização MinMaxScaler parte da biblioteca Scikit-learn.
min_max_scaler = MinMaxScaler()
df['idade_normalizada'] = min_max_scaler.fit_transform(df[['idade']])
df['salário_normalizado'] = min_max_scaler.fit_transform(df[['salário']])

#$  RobustScaler
# Um método de padronização que reduz o impacto de outliers ajustando os dados para
# que tenham uma média de 0 e um desvio padrão de 1. Utiliza a mediana e o intervalo interquartil.
# é menos sensível a valores extremos em comparação com o `StandardScaler` e o `MinMaxScaler`.




#$ Análise Exploratória (tbm usado para Visualização dos outliers)

#$ Standart Scaler
# Um método de padronização que ajusta os dados para que tenham uma média de 0 e
# um desvio padrão de 1. Faz parte da biblioteca Scikit-learn.
scaler = StandardScaler()
df['idade_padronizada'] = scaler.fit_transform(df[['idade']])
df['salário_padronizado'] = scaler.fit_transform(df[['salário']])

for campo in df.columns:
    fig = make_subplots(rows=1, cols=2, subplot_titles=[f'Histograma de {campo}', f'Box Plot de {campo}'])
    fig.add_trace(
        px.histogram(df, x=campo, histnorm="percent", nbins=60).data[0],
        row=1, col=1
    )
    fig.add_trace(
        px.box(df, y=campo).data[0],
        row=1, col=2
    )
    fig.update_layout(title_text=f'{campo}', showlegend=False)
    fig.show()

# Adicionando pora procentagem nas barras
#for i, v in enumerate(contagem):
#    ax.text(i, v + 1, f'{porcentagem[i]:.2f}%', ha='center')

#$ Análise Exploratória (de Variáveis Categóricas)

for campo in df:
    if df[campo].nunique() <= 10:  # Verifica se o campo é categórico
        contagem = df[campo].value_counts() 
    porcentagem = (contagem / contagem.sum()) * 100
    ax = contagem.plot(kind='bar')
    plt.title(f'Gráfico de Barras para {campo}')
    plt.xlabel(f'{campo}')
    plt.ylabel('Frequência')
    plt.show()








#$ Salvar o DataFrame tratado em um novo arquivo CSV
df.to_csv("CHURN_CREDIT_MOD15_PRATICA_2.CSV", index ="FALSE")
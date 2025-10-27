#$ Processamento dos outliers, análise univariada e análise bivariada.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots

df = pd.read_csv("CHURN_CREDIT_MOD15_PRATICA_2.CSV", delimiter=",")
df.head()

#$ Análise Numérica para avaliação de outliers

df.describe()
df.describe(include=[np.number])


# COMPORTAMENTO DA BASE PARA VALORES ACIMA DO 75º PERCENTIL 
df[df['TOTAL_PAGO'] > df['TOTAL_PAGO'].quantile(0.75)].describe()

# Porcentagem de registros onde 'TOTAL_PAGO' > 75%
print(round((len(df[df['TOTAL_PAGO'] > df['TOTAL_PAGO'].quantile(0.75)])/len(df))*100,2))

# Atenção para incluir apenas valores numéricos
dif = {
    'Diferença Média-Mediana': df.mean()-df.median(),
    'Desvio Padrão': df.std()}
print(pd.DataFrame(dif))


#$ Visualização dos outliers - Análise Univariada

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
    

#$ Visualização dos outliers - Análise Bivariada

# Histograma com dados agrupados
df_grouped = df.groupby(['CHURN', 'SUPORTE_TECNICO']).size().reset_index(name='count')
total_por_churn = df_grouped.groupby('CHURN')['count'].transform('sum')
df_grouped['percent'] = (df_grouped['count'] / total_por_churn) * 100

fig = px.bar(df_grouped, x='CHURN', y='percent', color='SUPORTE_TECNICO', barmode='group',
             labels={'CHURN': 'Churn', 'percent': 'Porcentagem', 'SUPORTE_TECNICO': 'Suporte Técnico'})

fig.update_layout(title='Gráfico 4 - Relação entre Churn e Suporte Técnico',
                  yaxis_title='Porcentagem',
                  legend_title='Suporte Técnico')
fig.show()

#$ IQR
q1 = df['A'].quantile(0.25)
q3 = df['A'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# $$ laço com IQR
 
diqr = pd.DataFrame(columns=['min', 'max', 'upper_bound'])

for campo in df.columns:
    q1 = df[campo].quantile(0.25)
    q3 = df[campo].quantile(0.75)
    iqr = q3 - q1
    # lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    diqr.loc[campo] = [df[campo].min(), df[campo].max(), upper_bound]

print(diqr)

# Remover outliers
# df = df[(df['A'] >= lower_bound) & (df['A'] <= upper_bound)]
mean_value = df['A'].mean()

#$ Z-square

#$ Transformar outliers

#$ Substituir outliers pela média ou mediana

salarios_abaixo_2milhoes = df[df['Salario_Anual'] < limiteOutlier]
salarios_abaixo_2milhoes['Salario_Anual'].median()
mediana_salario_abaixo_2milhoes = df[df['Salario_Anual'] < limiteOutlier]['Salario_Anual'].median()

#$ Transformação logarítmica
# Ajusta os valores discrepantes para uma distribuição mais uniforme.
# Deve ser usada quando os dados apresentam uma distribuição altamente assimétrica ou outliers
# Realizando engenharia de features
import numpy as np
data['log_salario'] = np.log(data['salário'] + 1)


#$ Salvar o DataFrame tratado em um novo arquivo CSV
df.to_csv("dados_outliers_tratados.CSV", index ="FALSE")
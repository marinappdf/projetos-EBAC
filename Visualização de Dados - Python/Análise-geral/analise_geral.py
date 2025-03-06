import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sem nenhum Na
df = pd.read_csv('../ecommerce_preparados_tratados.csv')
# Original
dfp = pd.read_csv('../ecommerce_preparados.csv')

# Histograma para aquecer
plt.figure(figsize=(8,5))
plt.hist(df['Desconto_MinMax'], bins=80, color='green', alpha=0.8)
plt.title('Histograma')
plt.xlabel('X')
plt.ylabel('Frequência')
plt.grid(True)
#plt.xticks(ticks=range(df['idade'].min()-5, df['idade'].max()+5,5))

plt.savefig('histograma_01.png')

# Dando uma olhada geral

# Heatmap de correlação
# Título,Nota,N_Avaliações,Desconto,Marca,Material,Gênero,
# Temporada,Review1,Review2,Review3,Qtd_Vendidos,Preço,Nota_MinMax,
# N_Avaliações_MinMax,Desconto_MinMax,Preço_MinMax,Marca_Cod,Material_Cod,
# Temporada_Cod,Qtd_Vendidos_Cod,Marca_Freq,Material_Freq

df_corr= df[['Preço_MinMax','Nota_MinMax' ,'Qtd_Vendidos_Cod','Nota_MinMax', 'Marca_Cod', 'Desconto_MinMax']].corr()

plt.figure(figsize=(10,8))
sns.heatmap(df_corr, annot=True, fmt='.2f')
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.savefig('graf-heatmap-01')

# +1: Correlação positiva – quando uma variável aumenta, a outra também aumenta na mesma proporção. Quanto mais próximo de +1, mais fortemente relacionadas de forma direta.
# 0: Nenhuma correlação – as variáveis não têm nenhuma relação linear, ou seja, a mudança de uma não afeta a outra de forma previsível.
# -1: Correlação negativa perfeita – quando uma variável aumenta, a outra diminui na mesma proporção. Quanto mais próximo de -1, mais fortemente relacionadas de forma inversa.
# Então vou buscar aprofundar a analise em variáveis que estão mais distantes de 0 e mais perto de +-1
# Exceto aquelas da diagonal, que são um auto correlação.
# Vou escolher aqueles com as maiores/menores correlações
# Analisando o mapa de calor da correlação entre variáveis, escolho analisar as variáveis:
# Preço MinMax
# Preço MinMax v.s. Marca_Cod
# Nota Min Max
# Desconto Minmax
# Nota Min Max v.s. Desconto Minmax



# Countplot
# Countplot com legenda
# sns.countplot(x='Qtd_Vendidos_Cod', hue='Marca_Cod', data=df)
# plt.title('Distribuição ')
# plt.xlabel('QTD vENDIDOS')
# plt.ylabel('Contagem')
# plt.legend(title='qTD VENDIDOS')
# plt.savefig('graf-countplot-01')
# plt.close()

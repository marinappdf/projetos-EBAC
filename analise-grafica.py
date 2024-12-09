
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Tratado
df = pd.read_csv('ecommerce_preparados_tratados.csv')
# Original
dfp = pd.read_csv('ecommerce_preparados.csv')

# Variáveis de interesse
# Preço MinMax
# Preço MinMax v.s. Marca_Cod
# Nota Min Max
# Desconto Minmax
# Nota Min Max v.s. Desconto Minmax

# Gráfico de Histograma
def criar_histograma(variavel, bins, nome_variavel, passo):
    plt.figure(figsize=(8,5))
    plt.hist(df[variavel], bins=int(bins)  , color='green', alpha=0.8)
    plt.title('Histograma de ' + nome_variavel)
    plt.xlabel(nome_variavel)
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.xticks(ticks=range(int(df[variavel].min())-10, int(df[variavel].max())+10,int(passo)))
    plt.savefig('histogramas/'+ nome_variavel)
    plt.close()


# criar_histograma('Desconto_MinMax', 80, "Descontos mínimos e máximos", 10)
# criar_histograma('Nota_MinMax',80, 'Notas máximos e mínimas', 1 )
# criar_histograma('Preço_MinMax', 80, "Preços mínimos e máximos", 10)
# criar_histograma('Marca_Cod', 80, 'Marcas por código', 1)

# Gráfico de dispersão
def criar_dispersao(x,y, nome_variavelX, nome_variavelY):
    sns.jointplot(x=x, y=y, data=df, kind='scatter',  height=10, ratio=10)
    # ['scatter', 'hist', 'hex', 'kde', 'reg', 'resid']

    plt.suptitle('Grafico de Dispersão de ' + nome_variavelX + ' por ' + nome_variavelY,
                 x=0.1, y=1.00, ha='left', fontsize=16)
    # plt.title('Grafico de Dispersão de ' + nome_variavelX + ' por '+ nome_variavelY, loc='left', pad=50)
    plt.xlabel(nome_variavelX)
    plt.ylabel(nome_variavelY)
    plt.tight_layout()
    plt.savefig('Gráficos de Dispersão/'+x + '_por_' + y + '_dispersao')
    plt.close()

# criar_dispersao('Marca_Cod', 'Preço_MinMax', 'Código da Marca', 'Preços mínimos e máximos')
# criar_dispersao('Desconto_MinMax', 'Nota_MinMax', 'Descontos mínimos e máximos', 'Notas mínimas e máximas')

# Mapa de calor
def criar_mapa_calor(a,b,c,d,e,f):
    df_corr= df[[a,b,c,d,e,f]].corr()
    sns.heatmap(df_corr, annot=True, fmt='.2f')
    plt.title('Mapa de Calor')
    plt.savefig('Mapa de calor/mapa_calor_{}_{}_{}_{}_{}_{}'.format(a,b,c,d,e,f))
    plt.close()

#criar_mapa_calor('Preço_MinMax','Nota_MinMax' ,'Qtd_Vendidos_Cod','Nota_MinMax', 'Marca_Cod', 'Desconto_MinMax')

# # Gráfico de barra
def criar_barras(variavel,nome_variavel, width,passo):
    x = df[variavel].value_counts().index
    y = df[variavel].value_counts().values
    plt.figure(figsize=(10,6))
    plt.bar(x,y, color='#330033', edgecolor='#c1aca7', width=width)
    plt.xticks(ticks=np.arange(
        df[variavel].min() - 0.1 * df[variavel].min(),  # Valores com float
        df[variavel].max() + 0.1 * df[variavel].min(),  # Valores com float
        passo ))
    plt.title('Barrar de {}'.format(nome_variavel))
    plt.xlabel(nome_variavel)
    plt.ylabel('Quantidade')
    plt.savefig('Gráfico de barras/barras-{}'.format(nome_variavel))
    plt.close()

# criar_barras('Desconto_MinMax', 'Descontos mínimos e máximos',0.01,0.05)
# criar_barras('Nota_MinMax', 'Notas mínimas e máximas',0.01,0.05)
# criar_barras('Preço_MinMax',"Preços mínimos e máximos",0.01,0.05)
# criar_barras('Marca_Cod', 'Marcas por código',1,100)

# # Gráfico de pizza
def criar_pizza(variavel, nome_variavel):
    x = df[variavel].value_counts().index
    y = df[variavel].value_counts().values
    plt.figure(figsize=(10,6))
    plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
    plt.title(nome_variavel)
    plt.savefig('Gráficos de Pizza/pizza_' + nome_variavel)
    plt.close()

# criar_pizza('Desconto', 'Descontos')
# # criar_pizza('Marca_Cod', 'Marcas por código')
# criar_pizza('Nota', 'Notas')
# criar_pizza('Preço',"Preços")

# # Gráfico de densidade
def criar_densidade(variavel, nome_variavel):
    plt.figure(figsize=(10,6))
    sns.kdeplot(df[variavel], fill=True, color='#863e9c')
    plt.title('Densidade de ' + nome_variavel)
    plt.xlabel(nome_variavel)
    plt.savefig('Gráficos de Densidade/densidade_' + nome_variavel)
    plt.close()

# criar_densidade('Desconto', 'Descontos')
# criar_densidade('Marca_Cod', 'Marcas por código')
# criar_densidade('Nota', 'Notas')
# criar_densidade('Preço',"Preços")

# # Gráfico de Regressão
def criar_regressao(x, y, nomeX, nomeY, a):
    sns.regplot(x=x, y=y, data=df, color='#278f65', scatter_kws={'alpha': a, 'color': '#34c289'})
    plt.title('Regressão de ' + nomeX + ' por ' + nomeY)
    plt.ylabel(nomeY)
    plt.xlabel(nomeX)
    plt.savefig('Gráficos de Regressão/regressao_' + nomeX + '_' + nomeY)
    plt.close()

criar_regressao('Marca_Cod', 'Preço_MinMax', 'Código da Marca', 'Preços mínimos e máximos', 0.5)
criar_regressao('Desconto_MinMax', 'Nota_MinMax', 'Descontos mínimos e máximos', 'Notas mínimas e máximas', 0.5)
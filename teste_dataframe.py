import pandas as pd

dados = {
        'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

df_dados = pd.DataFrame(dados)

print("\nInformaões do DataFrame:\n\n")
print(df_dados.info())
print("\nQuantidade de linhas e colunas:\n",df_dados.shape)
print("\nTipo de dados:\n", df_dados.dtypes)
print("\nMenor valor de cada coluna:\n",df_dados.min())
print("\nMaior valor de cada coluna:\n",df_dados.max())
print("\nMédia Aritmédica:\n",df_dados.mean())
print("\nDesvio Padrão:\n",df_dados.std())
print("\nMediana:\n",df_dados.median())
print("\n\nResumo do DataFrame:\n",df_dados.describe())

df_dados.head()

df_uma_coluna = df_dados['idades']
print(type(df_uma_coluna))
print('Média de idades = ',df_uma_coluna.mean())
print(df_uma_coluna)

colunas = ['nomes','cpfs']
df_duas_colunas = df_dados[colunas]
print(type(df_duas_colunas))
print(df_duas_colunas)

import pandas as pd

df = pd.read_json('vendas_ecommerce.json')

print("Primeiras 5 linhas:")
print(df.head())

print("Tipos de dados:")
print(df.dtypes)

print("Resumo:")
print(df.describe())

print("Valores nulos por coluna:")
print(df.isnull().sum())

df['valor_final'] = (df['preco_unitario'] * df['quantidade'] * (1 - df['desconto_pct'] / 100)).round(2)

colunas_visualizar = ['produto', 'quantidade', 'preco_unitario', 'desconto_pct', 'valor_final']
print(df[colunas_visualizar].head())

maior_desconto = df.loc[df['desconto_pct'].idxmax()]
print(f"Valor final do maior desconto: {maior_desconto['valor_final']}")

devolvidos = df[df['status'] == 'devolvido'][['cliente', 'produto', 'valor_final']]

eletronicos_top = df[(df['categoria'] == 'Eletrônicos') & (df['avaliacao'] == 5)]

filtro_especifico = df[(df['desconto_pct'] > 15) & (df['valor_final'] > 300)]

pedido_max = df.loc[df['valor_final'].idxmax()]

qtd_sp = len(df[df['estado'] == 'SP'])

total_devolvidos = len(df[df['status'] == 'devolvido'])
porcentagem_devolvidos = (total_devolvidos / len(df)) * 100

receita_cat = df.groupby('categoria')['valor_final'].sum().sort_values(ascending=False)

aval_pagamento = df.groupby('metodo_pagamento')['avaliacao'].mean()

pedidos_estado = df.groupby('estado').size()

idade_cat = df.groupby('categoria')['idade_cliente'].mean()

ticket_medio = df.groupby('categoria')['valor_final'].mean().sort_values(ascending=False)

df['data'] = pd.to_datetime(df['data'])
df['mes'] = df['data'].dt.month

vendas_mes = df.groupby('mes')['valor_final'].sum()

ticket_mes = df.groupby('mes')['valor_final'].mean()

mes_pico = df.groupby('mes').size().idxmax()

#1 Após explorar: qual coluna tem o maior valor máximo? E qual a média de avaliacao?
#a coluna com maior valor máximo é o preco_unitário e a média de avalição é 4.34

#2 Qual o valor_final do pedido de maior desconto percentual?
#30% e valor final: 419.93

#3 Quantos pedidos foram devolvidos no total? Qual a porcentagem em relação ao total?
#2

#4 Qual categoria gerou mais receita? Qual gerou menos? Existe alguma surpresa nos resultados?
#Eletronicos gerou mais, livros gerou menos

#5 s vendas cresceram ao longo dos meses? O que os dados sugerem?
#As vendas crescem pouco e no último mês cai



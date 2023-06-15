import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

plt.style.use("seaborn")

arq = files.upload()
df = pd.read_excel("AdventureWorks.xlsx")

df.head()
df.shape
df.dtypes

#Receita total
df["Valor Venda"].sum()

#Custo total
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna de custo
df.head(1)

round(df["custo"].sum(), 2)

df["lucro"]  = df["Valor Venda"] - df["custo"] 
df.head(1)

#Lucro
round(df["lucro"].sum(),2)
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]
df.head(1)

#Media tempo de envio por marca
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
df.head(1)

#Tipo de coluna tempo_envio
df["Tempo_envio"].dtype

#Verificando se existe dados faltantes
df.isnull().sum()

#Agrupando por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()
pd.options.display.float_format = '{:20,.2f}'.format

#Reset do index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

#total de produtos vendidos e grafico
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

#Vendas de 2009 e graficos
df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

df_2009 = df[df["Data Venda"].dt.year == 2009]
df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');
     
#
df["Tempo_envio"].describe()
plt.boxplot(df["Tempo_envio"]);
plt.hist(df["Tempo_envio"]);

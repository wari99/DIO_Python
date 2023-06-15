#cont...
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

df5.head()

df = pd.concat([df1,df2,df3,df4,df5])
df.head()

#Visualizando dados
df["LojaID"].value_counts(ascending=False)

#Grafico de barras verticais e horizontais
df["LojaID"].value_counts(ascending=False).plot.bar()
df["LojaID"].value_counts().plot.barh()
df["LojaID"].value_counts(ascending=True).plot.barh();

#Grafico pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

#Usando matlibplot, adicionando titulo ao grafico e alterando nome nos eixos
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

#Usand matlibplot alterando a cor do grafico
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

#Alterando estilo
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();

df.groupby(df["mes_venda"])["Qtde"].sum()

#Selecionando vendas de 2019
df_2019 = df[df["Ano_Venda"] == 2019]
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum()

#grafico total vendidos por mes
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();

#Histograma
plt.hist(df["Qtde"], color="orangered");

plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]);

#Salvar em png
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()
plt.savefig("grafico QTDE x MES.png")

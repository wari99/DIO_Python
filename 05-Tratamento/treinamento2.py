import pandas as pd

#Leitura dos arquivos
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

#Exibicao 
df = pd.concat([df1,df2,df3,df4,df5])

df5.head()
df.head()
df.tail()

df.sample(5)

#Verificando tipos e alterando
df.dtypes

df["LojaID"] = df["LojaID"].astype("object")
df.dtypes
df.head()

#Consulta de linhas c valores faltantes
df.isnull().sum()


df["Vendas"].fillna(df["Vendas"].mean(), inplace = True)
df["Vendas"].mean()
df.isnull().sum()
df.sample(15)

#Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace = True)

#Apagando linhas com valores nulos
df.dropna(inplace = True)

#Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace = True)

#Retornando a maior receita e a menor
df["Receita"].max()
df["Receita"].min()

df.nlargest(3, "Receita")
df.nsmallest(3, "Receita")

#Ordenacao
df.sort_values("Receita", ascending=False).head(10)


#Filtra vendas em 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
vendas_marco_19.sample(20)
   


'''Treinamento de métodos na biblioteca Pandas'''
import pandas as pd

#Copy path de Gapminder.csv
df = pd.read_csv("/content/drive/My Drive/Datasets/Gapminder.csv", error_bad_lines=False, sep=";")

#Visualiza por padrao as 5 primeiras linhas
df.head()

#Alternado nome da linha 0, de ingles para portugues
df = df.rename(columns={"country":"Pais", "continent": "continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap": "PIB"})
df.head(10)

#Mostra total de linhas e colunas; tipos
df.shape
df.columns
df.types

#15 Ultimas linhas
df.tail(15)

#Calcula estatisticas descritivas
df.describe()

#Retorna valores unicos da coluna continente
df["continente"].unique()

#Retornar apenas valores com continente = Oceania
Oceania = df.loc[df["continente"] == "Oceania"]
Oceania.head()

Oceania["continente"].unique()

#Agrupamento por continente
df.groupby("continente")["Pais"].nunique()

#Agrupar apenas expectativa de vida media para cada ano
df.groupby("Ano")["Expectativa de vida"].mean()

#Consultando PIB
df["PIB"].mean()
df["PIB"].sum()

#####








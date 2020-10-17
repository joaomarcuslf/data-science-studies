import requests
import pandas as pd

dados = requests.get("https://raw.githubusercontent.com/alura-cursos/imersao-dados-2-2020/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv")
arquivo = open("teste.csv","w+")
arquivo.write(dados.text)
arquivo.close()

df = pd.read_csv("teste.csv")

df.head()

media1 = df['NU_IDADE'].mean()
soma1 = df['NU_IDADE'].sum()
maximo1 = df['NU_IDADE'].max()
minimo1 = df['NU_IDADE'].min()
contagem1 = df['NU_IDADE'].count()
mediana1 = df['NU_IDADE'].median()
padrao1 = df['NU_IDADE'].std()
variancia1 = df['NU_IDADE'].var()

print ('Média Idade: ' + str(media1))
print ('Som of idades: ' + str(soma1))
print ('Máximo Idade: ' + str(maximo1))
print ('Mínimo Idade: ' + str(minimo1))
print ('Contagem de idades: ' + str(contagem1))
print ('Mediana Idade: ' + str(mediana1))
print ('adrão de idades: ' + str(padrao1))
print ('Variância de idades: ' + str(variancia1))

agrupar_soma1 = df.groupby(['CO_MUNICIPIO_RESIDENCIA']).sum()
agrupar_contagem1 = df.groupby(['CO_MUNICIPIO_RESIDENCIA']).count()

print ('Soma de valores, agrupados por código municipio: ' + str(agrupar_soma1))
print ('Contagem de valores, agrupados por código municipio: ' + str(agrupar_contagem1))
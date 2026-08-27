import pandas as pd

dados = pd.read_csv('dados.csv')

df = pd.DataFrame(dados)

media = df['Idade'].mean()
print(media)

mediana = df['Idade'].median()
print(df.describe())

d_user = df[df['Nome'] == 'Carlos']
info_ = df.info()

agregacao = df.groupby('Cidade') ['Idade'].mean()

print(info_)
print('Usuário : ',d_user)
print('media', media)
print('mediana',mediana)
print(agregacao)


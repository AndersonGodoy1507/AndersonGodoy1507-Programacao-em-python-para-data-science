import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dados =  pd.read_csv('dados_estudantes.csv')

df= pd.DataFrame(dados)
grupo_g_e = df.groupby('gender')['exam_score'].sum()
plt.figure(figsize=(7, 7))
plt.pie(grupo_g_e, labels = grupo_g_e.index, autopct='%1.1f%%')
plt.show()



plt.figure(figsize = (8,12))
plt.scatter(df['study_hours_per_day'],df['exam_score'])
plt.show()




plt.figure(figsize = (10,10))
plt.scatter(df['exam_score'],df['age'])
plt.show()

# media_de_horas =(df['study_hours_per_day'],df['exam_score']).sum()
# print(media_de_horas)


# df= pd.DataFrame(dados)
# plt.figure(figsize=(7, 7))
# plt.pieplt.pie(media_de_horas, labels = media_de_horas.index, autopct='%1.1f%%')

plt.figure(figsize = (10,10))
plt.bar(df['exam_score'],df['age'])
plt.show()


plt.figure(figsize = (10,10))
plt.scatter(df['exam_score'],df['age'])
plt.show()
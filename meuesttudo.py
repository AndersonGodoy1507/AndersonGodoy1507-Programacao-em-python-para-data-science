
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

# ml

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


df=  pd.read_csv("diabetes2.csv")
print(df)

# interface grafica

root = tk.Tk()
root.title('Risco de Diabetes')
root.geometry('2000x1700')

frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=20, fill=tk.BOTH, expand=True)

frame_resultados =  tk.Frame(root)
frame_resultados.pack(pady = 10)

frame_controle  =  tk.Frame(root)
frame_controle.pack(pady=10)

label_tendencia =  tk.Label(frame_resultados, text='', justify=tk.CENTER)
label_tendencia.pack()

label_descricao = tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_descricao.pack()

label_previsao = tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_previsao.pack()





# limpando 
def limpar_frame():
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    # 2. Reseta o texto de todas as labels informativas
    label_tendencia.config(text='')
    label_descricao.config(text='')
    label_previsao.config(text='')

    # 3. Libera as figuras do Matplotlib da memória
    plt.close('all')

# funçoes de analise
def grafico_brarra():
    limpar_frame()
    fig, ax =  plt.subplots(figsize = (8,5))

    risco_imc_idade =  df.groupby('idade','imc')['em_risco_diabetee'].mean() * 100
    risco_imc_idade.plot(kind='bar', color = ['blue','green','yellow'], ax=ax) 

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, expand=True)
        
    ax.set_title('SOBREVIVENTES POR CLASSE')
    ax.set_ylabel('Porcentagem ')
    ax.set_xlabel('Classe dos Sobreviventes')
        
    insight =  'Passageiros da 1º Classe tiveram maior taxa de sobrevivência'        
    label_tendencia.config(text= insight, ) 


# botao

btn_barras  = ttk.Button(frame_controle, text= 'Grafico de barras', command=grafico_brarra)
btn_barras.grid(row = 0, padx= 5, pady=5)

# btn_linhas  = ttk.Button(frame_controle, text= 'Grafico de linhas', command=mostrar_linhas)
# btn_linhas.grid(row = 1, padx= 5, pady=5)

# btn_pizza  = ttk.Button(frame_controle, text= 'Grafico de Pizza', command= mostrar_pizza)
# btn_pizza.grid(row = 2, padx= 5, pady=5)

# btn_tendecia  = ttk.Button(frame_controle, text= 'Medida de tendência', command=mostrar_tendencia)
# btn_tendecia.grid(row = 3, padx= 5, pady=5)

# btn_descricao = ttk.Button(frame_controle, text= 'Descrição', command=descricao)
# btn_descricao.grid(row = 4, padx= 5, pady=5)

# btn_previsao  = ttk.Button(frame_controle, text= 'Previsão', command=previsao)
# btn_previsao.grid(row = 5, padx= 5, pady=5)










root.mainloop()
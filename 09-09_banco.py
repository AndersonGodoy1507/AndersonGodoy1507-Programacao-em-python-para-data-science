# ATIVIDADE 3 

# CRIAR BANCO DE DADOS 3

# Você foi contratado para criar um sistema de biblioteca usando 
# SQLite + Tkinter + Matplotlib. O sistema precisa gerenciar livros e gerar relatórios.

#             id INTEGER PRIMARY KEY 
#             titulo TEXT, 
#             autor TEXT,  
#             ano INTEGER,
#             genero TEXT,
#             paginas INTEGER

import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

conexao = sqlite3.connect('banco_biblioteca')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS livros(
           
           id INTEGER PRIMARY KEY,
           titulo TEXT,
           autor TEXT,
           genero TEXT,
           paginas INTEGER
           ano INTERGER
           )''')

conexao.commit()



def inserir_dados():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    genero = entrada_genero.get()
    pagina = entrada_pagina.get()
    ano = entrada_ano.get()

    

    try:

        cursor.execute('INSERT INTO livros (titulo,autor,genero,paginas,ano) values (?,?,?,?,?)',(titulo,autor,genero,pagina,ano),)
        conexao.commit()
        messagebox.showinfo('', 'dados inseridos!')
        entrada_titulo.delete(0,'end')
        entrada_autor(0, 'end')
        entrada_genero.delete(0,'end')
        entrada_pagina.delete(0,'end')
        entrada_ano.delete(0,'end')
    except Exception as e:
        messagebox.showerror("", f"Erro: {e}")







# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Livros")

# Rótulos e campos de entrada
tk.Label(janela, text="Título:").grid(row=0, column=0, padx=10, pady=5)
entrada_titulo = tk.Entry(janela)
entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Autor:").grid(row=1, column=0, padx=10, pady=5)
entrada_autor = tk.Entry(janela)
entrada_autor.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Genero:").grid(row=2, column=0, padx=10, pady=5)
entrada_genero = tk.Entry(janela)
entrada_genero.grid(row=2, column=1, padx=10, pady=5)


tk.Label(janela, text="Página:").grid(row=3, column=0, padx=10, pady=5)
entrada_pagina = tk.Entry(janela)
entrada_pagina.grid(row=3, column=1, padx=10, pady=5)

tk.Label(janela, text="Ano Lançamento").grid(row=4, column=0, padx=10, pady=5)
entrada_ano = tk.Entry(janela)
entrada_ano.grid(row=4, column=1, padx=10, pady=5)

# Botões
btn_inserir = tk.Button(janela, text="Inserir Dados",command=inserir_dados)
btn_inserir.grid(row=5, column=0, columnspan=2, pady=10)

# btn_retirar = tk.Button(janela, text="Retirar", command=exibir_grafico)
# btn_retirar.grid(row=4, column=0, columnspan=2, pady=10)

# btn_gerar_relatorio = tk.Button(janela, text="Relatorio", command=exibir_grafico)
# btn_gerar_relatorio.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar o loop da aplicação
janela.mainloop()

# Fechar a conexão ao banco de dados quando a janela for fechada
conexao.close()

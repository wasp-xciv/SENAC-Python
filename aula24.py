#GRID

import tkinter as tk

janela = tk.Tk()
janela.resizable(False,False)
janela.title("Exemplo de Grid")

#Rótulo na Linha 0, Coluna 0
rotulo1 = tk.Label(janela, text="Linha 0, Coluna 0", bg="lightgreen")
rotulo1.grid(row=0,column=0)

#Botão na linha 1, coluna 0
botao1 = tk.Button(janela, text="Linha 1, Coluna 0",bg="lightyellow")
botao1.grid(row=1,column=0)

#Botão na linha 0, coluna 1
botao2 = tk.Button(janela, text="Linha 0, Coluna 1",bg="lightpink")
botao2.grid(row=0,column=1)

#Rótulo na linha 1, coluna 1 e se estende para a direção Leste (E)
rotulo2 = tk.Label(janela, text="Linha 1, Coluna 1", bg="lightgray")
rotulo2.grid(row=1,column=1,sticky="E")

#Botão na linha 1, coluna 2
botao3 = tk.Button(janela, text="Linha 1, Coluna 2",bg="lightcoral")
botao3.grid(row=1,column=2)

#Rótulo na linha 0, coluna 2
rotulo3 = tk.Label(janela, text="Linha 0, Coluna 2", bg="black",fg="white")
rotulo3.grid(row=0,column=2,sticky="W")

#Rótulo na linha 2, coluna 0
rotulo4 = tk.Label(janela, text="Linha 2, Coluna 0", bg="lightblue")
rotulo4.grid(row=2,column=0)

#Botão na linha 2, coluna 1
botao4 = tk.Button(janela, text="Linha 2, Coluna 1",bg="purple",fg="white")
botao4.grid(row=2,column=1)

#Rótulo na linha 2, coluna 2
rotulo5 = tk.Label(janela, text="Linha 2, Coluna 2", bg="orange")
rotulo5.grid(row=2,column=2)

#Botão na linha 0, coluna 3
botao5 = tk.Button(janela, text="Linha 0, Coluna 3",bg="green",fg="white")
botao5.grid(row=0,column=3)

#Rótulo na linha 1, coluna 3
rotulo6 = tk.Label(janela, text="Linha 1, Coluna 3", bg="blue",fg="white")
rotulo6.grid(row=1,column=3)

#Botão na linha 2, coluna 3
botao6 = tk.Button(janela, text="Linha 2, Coluna 3",bg="red",fg="white")
botao6.grid(row=2,column=3)

#Botão na linha 3, coluna 0
botao7 = tk.Button(janela, text="Linha 3, Coluna 0",bg="yellow")
botao7.grid(row=3,column=0)

#Rótulo na linha 3, coluna 1
rotulo7 = tk.Label(janela, text="Linha 3, Coluna 1", bg="lightgray")
rotulo7.grid(row=3,column=1)

#Botão na linha 3, coluna 2
botao8 = tk.Button(janela, text="Linha 3, Coluna 2",bg="lightblue")
botao8.grid(row=3,column=2)

#rótulo na linha 3, coluna 3
rotulo8 = tk.Label(janela, text="Linha 3, Coluna 3", bg="lightgreen")
rotulo8.grid(row=3,column=3)

janela.mainloop()

#check ttkbootstrap para novas opções de temas e paletas de cores

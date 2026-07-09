import tkinter

janela = tkinter.Tk()   #'tkinter' é a biblioteca. Tk é a classe.

"""
Para definir as dimensões em pixels:"""
janela.geometry("800x600")
janela.resizable(False,False)
"""
Para definir o nome da janela:"""
janela.title("PetLink - Version 1.0.0")

"""
Personalizar a janela - Cores"""
janela.configure(bg="#734673")

"""
Criação de rótulo/label:"""
rotulo = tkinter.Label(janela,text="🐕‍🦺PetLink🐈",font=("Courier",40),bg="#467373",fg="#E4D3E4")
rotulo.pack(fill=tkinter.X,pady=30)
rotulo2 = tkinter.Label(janela,text="Sistema de Pet Sitters",font=("Courier",15,"bold"),bg="#734673",fg="#E4D3E4")
rotulo2.pack(pady=10)

"""
Criação de botão:"""
botao1 = tkinter.Button(janela,text="Cadastrar Tutor",font=("Courier",10),bg="#F5EFF5")
botao1.pack(fill=tkinter.X,pady=5,padx=100)
botao2 = tkinter.Button(janela,text="Cadastrar Pet Sitter",font=("Courier",10),bg="#F5EFF5")
botao2.pack(fill=tkinter.X,pady=5,padx=100)
botao3 = tkinter.Button(janela,text="Cadastrar Animal",font=("Courier",10),bg="#F5EFF5")
botao3.pack(fill=tkinter.X,pady=5,padx=100)
botao4 = tkinter.Button(janela,text="Buscar Pet Sitter",font=("Courier",10),bg="#F5EFF5")
botao4.pack(fill=tkinter.X,pady=5,padx=100)
botao5 = tkinter.Button(janela,text="Agendar Serviços",font=("Courier",10),bg="#F5EFF5")
botao5.pack(fill=tkinter.X,pady=5,padx=100)
botao6 = tkinter.Button(janela,text="Avaliar Serviços",font=("Courier",10),bg="#F5EFF5")
botao6.pack(fill=tkinter.X,pady=5,padx=100)
botao7 = tkinter.Button(janela,text="Listar Agendamentos",font=("Courier",10),bg="#F5EFF5")
botao7.pack(fill=tkinter.X,pady=5,padx=100)
botao8 = tkinter.Button(janela,text="Fechar",font=("Courier",10),bg="#F5EFF5",command=janela.destroy)
botao8.pack(fill=tkinter.X,pady=5,padx=100)

"""
Para manter o programa rodando, é necessário criar um loop:"""
janela.mainloop()   #abre para visitantes
# import tkinter

# janela = tkinter.Tk()   #'tkinter' é a biblioteca. Tk é a classe.

# """
# Para definir as dimensões em pixels:"""
# janela.geometry("800x600")
# janela.resizable(False,False)   #esse comando impede que a largura e altura sejam modificada, trancando no padrão 800x600 estipulado.
# """
# Para definir o nome da janela:"""
# janela.title("PetLink - Version 1.0.0")

# """
# Personalizar a janela - Cores"""
# janela.configure(bg="#734673")

# """
# Criação de rótulo/label:"""
# rotulo = tkinter.Label(janela,text="🐕‍🦺PetLink🐈",font=("Courier",40),bg="#467373",fg="#E4D3E4")
# rotulo.pack(fill=tkinter.X,pady=170)
# rotulo2 = tkinter.Label(janela,text="Bem-vindo!(＾Ｕ＾)ノ~ＹＯ",font=("Courier",15,"bold"),bg="#734673",fg="#E4D3E4")
# rotulo2.pack(pady=10)

# """
# Criação de botão:"""
# botao1 = tkinter.Button(janela,text="Tutor",font=("Courier",10),bg="#F5EFF5")
# botao1.pack(fill=tkinter.X,pady=5,padx=100)
# botao2 = tkinter.Button(janela,text="Pet-Sitter",font=("Courier",10),bg="#F5EFF5")
# botao2.pack(fill=tkinter.X,pady=5,padx=100)
# botao3 = tkinter.Button(janela,text="Fechar",font=("Courier",10),bg="#F5EFF5",command=janela.destroy)
# botao3.pack(fill=tkinter.X,pady=5,padx=100)

# """
# Para manter o programa rodando, é necessário criar um loop:"""
# janela.mainloop()   #abre para visitantes

###############################################################################DESAFIO
import tkinter

janela = tkinter.Tk()
janela.geometry("250x350")
janela.resizable(False,False)
janela.title("Desafio")
janela.configure(bg="#F3F2F2")
rotulo=tkinter.Label(janela,text="DASHBOARD",font=("Arial",20,"bold"),bg="#616161",fg="#000000")
rotulo.pack(fill=tkinter.X,pady=30)
botao1=tkinter.Button(janela,text="Relatórios",bg="#F3F2F2")
botao1.pack(fill=tkinter.X,pady=5,padx=30)
botao2=tkinter.Button(janela,text="Vendas",bg="#F3F2F2")
botao2.pack(fill=tkinter.X,pady=5,padx=30)
botao3=tkinter.Button(janela,text="Estoque",bg="#F3F2F2")
botao3.pack(fill=tkinter.X,pady=5,padx=30)
botao4=tkinter.Button(janela,text="Configurações",bg="#F3F2F2")
botao4.pack(fill=tkinter.X,pady=5,padx=30)
botao5=tkinter.Button(janela,text="Sair",bg="#F3F2F2",fg="#E31717",command=janela.destroy)
botao5.pack(fill=tkinter.X,pady=30,padx=100)
janela.mainloop()
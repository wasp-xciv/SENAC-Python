#Posicionamento do Widget - Coordenada X,Y.
#place() - define a posição do widget
import tkinter as tk
janela = tk.Tk()
janela.title("Exemplo 2 - Place")
janela.geometry("800x600")
janela.resizable(False,False)
rotulo = tk.Label(janela,text="««««Cadastro de Cliente»»»»",font=("Courier",20,"bold"),bg="#C3ADD9",fg="#110811")
rotulo.place(x=0,y=0,width=800,height=100)

rotulo = tk.Label(janela,text="»»»» Nome:",font=("Courier",12,"bold"))        #acrescenta mais um label abaixo do primeiro
rotulo.place(x=30,y=120,width=100,height=30)
caixa_nome = tk.Entry(janela,font=("Courier",10,"bold"),fg="#110811")
caixa_nome.place(x=170,y=120,width=400,height=30)

rotulo = tk.Label(janela,text="»»»» Endereço:",font=("Courier",12,"bold"))
rotulo.place(x=30,y=160,width=140,height=30)
caixa_address = tk.Entry(janela,font=("Courier",10,"bold"),fg="#110811")
caixa_address.place(x=170,y=160,width=400,height=30)

rotulo = tk.Label(janela,text="»»»» Telefone:",font=("Courier",12,"bold"))
rotulo.place(x=30,y=200,width=140,height=30)
caixa_phone = tk.Entry(janela,font=("Courier",10,"bold"),fg="#110811")
caixa_phone.place(x=170,y=200,width=400,height=30)

rotulo = tk.Label(janela,text="»»»» E-mail:",font=("Courier",12,"bold"))
rotulo.place(x=30,y=240,width=110,height=30)
caixa_address = tk.Entry(janela,font=("Courier",10,"bold"),fg="#110811")
caixa_address.place(x=170,y=240,width=400,height=30)

rotulo = tk.Label(janela,text="»»»» CPF:",font=("Courier",12,"bold"))
rotulo.place(x=30,y=280,width=80,height=30)
caixa_address = tk.Entry(janela,font=("Courier",10,"bold"),fg="#110811")
caixa_address.place(x=170,y=280,width=400,height=30)

botao1 = tk.Button(janela,text="Salvar",font=("Courier",10,"bold"),bg="#F5EFF5")
botao1.place(x=30, y=550, width = 100, height=30)
botao2 = tk.Button(janela,text="Editar", font=("Courier",10,"bold"),bg="#D9ADD9")
botao2.place(x=150,y=550,width=100,height=30)
botao3 = tk.Button(janela,text="Excluir", font=("Courier",10,"bold"),bg="#BD70BD")
botao3.place(x=270,y=550,width=100,height=30)

janela.mainloop()
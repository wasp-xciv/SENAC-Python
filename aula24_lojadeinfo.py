import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

produtos = [
    {"nome":"Notebook Dell i5","cat":"Notebooks","preco":3299.90,"estoque":5},
    {"nome":"Mouse Logitech MX","cat":"Periféricos","preco":349.90,"estoque":20},
    {"nome":"SSD Kingston 1TB","cat":"Armazenamento","preco":419.90,"estoque":12},
    {"nome":"Monitor LG 24","cat":"Monitores","preco":1199.90,"estoque":8},
    {"nome":"Teclado Mecânico","cat":"Periféricos","preco":289.90,"estoque":15},
    {"nome":"Memória RAM 16GB","cat":"Componentes","preco":259.90,"estoque":30},
]

#temas = ["superhero","darkly","solar","flatly","cyborg","minty"]
root = tb.Window(themename="lumen")
root.title("TechStore - Catálogo")
root.geometry("600x430")

#FILTROS-------------------------------------------------
frame_filtro = tk.Frame(root,bg="#E7F8FE",pady=8)
frame_filtro.pack(fill="x")

tk.Label(frame_filtro,text = "Buscar:",bg="#E7F8FE").pack(side="left",padx=8)
entry_busca = tk.Entry(frame_filtro, width=20)
entry_busca.pack(side="left",padx=5)

cats = ["Todos"] +sorted({p["cat"] for p in produtos})
var_cat = tk.StringVar(value="Todos")
ttk.Combobox(frame_filtro,textvariable=var_cat,values=cats,width=14,state="readonly").pack(side="left",padx=8)
##Combobox se trata da criação de um submenu de categorias. O "sorted" coloca as categorias em ordem alfabética
tk.Button(frame_filtro,text="Filtrar",command=lambda:filtrar()).pack(side="left",padx=5)

#Tabela (Preview) -------------------------------------------
cols = ("Produto","Categoria","Preço","Estoque")
tree = ttk.Treeview(root,columns=cols,show="headings",height=10)

for c in cols:
    tree.heading(c,text=c)
    tree.column(c,width=130 if c == "Produto" else 100)
tree.pack(fill="x",padx=10,pady=8)

def popular(lista):
    tree.delete(*tree.get_children())
    for p in lista:
        tree.insert("","end",values=(
            p["nome"],p["cat"],
            f"R${p['preco']:.2f}",p["estoque"]))


def filtrar():
    termo = entry_busca.get().lower()
    cat = var_cat.get()
    res = [p for p in produtos
           if termo in p["nome"].lower() and (cat == "Todos" or p["cat"] == cat)]
    popular(res)

popular(produtos) ##carrega todos ao iniciar o programa

#Rodapé--------------------------------------------------
label_info = tk.Label(root,text="Selecione um produto para ver detalhes",fg="gray",font=("Arial",9))
label_info.pack(pady=4)

def on_select(event):
    sel = tree.selection()
    if sel:
        vals = tree.item(sel[0])["values"]
        label_info.config(text=f"📦 {vals[0]} | {vals[1]} | {vals[2]} | Estoque:{vals[3]} un.")

tree.bind("<<TreeviewSelect>>", on_select)
root.mainloop()

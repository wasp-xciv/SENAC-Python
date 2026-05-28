#Matrizes: Listas dentro de Listas

# Selecione a linha: use o primeiro índice para a lista
# Selecione a coluna: use o segundo índice para o elemento
#      0   1
# 0  | 1   2
# 1  | 3   4

# matriz = ([1,2],[3,4])

# #Atividade - Lista de compras:

# lista_compras = []

# while True:
#     print("\n--- Lista de Compras ---\n"
#           "1 - Adicionar item\n"
#           "2 - Remover item\n"
#           "3 - Mostrar lista\n"
#           "4 - Sair")
#     option = input("Escolha uma opção:\n")

#     if option == "1":
#         item = input("\nDigite o item:\n")
#         lista_compras.append(item)
#         print(f"{item} adicionado! (●'◡'●)")
#         add = input("Deseja adicionar mais itens?\nS/N: ").strip().upper()[0]
#         while add != "N":
#             item = input("\nDigite o item:\n")
#             lista_compras.append(item)
#             print(f"{item} adicionado! (●'◡'●)")
#             add = input("Deseja adicionar mais itens?\nS/N: ").strip().upper()[0]
#             if add != "S":
#                 break
#     elif option == "2":
#         for l in range(len(lista_compras)):
#             print(f"{l} - {lista_compras[l]}")
#         item = input("Digite um item para remover:\n")
#         if item in lista_compras:
#             lista_compras.remove(item)
#             print(f"{item} removido! (●'◡'●)")
#             add = input("Deseja remover mais itens?\nS/N: ").strip().upper()[0]
#             while add != "N":
#                 for l in range(len(lista_compras)):
#                     print(f"{l} - {lista_compras[l]}")
#                 item = input("Digite um item para remover:\n")
#                 if item in lista_compras:
#                     lista_compras.remove(item)
#                     print(f"{item} removido! (●'◡'●)")
#                 add = input("Deseja remover mais itens?\nS/N: ").strip().upper()[0]
#                 if add != "S":
#                     break
#         else:
#             print("Item não encontrado (；′⌒`)")
#     elif option == "3":
#         print("Sua lista de compras:\n")
#         for l in range(len(lista_compras)):
#             print(f"{l} - {lista_compras[l]}")
#     elif option == "4":
#         print("Saindo... ヾ(•ω•`)o")
#         break
#     else:
#         print("Opção inválida! （︶^︶）")


#Atividade 2:

produtos = []

while True:
    print("\n---Loja de Eletrônicos---\n"
          "1 - Cadastrar produto\n"
          "2 - Listar produtos\n"
          "3 - Vender produtos\n"   #
          "4 - Mostrar estoque\n"
          "5 - Sair")
    print()
    option = input("Escolha uma opção:\n")

    if option == "1":
        nome = input("\nNome do produto: ")
        preco = float(input("\nPreço: "))
        estoque = int(input("\nQuantidade em estoque: "))
        produtos.append([nome,preco,estoque])
        print(f"{nome} cadastrado com sucesso ☆*: .｡. o(≧▽≦)o .｡.:*☆")

    elif option == "2":
        print("\n---Produtos Cadastrados---\n")
        for p in produtos:
            print(f"Produto: {p[0]} | Preço: R${p[1]} | Estoque: {p[2]}")
            print()
    
    elif option == "3":
        nome = input("Digite o nome do produto para vender:\n")
        encontrado = False
        for p in produtos:
            if p[0] == nome:
                encontrado = True
                if p[2] > 0:
                    p[2] -= 1
                    print(f"Venda realizada! {nome} agora tem {p[2]} unidades.")
                else:
                    print("Produto sem estoque! (；′⌒`)")
                break
        if not encontrado:
            print("Produto não encontrado! （︶^︶）")
        
    elif option == "4":
        total_itens = sum([p[2] for p in produtos])
        print(f"Total de itens em estoque: {total_itens}")
    
    elif option == "5":
        print("Saindo... ヾ(•ω•`)o")
        break

    else:
        print("Opção Inválida! ╰（‵□′）╯")
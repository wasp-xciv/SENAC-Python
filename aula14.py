#Matrizes: Listas dentro de Listas

# Selecione a linha: use o primeiro índice para a lista
# Selecione a coluna: use o segundo índice para o elemento
#      0   1
# 0  | 1   2
# 1  | 3   4

matriz = ([1,2],[3,4])

#Atividade - Lista de compras:

lista_compras = []

while True:
    print("\n--- Lista de Compras ---\n"
          "1 - Adicionar item\n"
          "2 - Remover item\n"
          "3 - Mostrar lista\n"
          "4 - Sair")
    option = input("Escolha uma opção:\n")

    if option == "1":
        item = input("\nDigite o item:\n")
        lista_compras.append(item)
        print(f"{item} adicionado! (●'◡'●)")
        add = input("Deseja adicionar mais itens?\nS/N: ").strip().upper()[0]
        while add != "N":
            item = input("\nDigite o item:\n")
            lista_compras.append(item)
            print(f"{item} adicionado! (●'◡'●)")
            add = input("Deseja adicionar mais itens?\nS/N: ").strip().upper()[0]
            if add != "S":
                break
    elif option == "2":
        for l in range(len(lista_compras)):
            print(f"{l} - {lista_compras[l]}")
        item = input("Digite um item para remover:\n")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} removido! (●'◡'●)")
            add = input("Deseja remover mais itens?\nS/N: ").strip().upper()[0]
            while add != "N":
                for l in range(len(lista_compras)):
                    print(f"{l} - {lista_compras[l]}")
                item = input("Digite um item para remover:\n")
                if item in lista_compras:
                    lista_compras.remove(item)
                    print(f"{item} removido! (●'◡'●)")
                add = input("Deseja remover mais itens?\nS/N: ").strip().upper()[0]
                if add != "S":
                    break
        else:
            print("Item não encontrado (；′⌒`)")
    elif option == "3":
        print("Sua lista de compras:\n")
        for l in range(len(lista_compras)):
            print(f"{l} - {lista_compras[l]}")
    elif option == "4":
        print("Saindo... ヾ(•ω•`)o")
        break
    else:
        print("Opção inválida! （︶^︶）")
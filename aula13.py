#Criar menu para produtos:

option = ""
produtos = []
cod_produtos = []

while option != "0":
    print(f"=== Menu Inventário ===\n"
          "1 - Cadastrar produtos:\n"
          "2 - Listar produtos:\n"
          "3 - Editar prodrutos:\n"
          "4 - Excluir produtos:\n"
          "5 - Sair")
    option = input("Bem vindo! Escolha uma opção:\n")
    if option == "1":
        print(f"\n1 - Cadastrar produto:")

        prod = input("Digite o nome do produto: ")
        cod = input("Digite o código: ")

        if prod == "":
            print("=== Nome não pode ser vazio! ===")
        else:
            produtos.append(prod)
            cod_produtos.append(cod)
            print("\n=== Produto cadastrado com sucesso! ===")
            # new = (input("Deseja cadastrar mais algum produto?(s/n): "))
            
    elif option == "2":
        print(f"\n2 - Listar produtos")
        if len(produtos) == 0:
            print("=== Nenhum produto cadastrado! ===")
        else:
            for p in range(len(produtos)):
                print(f"{p} - {produtos[p]}\nCódigo do produto: {cod_produtos[p]}")
            print()
    
    elif option == "3":
        print("\n3 - Editar produtos:")
        if len(produtos) == 0:
            print("=== Nenhum produto para editar! ===")
        else:
            for p in range(len(produtos)):
                print(f"{p} - {produtos[p]}")
            
            try:
                indice = int(input("Digite o número do produto:\n"))
                if indice <0 or indice >= len(produtos):
                    print("=== Índice Inválido ===")
                else:
                    novo_prod = input("Novo nome (Enter para manter):\n")
                    novo_cod = input("Novo código do produto (Enter para manter):\n")

                    if novo_prod != "":
                        produtos[indice] = novo_prod
                    if novo_cod != "":
                        cod_produtos[indice] = novo_cod
                    print("=== Produto atualizado com sucesso! ===")
            
            except ValueError:
                print("=== Digite um número válido!")
            print()

    elif option == "4":
        print("\n4 - Excluir produtos:")
        if len(produtos) == 0:
            print("=== Não há produtos para excluir! ===")
        else:
            for p in range(len(produtos)):
                print(f"{p} - {produtos[p]}")
            try:
                indice = int(input("Digite o número do produto: "))
                if indice < 0 or indice >= len(produtos):
                    print("=== Índice Inválido!")
                else:
                    produtos.pop(indice)
                    cod_produtos.pop(indice)
                    print("=== Cliente excluído com sucesso! ===")
            except ValueError:
                print("=== Digite um número válido! ===")
            print()

    elif option == "5":
        print("\n=== Programa Encerrado! ===")
else:
    print("=== Opção inválida. Tente novamente! ===")
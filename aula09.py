# # #Criar um menu:
# option = ""
# cliente_cadastrado = False
# while option != "0":
#     print("=== MENU CLIENTE ===\n1 - Cadastrar cliente\n2 - Listar cliente\n3 - Editar cliente\n4 - Excluir cliente\n0 - Sair")
#     option = input("\nEscolha uma opção: ")
#     if option == "1":
#         print("\n1 - Cadastrar cliente")
#         cad = input("\nDigite seu nome completo: ")
#         phone_number = (input(f"\nBem vindo, {cad}.\nContato: "))
#         email = input ("\nAgora insira seu email: ")
#         address = input("\nDigite seu endereço: ")
#         print("\n=== Cliente cadastrado com sucesso! ☆*: .｡. o(≧▽≦)o .｡.:*☆ ===")
#         print()
#         cliente_cadastrado = True
#     elif option == "2":
#         print("\n2 - Listar cliente:")
#         if cliente_cadastrado == True:
#             # record = "\nCliente 666: " + cad + "\n"
#             # record = record + "\nContato: " + str(phone_number) + "\n"
#             # record = record + "\nEmail: " + str(email) + "\n"
#             # record = record + "\nEndereço: " + str(address)
#             print(cad,phone_number,email,address,sep="\n")
#         else:
#             print("=== Cliente não cadastrado (；′⌒`) ===")
#         print()
#     elif option == "3":
#         print("\n3 - Editar cliente")
#         if cliente_cadastrado:
#             record2 = input("\nAlterar:\n1 - Nome\n2 - Contato\n3 - Email\n4 - Endereço\n0 - Sair\n")
#             if record2 == "1":
#                 newcad = input("\nDigite novo nome ou aperte Enter para sair: ")
#                 if newcad != "":
#                     cad = newcad
#                 else:
#                     cad = cad
#             elif record2 == "2":
#                 new_phone_number = input("\nDigite o novo contato ou Enter para sair: ")
#                 if new_phone_number != "":
#                     phone_number = new_phone_number
#                 else:
#                     phone_number = phone_number
#             elif record2 == "3":
#                 new_email = input("\nDigite o novo email ou aperte Enter para sair: ")
#                 if new_email != "":
#                     email = new_email
#                 else:
#                     email = email
#             elif record2 == "4":
#                 new_address = input("\nDigite novo endereço ou aperte enter para sair: ")
#                 if new_address != "":
#                     address = new_address
#                 else:
#                     address = address
#         else:
#             print("=== Não há clientes para editar ===")
#             print()
#     elif option == "4":
#         print("\n4 - Excluir cliente")
#         if cliente_cadastrado:
#             confirm = input("\nConfirme: (S/N): ").strip().upper()[0]
#             if confirm == "S":
#                 cad = ""
#                 phone_number = ""
#                 email = ""
#                 address = ""
#                 cliente_cadastrado = False
#                 print("\n=== Cadastro excluído ===")
#                 print()
#             else:
#                 print("\n=== Exclusão cancelada ===")
#                 print()
#         else:
#             print("=== Cliente não cadastrado ===")
#             print()        
#     elif option == "0":
#         print("\nPrograma encerrado.")
#     else:
#         print("Opção inválida. Tente novamente.")

#************************************************

option = ""
produto_cadastrado = False
while option != "0":
    print("=== CADASTRO DE PRODUTO ===\n1 - Cadastrar produto\n2 - Listar produto\n3 - Editar produto\n4 - Excluir produto\n0 - Sair")
    option = input("\nEscolha uma opção: ")
    if option == "1":
        print("\n1 - Cadastrar produto")
        cad = input("\nProduto: ")
        cod = input("\nCód do produto: ")
        quantidade = int(input("\nQuantidade: "))
        preco = float(input("\nPreço(U): "))
        print("\n=== Produto cadastrado com sucesso! ☆*: .｡. o(≧▽≦)o .｡.:*☆ ===")
        print()
        produto_cadastrado = True
    elif option == "2":
        print("\n2 - Listar produto:")
        if produto_cadastrado == True:
            # record = "\nCliente 666: " + cad + "\n"
            # record = record + "\nContato: " + str(phone_number) + "\n"
            # record = record + "\nEmail: " + str(email) + "\n"
            # record = record + "\nEndereço: " + str(address)
            print(f"{cad}\n{cod}\n{quantidade} unidades\nPreço(U):R${preco:,.2f}")
        else:
            print("=== Produto não cadastrado (；′⌒`) ===")
        print()
    elif option == "3":
        print("\n3 - Editar produto")
        if produto_cadastrado:
            record2 = input("\nAlterar:\n1 - Produto\n2 - Código\n3 - Quantidade\n4 - Preço\n0 - Sair\n")
            if record2 == "1":
                newcad = input("\nDigite novo produto ou aperte Enter para sair: ")
                if newcad != "":
                    cad = newcad
                else:
                    cad = cad
            elif record2 == "2":
                newcod = input("\nDigite o novo código ou Enter para sair: ")
                if newcod != "":
                    cod = newcod
                else:
                    cod=cod
            elif record2 == "3":
                new_quantidade = int(input("\nDigite a nova quantidade ou aperte Enter para sair: "))
                if new_quantidade != "":
                    quantidade = new_quantidade
                else:
                    quantidade=quantidade
            elif record2 == "4":
                new_preco = float(input("\nDigite novo preço ou aperte enter para sair: "))
                if new_preco != "":
                    preco = new_preco
                else:
                    preco = preco
        else:
            print("=== Não há produtos para editar ===")
            print()
    elif option == "4":
        print("\n4 - Excluir produto")
        if produto_cadastrado:
            confirm = input("\nConfirme: (S/N): ").strip().upper()[0]
            if confirm == "S":
                cad = ""
                cod = ""
                quantidade = ""
                preco = ""
                produto_cadastrado = False
                print("\n=== Cadastro excluído ===")
                print()
            else:
                print("\n=== Exclusão cancelada ===")
                print()
        else:
            print("=== Produto não cadastrado ===")
            print()        
    elif option == "0":
        print("\nPrograma encerrado.")
    else:
        print("Opção inválida. Tente novamente.")
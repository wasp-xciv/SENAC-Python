#Criar um menu:
option = ""
cliente_cadastrado = False
while option != "0":
    print("=== MENU CLIENTE ===\n1 - Cadastrar cliente\n2 - Listar cliente\n3 - Editar cliente\n4 - Excluir cliente\n0 - Sair")
    option = input("\nEscolha uma opção: ")
    if option == "1":
        print("\n1 - Cadastrar cliente")
        cad = input("\nDigite seu nome completo: ")
        phone_number = (input(f"\nBem vindo, {cad}.\nContato: "))
        email = input ("\nAgora insira seu email: ")
        address = input("\nDigite seu endereço: ")
        print("\n=== Cliente cadastrado com sucesso! ☆*: .｡. o(≧▽≦)o .｡.:*☆ ===")
        print()
        cliente_cadastrado = True
    elif option == "2":
        print("\n2 - Listar cliente:")
        if cliente_cadastrado == True:
            record = "\nCliente 666: " + cad + "\n"
            record = record + "\nContato: " + str(phone_number) + "\n"
            record = record + "\nEmail: " + str(email) + "\n"
            record = record + "\nEndereço: " + str(address)
            print(record)
        else:
            print("Cliente não cadastrado (；′⌒`)")
        print()
    elif option == "3":
        print("\n3 - Editar cliente")
        if cliente_cadastrado == True:
            record2 = input("\nAlterar:\n1 - Nome\n2 - Contato\n3 - Email\n4 - Endereço\n0 - Sair\n")
            if record2 == "1":
                newcad = input("Digite novo nome ou aperte Enter para sair: ")
                if newcad != "":
                    cad = newcad
                else:
                    cad = cad
            if record2 == "2":
                new_phone_number = input("Digite o novo contato ou Enter para sair: ")
                if new_phone_number != "":
                    phone_number = new_phone_number
                else:
                    phone_number = phone_number
            if record2 == "3":
                new_email = input("Digite o novo email ou aperte Enter para sair: ")
                if new_email != "":
                    email = new_email
                else:
                    email = email
            if record2 == "4":
                new_address = input("Digite novo endereço ou aperte enter para sair: ")
                if new_address != "":
                    address = new_address
                else:
                    address = address
        else:
            print("== Não há clientes para editar ==")
            print()
    elif option == "4":
        print("\n4 - Excluir cliente")
    elif option == "0":
        print("\n0 - Sair")
    else:
        print("Opção inválida. Tente novamente.")
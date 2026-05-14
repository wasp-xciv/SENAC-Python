#Criar um menu:
option = ""
cliente_cadastrado = False
while option != "0":
    print("=== MENU CLIENTE ===\n1 - Cadastrar cliente\n2 - Listar cliente\n3 - Editar cliente\n4 - Excluir cliente\n0 - Sair")
    option = input("\nEscolha uma opção: ")
    if option == "1":
        print("\n1 - Cadastrar cliente")
        cad = input("\nDigite seu nome completo: ")
        phone_number = int(input(f"\nBem vindo, {cad}.\nContato: "))
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
    elif option == "4":
        print("\n4 - Excluir cliente")
    elif option == "0":
        print("\n0 - Sair")
    else:
        print("Opção inválida. Tente novamente.")
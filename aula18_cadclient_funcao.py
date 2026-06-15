
clientes = []
def mostrar_menu():
    print("\n--- Menu ---")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Alterar cliente")
    print("4 - Excluir cliente")
    print("5 - Sair")

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    clientes.append(nome)
    print("Cliente cadastrado!")

def listar_clientes():
    print("\nClientes:")
    for cliente in clientes:
        print(cliente)

def alterar_cliente():
    nome = input("Nome a alterar: ")
    if nome in clientes:
        novo_nome = input("Novo nome: ")
        posicao = clientes.index(nome)
        clientes[posicao] = novo_nome
        print("Cliente alterado!")
    else:
        print("Cliente não encontrado.")

def excluir_cliente():
    nome = input("Nome a excluir: ")
    if nome in clientes:
        clientes.remove(nome)
        print("Cliente excluído!")
    else:
        print("Cliente não encontrado.")

while True:
    mostrar_menu()
    opcao = input("Escolha: ")
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        alterar_cliente()
    elif opcao == "4":
        excluir_cliente()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
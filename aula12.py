#Listas (continuação):

# lista1 = [1,2,3]
# lista2 = lista1
# print(f"{lista1}\n{lista2}")
# lista2.append(4) #acaba atualizando as DUAS listas
# print()
# print(f"{lista1}\n{lista2}")

# #agora, atualizando SÓ a lista 2:

# lista2 = lista1.copy() #garante que a lista1 permaneça como está antes do append
# lista2.append(5) #atualiza SÓ a lista2!
# print()
# print(f"{lista1}\n{lista2}")


#agora, consertando o cadastro de cliente:

# clientes = [] #Cadastro Cliente 1
# print("Informe o nome e telefone:")
# for cliente in range(2):
#     clientes.append(input())
# print("*********"*8)
# print(f"\nCliente:\n{clientes[0]}\n")
# print(f"Telefone:\n{clientes[1]}")

# print("\nLista de Clientes:",clientes)
# print("*********"*10)

# cad_clientes = [] #Criando uma lista geral para TODOS os clientes
# cad_clientes.append(clientes[:])
# print(f"Lista Cadastro de Clientes:\n{cad_clientes}")

# clientes.clear() #A lista fica vazia

# clientes = [] #Cadastro Cliente 2
# print("Informe o nome e telefone:")
# for cliente in range(2):
#     clientes.append(input())
# print("*********"*8)
# print(f"\nCliente:\n{clientes[0]}\n")
# print(f"Telefone:\n{clientes[1]}")

# print("\nLista de Clientes:",clientes)
# print("*********"*10)

# #NÃO REPETE cad_clientes = [], pois isso sobrescreverá a lista
# cad_clientes.append(clientes[:])
# print(f"Lista Cadastro de Clientes:\n{cad_clientes}")




# #Agora com o .copy: não gera listas dentro de listas
# clientes = [] #Cadastro Cliente 1
# print("Informe o nome e telefone:")
# for cliente in range(2):
#     clientes.append(input())
# print("*********"*8)
# print(f"\nCliente:\n{clientes[0]}\n")
# print(f"Telefone:\n{clientes[1]}")

# print("\nLista de Clientes:",clientes)
# print("*********"*10)

# cad_clientes = [] #Criando uma lista geral para TODOS os clientes
# cad_clientes.append(clientes.copy())
# print(f"Lista Cadastro de Clientes:\n{cad_clientes}")

# clientes.clear()

# clientes = [] #Cadastro Cliente 2
# print("Informe o nome e telefone:")
# for cliente in range(2):
#     clientes.append(input())
# print("*********"*8)
# print(f"\nCliente:\n{clientes[0]}\n")
# print(f"Telefone:\n{clientes[1]}")

# print("\nLista de Clientes:",clientes)
# print("*********"*10)

# cad_clientes.append(clientes.copy())
# print(f"Lista Cadastro de Clientes:\n{cad_clientes}")



#Cadastro de clientes com .append e loop:
cliente = []
cad_clientes = []
while True:
    cad = input("Deseja cadastrar um cliente?(s/n):\n")
    if cad == "n":
        break
    elif cad == "s":
        cliente.append(input("Nome do cliente: "))
        cliente.append(int(input("Idade do cliente: ")))
        cliente.append(input("Telefone do cliente: "))
        cad_clientes.append(cliente[:])
        cliente.clear()
    else:
        print("Opção inválida. Tente novamente.")
        continue
print()
listar = input("Deseja listar os clientes cadastrados?(s/n):\n")
if listar == "s":
    cad_clientes.sort() #Listar em ordem alfabética
    for cliente in cad_clientes:
        print("*"*20)
        print(f"Cliente: {cliente[0]}\nIdade: {cliente[1]} anos\nTelefone: {cliente[2]}")
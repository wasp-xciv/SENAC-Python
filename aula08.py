#Criar um menu:
# option = ""
# while option != "0":
#     print("=== MENU CLIENTE ===\n1 - Cadastrar cliente\n2 - Listar cliente\n3 - Editar cliente\n4 - Excluir cliente\n0 - Sair")
#     option = input("\nEscolha uma opção: ")
#     if option == "1":
#         print("1 - Cadastrar cliente")
#     elif option == "2":
#         print("2 - Listar cliente")
#     elif option == "3":
#         print("3 - Editar cliente")
#     elif option == "4":
#         print("4 - Excluir cliente")
#     elif option == "0":
#         print("0 - Sair")
#     else:
#         print("Opção inválida. Tente novamente.")



# *******
# Criação de Senha:
# user = input("Digite seu usuário: ")
# password = input("Digite sua senha: ")
# while password != "banana":
#     print("Senha Incorreta.")
#     password = input("Digite sua senha: ")

# print("Acesso Liberado")

##Outra forma:
# user = input("Digite seu usuário: ")
# while True:
#     password = input("Digite sua senha: ")
#     if password != "banana":
#         print("Senha Incorreta.")
#         continue
#     else:
#         print("Acesso Liberado")
#         break

# Criação de Senha:
# user = input("Digite seu usuário: ")
# tentativas = 0
# while tentativas < 3:
#     password = input("Digite sua senha: ")
#     if password == "banana":
#         print("Acesso Liberado!")
#         break
#     elif tentativas == 3:
#         print("Acesso Bloqueado!")
#     else:
#         print(f"Senha Incorreta. Tentativa {tentativas}.")
#     tentativas += 1

# Outra forma:
user = input("Digite seu usuário: ")
tentativas = 3
while tentativas != 0:
    password = input("Digite sua senha: ")
    if password == "banana":
        print("Acesso Liberado!")
        break
    tentativas -= 1

if tentativas == 0:
    print("Acesso Bloqueado!")

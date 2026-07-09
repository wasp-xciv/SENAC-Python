# """
# Exercícios Guanabara
# """
# # #1
# msg = "Olá, mundo!"
# print(msg)

# #2
# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}, tudo bem?")

# #3
# birth = int(input(f"Qual ano você nasceu, {nome}?\n"))
# current = 2026
# age = current - birth
# print(f"Ah, você tem {age} anos, né?")

# #4
# algo = input(f"Digite algo, {nome}:\n")
# print(f"Você digitou um {type(algo)}, {nome}?")
# print("Só tem espaços? ", algo.isspace())
# print("É um número? ", algo.isnumeric())
# print("É alfabético? ", algo.isalpha())
# print("É alfanumérico? ", algo.isalnum())

# #5- Predecessor e Sucessor
# number = int(input("Escolha um número:\n"))
# pred = number - 1
# sus = number + 1
# print(f"Número escolhido:{number}"
#       f"Seu predecessor é {pred} e seu sucessor é {sus}")

#6 - Dobro, Triplo, Raiz Quadrada
n = int(input("Escolha um número:\n"))
print(f"O número escolhido é {n}.\nO dobro de {n} é {n*2}."
      f" O triplo de {n} é {n*3}. E a raiz quadrada de {n} é {n**0.5:.1f}.")

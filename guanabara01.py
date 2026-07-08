"""
Exercícios Guanabara
"""
# #1
msg = "Olá, mundo!"
print(msg)

# #2
nome = input("Digite seu nome: ")
print(f"Olá, {nome}, tudo bem?")

# #3
birth = int(input(f"Qual ano você nasceu, {nome}?\n"))
current = 2026
age = current - birth
print(f"Ah, você tem {age} anos, né?")

# #4
algo = input(f"Digite algo, {nome}:\n")
print(f"Você digitou um {type(algo)}, {nome}?")
print("Só tem espaços? ", algo.isspace())
print("É um número? ", algo.isnumeric())
print("É alfabético? ", algo.isalpha())
print("É alfanumérico? ", algo.isalnum())



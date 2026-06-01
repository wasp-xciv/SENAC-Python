#Slicing:

# nome = input("Digite seu nome completo: ").strip()
# print(f"Nome em maiúsculo = {nome.upper()}")
# print(f"Nome em minúsculo = {nome.lower()}")
# print("Comprimento do texto =", len(nome))
# print(f"Total de letras = {len(nome) - nome.count(" ")}")

# for contador, caractere in enumerate(nome):
#     print(contador,caractere,end=" ")

# print(f"\nSeu primeiro nome é {nome[3:]}")

# nomes = nome.split(" ")
# print(nomes)

# print(f"\nSeu primeiro nome é {nomes[1]} e seu sobrenome é {nomes[0]}")

# nome2 = input("Digite o novo nome: ")
# nome2 = nome.replace(nome,nome2)
# print(f"\n{nome2}")

#Tuplas

#Tuplas são imutáveis.

premios = ("moto","carro","viagem","casa")
for c,n in enumerate(premios):
    print(f"O {c+1}º prêmio é um(a) {n}!")
dinheiro = (1000.00, 2000.00, 5.000)
premiacao = premios + dinheiro #pois tuplas não permitem alterações, só resta criar uma nova variável
print(premiacao)

##Sorteio

from random import randint
numeros = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
for c in numeros:
    print(c,end=" ")


print()
print(f"O maior número sorteado é {max(numeros)}")
print(f"O menor número sorteado é {min(numeros)}")
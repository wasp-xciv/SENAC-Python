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

# premios = ("moto","carro","viagem","casa")
# for c,n in enumerate(premios):
#     print(f"O {c+1}º prêmio é um(a) {n}!")
# dinheiro = (1000.00, 2000.00, 5.000)
# premiacao = premios + dinheiro #pois tuplas não permitem alterações, só resta criar uma nova variável
# print(premiacao)

# ##Sorteio

# from random import randint
# numeros = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
# for c in numeros:
#     print(c,end=" ")


# print()
# print(f"O maior número sorteado é {max(numeros)}")
# print(f"O menor número sorteado é {min(numeros)}")

# #**************************************************************************************************************

# nums = []
# for c in range(0,5):
#     num = int(input("Digite um número: "))
#     nums.append(num)
# print(nums) ###aqui é uma lista!
# print(type(nums))

# nums = tuple(nums)
# print(type(nums)) ###aqui a lista é convertida para tupla, pois tupla originalmente é IMUTÁVEL, ou seja, não aceita appendm insert, etc
# print(f"Os números escolhidos foram {nums}!")

#***************************************************************************************************************

produtos = ("pão", "salgado", "suco", "café", "bolo")
print(produtos)

for produto in produtos:
    print(f"Produto à venda: {produto}")

print(sorted(produtos)) ###mostra como lista
print(f"O produto suco está na posição {produtos.index("suco")}")

###maneiras diferentes de apresentar a lista/tupla 👇👇👇👇
for produto in produtos:
    print(f"\nO produto {produto} está na posição {produtos.index(produto)}") #usando o INDEX
print()

for pos,prod in enumerate(produtos):
    print(f"O produto {prod} está na posição {pos}.") #usando o ENUMERATE

print()

for produto in range(len(produtos)):
    print(f"O produto {produtos[produto]} está na posição {produto}") #usando o RANGE(LEN(tupla))
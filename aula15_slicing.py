#Slicing:

nome = input("Digite seu nome completo: ").strip()
print(f"Nome em maiúsculo = {nome.upper()}")
print(f"Nome em minúsculo = {nome.lower()}")
print("Comprimento do texto =", len(nome))
print(f"Total de letras = {len(nome) - nome.count(" ")}")

for contador, caractere in enumerate(nome):
    print(contador,caractere,end=" ")

print(f"\nSeu primeiro nome é {nome[3:]}")

nomes = nome.split(" ")
print(nomes)

print(f"\nSeu primeiro nome é {nomes[1]} e seu sobrenome é {nomes[0]}")

nome2 = input("Digite o novo nome: ")
nome2 = nome.replace(nome,nome2)
print(f"\n{nome2}")
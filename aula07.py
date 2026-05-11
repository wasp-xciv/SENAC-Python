# Loops

# contador = 0
# while contador <= 100:
#     print('repetiu',contador,'vezes')
#     contador += 3 #contador = contador + 1 (INCREMENTO)

# numero = int(input("Digite um número ou 0 para encerrar: "))
# while numero != 0:
#     numero = int(input("Digite um número ou 0 para encerrar: "))

# print("FIM")

#outra forma (com if e else):
# while True: 
# 	numero = int(input("Digite um número ou 0 para encerrar: ")) 
# 	if numero != 0: 
# 		continue 
# 	else: 
# 		break 

# print("FIM") 

# resposta = "S"
# while resposta == "S":
#     n = int(input("Digite um número: "))
#     resposta = input("Deseja continuar? (S/N): ").upper().strip()[0]
#     #upper vem de "uppercase", ou seja, ele leva em consideração entradas em maiúscula ou minúscula.
#     #strip()[0] tem a ver com retirada dos espaços, onde apenas "s"im ou "n"ão serão considerados para prosseguir com o loop.

# print("Fim")

# resposta = "s"
# while resposta == "s":
#     n = int(input("Digite um número: "))
#     resposta = input("Deseja continuar? (S/N): ").lower().strip()[0]
#     #lower vem de "lowercase", ou seja, ele leva em consideração entradas em maiúscula ou minúscula.
#     #strip()[0] tem a ver com retirada dos espaços, onde apenas "s"im ou "n"ão serão considerados para prosseguir com o loop.

# print("Fim")

#O Sistema de Notas 2.0:
contador = 1
soma = 0
while contador <= 4:
    nota = float(input(f"Insira a {contador}º nota: "))
    contador += 1
    soma += nota

print("Média final:", soma/4)


"""
Exercícios Guanabara
"""
#1
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

#5
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# media = (nota1 + nota2) / 2
# print(f"Nota 1 = {nota1}\nNota 2 = {nota2}\nA média do aluno é: {media:,.1f}.")

#6
# medida = float(input("Distância em metros: "))
# cm = medida * 100
# mm = medida * 1000
# print(f"{medida}m(s) equivale a {cm} centimetro(s) e {mm} milímetro(s).")

# #7 TABUADA
# n = int(input("Digite o número para exibir sua tabuada correspondente: "))
# print(">>> tabuada de multiplicação <<<")
# print(f"{n} x {1} = {n*1}")
# print(f"{n} x {2} = {n*2}")
# print(f"{n} x {3} = {n*3}")
# print(f"{n} x {4} = {n*4}")
# print(f"{n} x {5} = {n*5}")
# print(f"{n} x {6} = {n*6}")
# print(f"{n} x {7} = {n*7}")
# print(f"{n} x {8} = {n*8}")
# print(f"{n} x {9} = {n*9}")
# print(f"{n} x {10} = {n*10}")

#8 Conversor de Moedas
# wallet = float(input("Quanto dinheiro você tem? R$"))
# dol = wallet / 5.00
# print(f"Você tem R${wallet:,.2f}.\nIsso equivale a US${dol:,.2f}")

#9 Calculando descontos
# product = float(input("Digite o preço do produto:\nR$"))
# discount = product*5/100
# final_price = product - discount
# print(f"Você tem direito à 5% de desconto!\nNovo preço: R${final_price:,.2f}")

#10 Conversor de Temperatura
# celsius = float(input("Digite a temperatura em Celsius:\n"))
# farenheit = (celsius * 1.8) + 32
# print(f"{celsius:,.1f}°C equivale à {farenheit:,.1f}°F.")

#Aluguel de Carros: R$60,00/dia e R$0,15/km
dias = int(input("Aluguel de quantos dias?\n"))
km = float(input("Quantos kms rodados?\n"))
carro = (dias*60) + (km*0.15) 
print(f"Dias alugados: {dias} dia(s)\nQuilômetros rodados: {km}km\nTotal:R${carro:,.2f}")
#Cálculo de IMC
# print("=== Calculadora de IMC ===")

# peso = float(input("Insira seu peso: "))
# altura = float(input("Agora sua altura: "))
# imc = altura * altura
# imc = peso / imc
# #abaixo = imc < 18.5
#normal = imc >= 18.5 or imc <= 24.9
#sobrepeso = imc >= 25.0 or imc <= 29.9


# if imc < 18.5:
#     print(f"Seu IMC é {imc:,.1f}. Você está abaixo do peso.")
# else:
#     if imc >= 18.5 and imc <= 24.9:
#         print(f"Seu IMC é {imc:,.1f}. Seu peso está na faixa ideal.")
#     elif imc >= 25.0 and imc <= 29.9:
#         print(f"Seu IMC é {imc:,.1f}. Você está com sobrepeso")
#     else:
#         print(f"Seu IMC é {imc:,.1f}. Você está obeso.")

# IDADE - FAIXA ETÁRIA

idade = int(input("Digite sua idade: "))

if idade < 0:
    print("\nDigite uma idade válida.")
elif idade <= 12:
    print("\nVocê é criança.")
elif idade <= 17:
    print("\nVocê é adolescente.")
elif idade<= 59:
    print("\nVocê é adulto.")
elif idade > 100:
    print("\nDigite uma idade válida.")
else:
    print("\nVocê é idoso.")
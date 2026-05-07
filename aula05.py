# # IDADE - FAIXA ETÁRIA

# idade = int(input("Digite sua idade: "))

# if idade < 0:
#     print("\nDigite uma idade válida.")
# elif idade <= 12:
#     print("\nVocê é criança.")
# elif idade <= 17:
#     print("\nVocê é adolescente.")
# elif idade<= 59:
#     print("\nVocê é adulto.")
# elif idade > 100:
#     print("\nDigite uma idade válida.")
# else:
#     print("\nVocê é idoso.")

# Regras do Sistema

# nota = float(input("Insira uma nota de 0 a 10: "))

# if nota >= 9:
#     print(f"\nNota {nota}: Conceito A.")
# elif nota >= 7:
#     print(f"\nNota {nota}: Conceito B.")
# elif nota >=5:
#     print(f"\nNota {nota}: Conceito C.")
# else:
#     print(f"\nNota {nota}: Conceito D.")

# Desafio: Desconto Inteligente

print("=== CHECKOUT ===")

valor_compra = float(input("Valor da compra: "))
vip_desconto20 = valor_compra - valor_compra * 20/100
vip_desconto10 = valor_compra - valor_compra * 10/100

if valor_compra > 100.00:
    vip = input("Cliente Vip? S/N: ")
    if vip == "S":
        print("Valor original:",valor_compra,"\nValor final:", vip_desconto20)
    elif vip == "N":
        print("Valor original:",valor_compra,"\nValor final:",vip_desconto10)
else:
    print("Valor total: ", valor_compra)

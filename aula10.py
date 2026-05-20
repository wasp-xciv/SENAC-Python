#For e Range

# for contador in range (1,21):
#     print("repetiu",contador,"vezes.")
# print("=== Fim ===")

# # para for, o contador sempre considera o primeiro número, mas NÃO imprime o último.
# # Comparação com while:

# i = 0
# while i < 10:
#     i += 1
#     print("repetiu",i,"vezes")
# print("=== Fim ===")

# for contador in range (10,100,10):
#     print("repetiu",contador,"vezes")
# print("=== Fim ===")

# O salto:
# from time import sleep
# for i in range (10,-1,-1):
#     print("repetiu",i,"vezes")
#     sleep(0.70)

# For também inspira economia. No exemplo da inserção das notas:
# soma = 0
# for c in range (1,5):
#     print(input(f"Informe a {c}º nota: "))
#     soma += c

# for i in range (1,11):
#     resultado = 3*i
#     print(f"3 x {i} = {resultado}")


while True:
    num = int(input("Escolha um número da tabuada: "))
    operacao = input("Escolha a operação:\nAdição(+)\nSubtração(-)\nMultiplicação(*)\nDivisão(/)\n")
    if operacao == "+":
        print(f"\nTabuada de Adição de {num}")
        for i in range (num,11):
            resultado = num + i
            print(f"\n{num} + {i} = {resultado}")
    elif operacao == "-":
        print("\nSubtração")
        for i in range (num,11):
            print(f"\n{i} - {num} = {i - num}")
    elif operacao == "*":
        print("\nMultiplicação")
        for i in range(1,11):
            resultado = num * i
            print(f"\n{num} x {i} = {resultado}")
    elif operacao == "/":
        print("\nDivisão")
        for i in range (num,11):
            print(f"\n{i} / {num} = {i/num:,.1f}")
    else:
        print("Operação inválida.")
    loop = input("Deseja continuar?\ns/n: ").strip().lower()[0]
    if loop == "n":
       break

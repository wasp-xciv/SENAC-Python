# Valores Booleanos e Operações de Atribuição

#Flexibilidade na Aprovação Escolar

# nota_prova = 5.0
# nota_trabalho = 8.0
# check_aprovacao = nota_prova >= 7 or nota_trabalho >= 7
# print()
# print("Resultado:", check_aprovacao)

#O Interruptor do Sistema
# sistema_ativo = False
# resultado = not sistema_ativo
# print(resultado)

#Empilhando Regras para Motoristas

# idade = 22
# carteira_motorista = True
# no_fines = True
# condicao = idade > 18 and carteira_motorista and no_fines
# print(condicao)

#IF ELIF ELSE

#Flexibilidade na Aprovação Escolar

nota_prova = float(input("Digite a nota da prova: "))
nota_trabalho = float(input("Digite a nota do trabalho: "))
frequencia = float(input("Informe a frequência: "))
media = (nota_prova + nota_trabalho) / 2

if frequencia < 75:
    print("Frequência insuficiente. O aluno está reprovado.")
elif media >= 7:
    print(f"\nA média foi {media} e a frequência {frequencia}%. O aluno está aprovado!")
elif media >= 5:
    print(f"\nA média foi {media} e a frequência {frequencia}%. O aluno está de re-cu-pe-ra-ção!")
else:
    print(f"\nA média foi {media} e a frequência {frequencia}%. O aluno está reprovado :(")

#DESAFIO DO DIA! Calculadora de IMC

# crie um programa que calcule o imc do usuário: altura, peso e genero (idade não é necessário)

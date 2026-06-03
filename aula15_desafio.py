# ==== DESAFIO ====

# # Desafio 1: Cadastro de Produtos (Tupla + Loop FOR + IF) 
# # Situação 
# # Você tem uma tupla com nomes de produtos e outra com seus preços. Seu 
# # programa deve analisar esses dados. 
# # Dados iniciais 
produtos = ("Arroz", "Feijão", "Macarrão", "Óleo", "Açúcar") 
precos = (20.00, 8.00, 5.00, 7.00, 4.00) 
# # Objetivos 
# # 1. Mostrar todos os produtos com seus preços
for produto in range(len(produtos)):                #maneira de correlacionar os index de ambas as listas
    print(f"O produto {produtos[produto]} custa R${precos[produto]:,.2f}")

# # 2. Mostrar quais produtos custam mais de R$ 10 
print()
print("Produtos que custam mais de R$10,00:")
for index,prod in enumerate(produtos):   #enumerate pede dois argumentos(índice, valor)
    if precos[index] > 10:
        print(f"O produto maior que R$10,00 é {prod} e custa R${precos[index]:,.2f}")

# # 3. Calcular o total da compra

total = 0
for index,prod in enumerate(produtos):     #outra maneira de calcular a soma dos elementos de uma lista
    total += precos[index]
print(f"\nO valor total dos produtos é R${total:,.2f}")


# Passo a passo 
# 1. Use um loop FOR com range() para percorrer as tuplas 
# 2. Mostre o nome do produto e seu preço 
# 3. Use um IF para verificar se o preço é maior que 10 
# 4. Some os preços usando uma variável acumuladora

#************************************************************************************
# Desafio 2: Análise de Notas (Tupla + FOR + IF/ELIF)
# Situação
# Você recebeu uma tupla com notas de alunos e precisa avaliar o desempenho da 
# turma.
# Dados iniciais
notas = (7.5, 4.0, 6.5, 9.0, 3.5, 8.0)
total = 0
aprovados = 0

# Objetivos:

# 1. Mostrar cada nota e sua situação: 
# o Aprovado (nota ≥ 7)
# o Recuperação (nota ≥ 5 e < 7)
# o Reprovado (nota < 5)
#notas = list(notas)

for nota in notas: #é importante diferenciar valor de índice
     if nota >= 7.0:
         aprovados +=1
         print(f"Nota - {nota}\nStatus - Aprovado!") #variável 'nota' sozinha, ao invés de inserida dentro de 'notas'
     elif nota >5.0 and nota <7.0:
         print(f"Nota - {nota}\nStatus - Em Recuperação!")
     else:
        print(f"Nota - {nota}\nStatus - Reprovado!")

# 2. Mostrar a média da turma
print()
print("=== Média da turma: ===\n")

# media = sum(notas)/len(notas)   #MUITO mais fácil

for nota in range(len(notas)):
    total += notas[nota]
media = total/len(notas)
print(f"A média da turma é {media:.1f}")
    

# 3. Mostrar quantos alunos foram aprovados
print()
print("=== Aprovados ===\n")
aprovados = 0
# for nota in notas:
#     if nota >= 7.0:
#         aprovados += 1

# for index,nota in enumerate(notas):     #outra maneira de resolver
#     if notas[index] >= 7.0:
#         aprovados += 1

for nota in range(len(notas)):      #oooooooutra maneira de resolver
    if notas[nota] >= 7.0:
        aprovados +=1

print(f"{aprovados} alunos foram aprovados!")

# Passo a passo
# 1. Percorra a tupla com FOR
# 2. Use IF / ELIF / ELSE para classificar cada estudante
# 3. Some as notas para calcular a média
# 4. Conte quantos alunos foram aprovados
 
# Dica para os alunos
# • Tuplas são imutáveis → não podem ser alteradas
# • Para percorrer tuplas: "for item in tupla ou for i in range(len(tupla))"
#
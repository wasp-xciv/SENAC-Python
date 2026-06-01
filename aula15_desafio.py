# ==== DESAFIO ====

# Desafio 1: Cadastro de Produtos (Tupla + Loop FOR + IF) 
# Situação 
# Você tem uma tupla com nomes de produtos e outra com seus preços. Seu 
# programa deve analisar esses dados. 
# Dados iniciais 
produtos = ("Arroz", "Feijão", "Macarrão", "Óleo", "Açúcar") 
precos = (20, 8, 5, 7, 4) 
# Objetivos 
# 1. Mostrar todos os produtos com seus preços
for produto in range(len(produtos)):
    print(f"O produto {produtos[produto]} custa R${precos[produto]:,.2f}")

# 2. Mostrar quais produtos custam mais de R$ 10 
print()
print("Produtos que custam mais de R$10,00:\n")
for pos,prod in enumerate(produtos):
    if precos[pos] > 10:
        print(f"O produto maior que R$10,00 é {prod} e custa R${precos[pos]:,.2f}")

# 3. Calcular o total da compra

soma = 0
for pos,prod in enumerate(produtos):
    soma += precos[pos]
print(f"O valor total dos produtos é R${soma:,.2f}")


# Passo a passo 
# 1. Use um loop FOR com range() para percorrer as tuplas 
# 2. Mostre o nome do produto e seu preço 
# 3. Use um IF para verificar se o preço é maior que 10 
# 4. Some os preços usando uma variável acumuladora
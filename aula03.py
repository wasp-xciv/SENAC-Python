#Exercício 01: Loja

# produto = "Memória RAM 4GB"
# preco = 264.99
# quantidade = 30

# total_estoque = preco * quantidade

# print("Orçamento do produto:")
# print()
# print(f"= {produto} =")
# print(f"Preço por unidade: R$ {preco:,.2f} reais")
# print(f"Quantidade requisitada: {quantidade} unidades")
# print(f"Total da compra: R${total_estoque:,.2f} reais")

#Exercício 02: Boletim

# aluno = "Qi Yu"
# nota1= 6.5
# nota2= 9.5
# media= (nota1+nota2)/2

# print(f"> Aluno: {aluno}\n> Média: {media}")

#Exercício 3: Aumento de salário

# nome = "Li Shen"
# sal_at = 1500.00
# percentual = 1

# print(f"=== Funcionário: {nome} ===\n> Vencimento atual: R${sal_at:,.2f}"
#       f"\n> Percentual de Aumento: R${(sal_at*percentual)/100:,.2f}"
#       f"\n> Novo vencimento: R${(sal_at*percentual)/100+sal_at:,.2f}")

#Valores Booleanos

# idade = int(input("Digite sua idade: "))
# resultado = idade >= 20
# print(resultado)

# Desafio do cadastro
nome = input("Bem vindo(a)!\nDigite seu nome: ")
idade = int(input(f"Ok, {nome}, agora digite sua idade: "))
saldo = float(input(f"Perfeito, {nome}, agora digite seu saldo bancário: "))

check_idade = idade > 18
check_saldo = saldo >= 1000.00
check_nome = nome == "Ana"

print(f"\nNome informado: {nome}"
      f"\nIdade informada: {idade}"
      f"\nSaldo informado: R${saldo:,.2f}")
print(f"\nIdade maior que 18: {check_idade}"
      f"\nSaldo maior ou igual a R$1000,00: {check_saldo}"
      f"\nNome é igual a Ana: {check_nome}")


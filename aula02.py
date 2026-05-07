""" #Entrada de Dados pelo Usuário: o "input" """

# nome=input("Informe seu nome: ")
# #saída
# print(f"O nome informado foi: {nome}")


# idade=int(input("Qual a sua idade: "))
# print(f"O usuário {nome} tem {idade} anos.")
# print(type(nome))
# print(type(idade))

# num1=float(input("Digite um número: "))
# num2=int(input("Digite outro número: "))
# print(f"A soma de {num1} e {num2} é {num1 + num2}.")
# # print(type(num1), type(num2))
# #cls é o comando para limpar o terminal.

# #Exemplo Cadastro de Filme
# movie="Oppenheimer"
# year=2023
# rate=8.4
# disponivel=True
# search=input("Digite sua busca: ")
# print("Filme:",movie)
# print("Ano:",year)
# print("Nota:",rate)
# print("Disponível:",disponivel)

#Cadastro de Loja
# produto1="Teclado Ergonômico"
# produto2="Cadeira Gamer"
# preco1=25.00
# preco2=239.99
# cod1="AB58-Y"
# cod2="XO77-21"
# nome=input("Nome do cliente: ")
# idade=input("Idade: ")
# genero=input("Gênero: ")
# print(f'Bem-vindo, {nome}\n{idade} anos\n{genero}')
# search=input("Digite sua busca: ")
# print(f'Resultados por "{search}":\n{produto1}\nPreço:R${preco1:.2f} reais\nCod.:{cod1}')
# search2=input("Digite sua busca: ")
# print(f'Resultados por "{search2}":\n{produto2}\nPreço:R${preco2:.2f} reais\nCod.:{cod2}')

#Solicitar a entrada do usuário dos seguintes dados:
# nome, idade, endereço, estado_civil, escolaridade, salario1, salario2, salario3.
# Processar a média salarial
# Crie uma saída  com todos os dados informados e a média salarial.

nome=input("Insira seu nome: ")
idade=int(input("Insira sua idade: "))
endereco=input("Insira seu endereço: ")    
estado_civil=input("Insira seu estado civil: ")
escolaridade=input("Insira sua escolaridade: ")
salario1= float(input("Informe o salário1: "))
salario2= float(input("Informe o salário2: "))
salario3= float(input("Informe o salário3: "))
media_salarial= (salario1+salario2+salario3)/3
print("****" * 20)
print(f'Funcionário: {nome}\nIdade: {idade} anos\nEndereço: {endereco}\nEstado Civil: {estado_civil}'
      f'\nEscolaridade: {escolaridade}\nMédia Salarial: R${media_salarial:,.2f} reais.')
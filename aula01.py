idade = 20
salario = 1500.75
altura = 1.80
genero = "M"
nome = "Yu Qi"
print("Dados do Cliente:")
print("Idade:",idade)
print("Salário:",salario, "reais")
print("Altura:",altura)
print("Gênero:",genero)
print("Nome:", nome)
print("-----"*10)
# """ print(type(idade)) #
# print(type(salario))
# print(type(altura))
# print(type(genero))
# print(type(nome)) """não é pra mostrar

# """ maneira tradicional """
# """ # print(nome,idade,"anos, recebe",salario,"reais.\n",nome,"tem", altura, "e é", genero,".") 

# """ maneira format """
# """ # print("O cliente {} recebe {:,.2f} reais por mês.\n"
# # "{} tem {} anos e é {}.".format(nome,salario,nome,idade,genero))"""

# """ format short ver """
print(f"O cliente {nome} tem {idade} anos, é do sexo {genero}, tem altura {altura:.2f}.\n"
       f"{nome} recebe {salario:,.2f} reais por mês.") 
print("------"*20)

a=5
b=2
print("O resultado é:",a%b)
print(f"O resultado de '{a} + {b}' é",a+b)
print(f"O resultado de '{a} - {b}' é",a-b)
print(f"O resultado de '{a} / {b}' é",a/b)
print(f"O resultado de '{a} // {b}' é",a//b)
print(f"O resultado de '{a} % {b}' é",a%b)
print(f"O resultado de '{a} x {b}' é",a*b)
print(f"O resultado de '{a} ** {b}' é",a**b)
print("-----"*20)
ano=12
print(f"{nome}, ao fim de um ano, o funcionário terá recebido {salario*ano:,.2f}")

#
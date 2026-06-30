'''
#Como criar a função?
def saudacao():
    print("Olá Galera!")
    print("Bora aprender python")
#E como chamar a função criada?

saudacao()

'''

# def saudacao():
#     print("OOOOOOOOOOOOOOOOOOOOOOOI")
#     print("\nTudo bem?")

# saudacao() #chama a função

# #é possível definir que tipo de parâmetro vai dentro da função:

# def imprime_nome(nome):
#     print(f"Nome:{nome}")

# imprime_nome("João")

# #reaproveitando a função saudação:

# def saudacao2(nome):
#     print(f"Olá,{nome}!")

# saudacao2("Ana")

# ################################################

# def imprime_nome(nome = "não informado", idade = "não informada"):
#     print(f"Nome do cliente: {nome}, Idade: {idade}")

# imprime_nome("Ana Silva",25)
# imprime_nome(27,"Qi Yu")  ####a função não reconhece a inversão de dados e emitirá o que já foi acordado no print.
# #corrigindo:
# imprime_nome(idade=27,nome="Qi Yu")
# imprime_nome("Ana Silva") #dará o aviso de que a idade não foi informada
# imprime_nome() #avisa que nem nome e nem idade foram informados

# #################################

# alunos = ['Ana','João','Maria','Pedro']
# def listar_alunos():
#     print("Lista de alunos:\n")
#     for aluno in alunos:
#         print(f"{aluno} está matriculado(a) no curso de Programação.")


# listar_alunos()

# ##################################

# def cad_aluno():
#     aluno = input("Digite o nome do aluno: ")
#     alunos.append(aluno)
#     print(f"{aluno} foi cadastrado com sucesso!")

# cad_aluno()
# cad_aluno()
# alunos.sort()
# listar_alunos()

# #E para remover o aluno?
# def excluir_aluno():
#     aluno = input("Digite o aluno a ser excluído:\n")
#     if aluno in alunos:
#         alunos.remove(aluno)
#         print(f"{aluno} excluído com sucesso!")
#     else:
#         print(f"{aluno} não foi encontrado na lista.")

# excluir_aluno()
# listar_alunos()

##Resultados com return: a exportação de uma operação dentro da função.
# def soma(a,b):
#     resultado = a + b
#     return resultado
# total = soma(4,9)
# print(f"O resultado foi {total}.")

# ###############################
# def calcular_idade(birthyear,current_year=2026):
#     idade = current_year - birthyear
#     return idade

# idade_xav = calcular_idade(1800) ##aqui é informado apenas o ano de nascimento, a função completa com o paramêtro current_year
# print(f"Xavier tem {idade_xav} anos.")

# idade_zay = calcular_idade(1993,2010) #aqui o valor 2026 do parâmetro current_year é ignorado, sendo substituído por outro ano
# print(f"Zayne tem {idade_zay} anos")

# #################################
# '''
# Originalmente, a variável "idade" não funciona sozinha, pois está contida DENTRO da função "calcular_idade".
# Por isso é necessário o "return"
# Como contornar isso?
# É necessário editar a variável como "global".
# '''
# ####################################
# def calcular_imc(peso,altura):
#     imc = peso/altura**2
#     return imc

# resultado = calcular_imc(peso=70,altura=1.75)
# print(f"O imc é {resultado:.2f}")

####################################################
def maior_30(*args): #args apontam que não se sabe quantos parâmetros uma função possuirá.
    print(args)
    print(type(args))
    for num in args:
        if num > 30:
            print(f"Número(s) maior que 30: {num}")

maior_30(10,25,32,77,9)
print()
maior_30(99,24,80)
print()
maior_30(30,29,41)
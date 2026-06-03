#Dicionários em Python
#Dicionários são estruturas de dados que armazenam informações na forma de pares chave:valor

#Chaves: únicas, podem ser strings ou números
#Valores: podem ser qualquer tipo de dado (strings, números, listas, outros dicionários etc)

pessoa = {"nome": "Qi Yu","idade":27,"cidade": "Linkon","telefone":"(88) 5122-0000"}
print(pessoa["nome"])
print()
print(f"{pessoa["idade"]} anos")
print()
print(pessoa["cidade"])
print()
print(pessoa["telefone"])

#.keys()
print()
print(pessoa.keys())

#.values()
print()
print(pessoa.values())

#.items()
print()
print(pessoa.items())

print()
print(pessoa)

for k,v in pessoa.items():
    print(f"\n{k}:{v}")

#Como adicionar novas chaves e valores em um dicionário?
pessoa["profissão"] = "presidente"
print(pessoa)

# #Como modificar uma chave existente?
pessoa["profissão"] = "pintor"
print(pessoa)

pessoa["estado civil"] = "destinado à ser viúvo"
print(pessoa)

# #Como deletar um par?
print()
del pessoa["profissão"]
print(pessoa)

#Como usar o for para chamar keys OU values?
#keys:
for chaves in pessoa:
    print(chaves)
#values: aí tem que usar o método do dicionário
for valor in pessoa.values():
    print(valor)

# nome = {}
# name = input("Digite seu nome:\n")
# age = input("Digite sua idade:\n")
# hobby = input("Hobby:\n")
# nome = {"Nome":name,"Idade":age,"Hobby":hobby}
# print(nome)

###################################################################################################
print()
pessoa["notas"] = [7.0,8.5,9.0]
print(pessoa["notas"])
media = sum(pessoa["notas"])/len(pessoa["notas"])
print(f"{media:,.1f}")


#O que fazer se surgir a dúvida se uma chave existe ou foi apagada
# print(pessoa["profissão"])  #foi deletado
print()
print(pessoa.get("Profissão","Chave não encontrada (；′⌒`)"))

#Desafio

#Nível Básico:
# Missão: Criar um dicinário com nome, idade e cidade de uma pessoa. Exibir dados na tela.

profile = {"Nome":"Li Shen","Idade":29,"Cidade":"Linkon"}
print(f"Nome: {profile['Nome']}\nIdade:{profile["Idade"]} anos\nCidade: {profile["Cidade"]}")

#Nível Intermediário:
#Missão: Criar um dicionário com nome e uma lista de 3 notas. Calcular e mostrar a média.

profile["Notas"] = [9.5,10.0,10.0]
media = sum(profile["Notas"])/len(profile["Notas"])
print(f"Notas:{profile["Notas"]}\nA média é {media:,.1f}.")

#Nível Avançado:
#Missão: Criar uma lista contendo 3 alunos (dicionários). Percorrer a lista e exibir o nome e nota de cada um.
student1 = {"Aluno":"Li Shen","Notas":[10.0,10.0,10.0]}
student2 = {"Aluno":"Qin Che","Notas":[8.5,7.9,9.0]}
student3 = {"Nome":"Qi Yu","Notas":[7.3,7.0,9.5]}
class_LIS = [student1,student2,student3]

for student in class_LIS:
    print(student)
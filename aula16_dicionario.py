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
    print(f"\n{v}")


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


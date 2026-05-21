# Variáveis Compostas
# nomes = ["Ana", "Rafael", "Gisele", "Isabella"]
# #Python lê os nomes por ordem de índice (0,1,2,3). Sendo assim, para especificar um único cliente e isolá-lo da lista, é necessário
# #puxar a variável+índice que ocupa.
# # print(nomes[3])
# # print(f"A primeira cliente cadastrada foi {nomes[3]}")
# nomes.append("Gilberto")
# #append atualiza a lista com novos nomes.
# # print(nomes)
# nomes[1] = "Larissa"
# #atualiza a lista e muda a posição do novo nome, substituindo o que estava naquele índice anteriormente.
# # print(nomes)
# nomes.pop(0)
# #pop deleta o último nome da lista
# print(nomes)

# ***********************************************
# Duas listas independentes:

#Lista de produtos:
produtos = ["Macarrão","Azeite","Miojo","Paçoca"]
produtos.append("Açúcar")
produtos.insert(2,"Café")
# print("Produtos:",produtos)

print("*****"*10)

tarefas = ["Limpar os armários","Organizar a dispensa","Sonequinha"]
tarefas.append("Ler documentação")
# print("Tarefas:",tarefas)

#Juntar listas e expandir listas:
atividades = produtos + tarefas #criar uma lista com base em listas já existente
print(atividades)
print("*****"*10)
produtos.extend(tarefas) #EXTENDE uma lista com outra lista
print(f"\nProdutos:{produtos}")
print("*****"*10)
atividades.clear()  #limpa toda a lista
print(f"\nLista de atividades: {atividades}")
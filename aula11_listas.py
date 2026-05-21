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
# #atualiza a lista e muda a posição do novo nome.
# # print(nomes)
# nomes.pop(0)
# #pop deleta o último nome da lista
# print(nomes)

# ***********************************************
# Duas listas independentes:

#Lista de produtos:
produtos = ["Macarrão", "Azeite", "Miojo", "Paçoca"]
produtos.append("Açúcar")
print("Produtos:",produtos)
tarefas = ["Limpar os armários", "Organizar a dispensa", "Sonequinha"]
tarefas.append("Ler documentação")
print("Tarefas:",tarefas)
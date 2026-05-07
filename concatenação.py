# Cenário: um jogo que gera relatório final

# jogador = "Ana"
# fase = 5
# tesouros = 3

# # Construindo o relatório
# relatorio = "Relatório da " + jogador + ":\n"
# relatorio = relatorio + "- Fase alcançada: " + str(fase) + "\n"
# relatorio = relatorio + "- Tesouros coletados: " + str(tesouros)

# # Agora posso usar este relatório onde quiser
# print("=== FIM DE JOGO ===")
# print(relatorio)   # mostra
# # guardar em arquivo
# with open("relatorio.txt", "w") as arquivo:
#     arquivo.write(relatorio)  # salva

    # Cenário: catalogo de filme
cliente = "Qi Yu"
rent = "Filmes alugados recentemente"
filme = "Oppenheimer"
ano = 2023
disponibilidade = True

print(type(cliente))
print(type(rent))
print(type(filme))
print(type(ano))
print(type(disponibilidade))

# Construindo o relatório
relatorio = "Relatório do cliente " + cliente + ":\n"
relatorio = relatorio + str(rent) + ":\n"
relatorio = relatorio + "- " +str(filme) + "\n"
relatorio = relatorio + "- Ano: " + str(ano) + "\n"
relatorio = relatorio + "- Disponibilidade: " + str(disponibilidade)

# Agora posso usar este relatório onde quiser
print("=== FIM DE DOCUMENTO ===")
print(relatorio)   # mostra
# guardar em arquivo
with open("relatorio.txt", "w") as arquivo:
    arquivo.write(relatorio)  # salva
# Alistamento Militar: Ana, Jorge e Yago

ano_de_nascimento = int(input("Insira seu ano de nascimento: "))
ano_atual = 2026
idade_atual = (ano_atual - ano_de_nascimento)

print("\nVocê tem",idade_atual,"anos.")

if idade_atual == 18:
    print("\nVocê deve se alistar esse ano.")
elif idade_atual < 18:
    print("\nVocê ainda não tem 18 anos. Faltam",18 - idade_atual, "anos.")
else:
    print("\nVocê já passou do prazo de alistamento por", ano_atual - (ano_de_nascimento + 18), "anos.")
    print(f"\nVocê deveria ter se alistado em {ano_de_nascimento + 18}.")
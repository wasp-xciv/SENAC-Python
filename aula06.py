# Validação de Acesso com Regras Múltiplas:

# idade = 20
# permissao = False
# admin = True

# if (idade >= 18 and permissao) or admin:
# # agrupamento AND: ambas as condições devem ser verdadeiras juntas. Os parênteses garantem que o Python avalie este bloco primeiro.
# # o rota alternativa OR: Se admin for TRUE, a verificação inteira dos parênteses é ignorada e o acesso é liberado.
#     print("Acesso Permitido")
# else:
#     print("Acesso Negado")

# Alistamento Militar:

# ano_de_nascimento = int(input("Insira seu ano de nascimento: "))
# ano_atual = 2026
# idade_atual = (ano_atual - ano_de_nascimento)

# print("\nVocê tem",idade_atual,"anos.")

# if idade_atual == 18:
#     print("\nVocê deve se alistar esse ano.")
# elif idade_atual < 18:
#     print("\nVocê ainda não tem 18 anos. Faltam",18 - idade_atual, "anos.")
# else:
#     print("\nVocê já passou do prazo de alistamento por", ano_atual - (ano_de_nascimento + 18), "anos.")
#     print(f"\nVocê deveria ter se alistado em {ano_de_nascimento + 18}.")

# Alistamento Militar:

# from datetime import date
# ano_de_nascimento = int(input("Insira seu ano de nascimento: "))
# ano_atual = date.today().year
# idade_atual = (ano_atual - ano_de_nascimento)

# print("\nVocê tem",idade_atual,"anos.")

# if idade_atual == 18:
#     print("\nVocê deve se alistar esse ano.")
# if idade_atual == 17:
#     print("\nVocê deve se alistar ano que vem.")
# elif idade_atual < 18:
#     temp_alist = 18 - idade_atual
#     print("\nVocê ainda não tem 18 anos. Faltam",temp_alist, "anos.")
# else:
#     temp_alist = idade_atual - 18
#     print("\nVocê já passou do prazo de alistamento por", temp_alist, "anos.")
#     ano_alist = ano_atual - temp_alist
#     print(f"\nVocê deveria ter se alistado em {ano_alist}.")

#Verificação de Permissão para Dirigir:

from datetime import date
birth = int(input("Insira seu ano de nascimento: "))
current_year = date.today().year
age = (current_year - birth)

print("\nVocê tem ",age,"anos.")

print("\n=== Status Habilitação ===")
print()
if age == 17:
    print("\nVocê não tem a idade mínima para dirigir.\nFalta 1 ano.")
elif age < 18:
    print("\nVocê não tem a idade mínima para dirigir.\nFaltam",18 - age,"anos.")
elif age == 18 and age <= 20:
    print("\nVocê está autorizado a solicitar habilitação para categorias A e B.")
else:
    print("\nVocê está autorizado a solicitar qualquer categoria de habilitação (A, B, C, D e E).")

'''
A solução: try / except ValueError
Com try/except, você tenta fazer algo que pode dar erro e,
se der, você captura o erro e continua o programa com uma mensagem
amigável.
'''
indice = int(input("Digite um número: "))
try:
# código que pode dar erro
    indice = int(input("Digite um número: "))
except ValueError:
# o que fazer se o usuário digitou algo inválido
    print("❗ Digite um número válido.")

'''
Diferença entre except ValueError e except genérico
except ValueError: captura somente erros de conversão de valor (ex.: int("abc")).
except: sem tipo captura qualquer erro, o que pode esconder problemas que você
queria ver (ex.: bugs de lógica).
 '''
#Como tratar erros genéricos (qualquer erro)

try:
    # código que pode dar erro
    x = int("abc")  # erro proposital
except Exception as e:
    print("❗ Ocorreu um erro:", e)

# #1. ZeroDivisionError
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("❗ Não é possível dividir por zero.")

# #2. IndexError
lista = [1, 2, 3]
try:
    print(lista[5])  # índice inválido
except IndexError:
    print("❗ Índice fora do intervalo da lista.")

# #3. TypeError
try:
    soma = "texto" + 10  # não pode somar string com número
except TypeError:
    print("❗ Tipos incompatíveis para operação.")

# #4. FileNotFoundError
try:
    arquivo = open("inexistente.txt", "r")
except FileNotFoundError:
    print("❗ Arquivo não encontrado.")

# #5. KeyError

dados = {"nome": "Ana"}
try:
    print(dados["idade"])  # chave não existe
except KeyError:
    print("❗ Chave não encontrada no dicionário.")
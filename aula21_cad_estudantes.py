"""
Sistema de Cadastro de Estudantes:
"""

# class Estudante:
#     total_estudantes = 0
    
#     def __init__(self,nome,turma,nota1,nota2):
#         self.nome = nome
#         self.turma = turma
#         self.nota1 = nota1
#         self.nota2 = nota2
#         Estudante.total_estudantes +=1

#     def calcular_media(self):
#         return(self.nota1 + self.nota2) / 2
    
#     def situacao(self):
#         media = self.calcular_media()
#         if media >= 7:
#             return f"{self.nome}: Aprovado (media {media:.1f})"
#         else:
#             return f"{self.nome}: Reprovado (media {media:.1f})"
    
#     def exibir_ficha(self):
#         print(f"--- Ficha do Estudante ---")
#         print(f"Nome: {self.nome}")
#         print(f"Turma: {self.turma}")
#         print(f"Média: {self.calcular_media():.1f}")
#         print(self.situacao())

# a1 = Estudante("Ao Yin","CB2601",10,9)
# a2 = Estudante("Li Shen","MED2605",9.5,10)

# a1.exibir_ficha()
# a2.exibir_ficha()
# print(f"\nTotal de estudantes cadastrados: {Estudante.total_estudantes}")

# print(125*"*")

#Agora sem declarar parâmetros:
class Cliente:
    '''
    Classe para representar um cliente. Cadastro de clientes.'''
    def __init__(self):
        '''Inicializa um objeto da classe Cliente com atributos'''
        #attribs
        self.codigo = ""
        self.nome = ""
        self.telefone = ""
        #métodos de instância
    

    def cadastrar_cliente(self):
        '''
        Lógica para cadastrar cliente (não é realmente a melhor...)
        '''
        self.codigo = input("Digite o código do cliente: ")
        self.nome = input("Digite nome do cliente: ")
        self.telefone = input("Digite o telefone do cliente: ")
        print("Cliente cadastrado com sucesso!\n")

    def mostrar_dados(self):
        '''
        Lógica para mostrar os dados do Cliente
        '''
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")

    def atualizar_cliente(self):
        '''
        Lógica para atualizar os dados do cliente
        '''
        self.codigo = input("\nDigite o novo código do cliente: ")
        self.nome = input("Digite o novo nome do cliente: ")
        self.telefone = input("Digite o novo telefone do cliente: ")
        print("Cliente atualizado com sucesso!")

    def excluir_cliente(self):
        '''
        Lógica para excluir cliente
        '''
        select_cod = input("\nDigite o código do cliente que deseja excluir: ")
        if select_cod == self.codigo:
            self.codigo = ""
            self.nome = ""
            self.telefone = ""
            print("Cliente excluído com sucesso!")
        else:
            print("Código do cliente não encontrado.")
        
#Criando o maldito clienteeeeeeeeeeeeeeeeeeee (objeto)

# cliente1 = Cliente()
# cliente1.cadastrar_cliente()
# cliente1.mostrar_dados()
# cliente1.atualizar_cliente()
# cliente1.mostrar_dados()
# cliente1.excluir_cliente()
# cliente1.mostrar_dados()

# cliente2 = Cliente()
# cliente2.cadastrar_cliente()
# cliente2.mostrar_dados()
# cliente2.atualizar_cliente()
# cliente2.mostrar_dados()
# cliente2.excluir_cliente()
# cliente2.mostrar_dados()

#Lista para armazenar vários clientes:
clientes = []

#Loop para cadastrar múltiplos clientes:
# quantidade = int(input("Quantos clientes deseja cadastrar?\n"))

# for c in range(quantidade):
#     print(f"\nCadastro do cliente {c+1}:")
#     cliente = Cliente() #cria um novo cliente vazio
#     cliente.cadastrar_cliente()
#     clientes.append(cliente) #adiciona na lista

#Mostrar todos os clientes cadastrados
# print("\n---Lista de Clientes Cadastrados---")
# for cliente in clientes:
#     cliente.mostrar_dados()

#Como usar uma função para buscar o cliente pelo código?
def buscar_cliente(codigo):
    for cliente in clientes:
        if cliente.codigo == codigo:
            return cliente
        return None

#Menu Principal
while True:
    print("\n---MENU DE CLIENTES---")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Atualizar Cliente")
    print("4 - Excluir Cliente")
    print("5 - Sair")

    opcao = input("Escolha uma opção:\n")

    if opcao == "1":
        cliente = Cliente()
        cliente.cadastrar_cliente()
        clientes.append(cliente)
    
    elif opcao == "2":
        if clientes:        #"se" a lista "clientes" não está vazia...
            print("\n---Lista de Clientes---")
            for cliente in clientes:
                cliente.mostrar_dados()
        else:
            print("Nenhum cliente cadastrado（︶^︶）")

    elif opcao == "3":
        codigo = input("Digite o código do cliente que deseja atualizar:\n")
        cliente = buscar_cliente(codigo)
        if cliente:
            cliente.atualizar_cliente()
        else:
            print("Cliente não encontrado（︶^︶）")

    elif opcao == "4":
        cliente.excluir_cliente()
        clientes.remove(cliente)
    
    elif opcao == "5":
        print("Saindo do sistema...ヾ(￣▽￣) Bye~Bye~")
        break
    
    else:
        print("Opção inválida. Tente novamente!（︶^︶）")



# class Gatos:
#     def __init__(self):
#         self.nome = ""
#         self.idade = ""
#         self.pelagem = ""
#         self.tutor = ""
#         self.vacina = False

#     def cadastrar_gato(self):
#         self.nome = input("Digite nome do gato: ")
#         self.idade = int(input("Digite a idade do gato: "))
#         self.pelagem = input("Digite a pelagem: ")
#         self.tutor = input("Digite o nome do tutor: ")

#     def vacinacao(self):
#         doses = input("O gato já foi vacinado esse ano?\n(S/N): ")
#         if doses == "S":
#             self.vacina = True

#     def mostrar_dados(self):
#         print("\n--- Dados do animal ---")
#         print(f"\nGato: {self.nome}\nIdade: {self.idade} anos\nPelagem: {self.pelagem}\nTutor: {self.tutor}\nVacinado: {self.vacina}")

# gato1 = Gatos()
# gato1.cadastrar_gato()
# gato1.vacinacao()
# gato1.mostrar_dados()
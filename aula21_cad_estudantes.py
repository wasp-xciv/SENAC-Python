"""
Sistema de Cadastro de Estudantes:
"""

class Estudante:
    total_estudantes = 0
    
    def __init__(self,nome,turma,nota1,nota2):
        self.nome = nome
        self.turma = turma
        self.nota1 = nota1
        self.nota2 = nota2
        Estudante.total_estudantes +=1

    def calcular_media(self):
        return(self.nota1 + self.nota2) / 2
    
    def situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return f"{self.nome}: Aprovado (media {media:.1f})"
        else:
            return f"{self.nome}: Reprovado (media {media:.1f})"
    
    def exibir_ficha(self):
        print(f"--- Ficha do Estudante ---")
        print(f"Nome: {self.nome}")
        print(f"Turma: {self.turma}")
        print(f"Média: {self.calcular_media():.1f}")
        print(self.situacao())

a1 = Estudante("Ao Yin","CB2601",10,9)
a2 = Estudante("Li Shen","MED2605",9.5,10)

a1.exibir_ficha()
a2.exibir_ficha()
print(f"\nTotal de estudantes cadastrados: {Estudante.total_estudantes}")

print(125*"*")

#Agora sem declarar parâmetros:
class Cliente:
    def __init__(self):
        #attribs
        self.codigo = ""
        self.nome = ""
        self.telefone = ""
        #métodos de instância
    
    def cadastrar_cliente(self):
        #Lógica para cadastrar cliente (não é realmente a melhor...)
        self.codigo = input("Digite o código do cliente: ")
        self.nome = input("Digite nome do cliente: ")
        self.telefone = input("Digite o telefone do cliente: ")
        print("Cliente cadastrado com sucesso!\n")

    def mostrar_dados(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
    
    def atualizar_cliente(self):
        #Lógica para atualizar os dados do cliente
        self.codigo = input("\nDigite o novo código do cliente: ")
        self.nome = input("Digite o novo nome do cliente: ")
        self.telefone = input("Digite o novo telefone do cliente: ")
        print("Cliente atualizado com sucesso!")

    def excluir_cliente(self):
        select_cod = input("\nDigite o código do cliente que deseja excluir: ")
        if select_cod == self.codigo:
            self.codigo = ""
            self.nome = ""
            self.telefone = ""
            print("Cliente excluído com sucesso!")
        else:
            print("Código do cliente não encontrado.")
    
#Criando o maldito clienteeeeeeeeeeeeeeeeeeee

cliente1 = Cliente()
cliente1.cadastrar_cliente()
cliente1.mostrar_dados()
cliente1.atualizar_cliente()
cliente1.excluir_cliente()

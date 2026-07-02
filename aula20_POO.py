'''
Classe = molde
Objeto = algo criado a partir do molde

Analogia:
Classe Aluno -> alunos Shen Li, Qi Yu, Xia Yazhou (objetos)
'''

# Criando um objeto da classe Aluno

class Aluno:
    pass #segue o código a se fazer

aluno1 = Aluno()
aluno2 = Aluno()

#Atribb (dados dos objetos) são as características do objeto.

aluno1.nome = "Ana"
aluno1.idade = 17

print(aluno1.nome)
print(aluno1.idade)

#Método __init__(construtor). Trata-se de um método especial que roda quando o objeto é criado.
#Ele é usado para inicializar os atributos do objeto.

class Aluno:
    def __init__(self,nome,idade,endereco,email,sexo): #método construtor
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.email = email
        self.sexo = sexo
        #self é uma referência ao próprio objeto. Ele é usado para acessar os atribb e métodos do objeto.

    def mostrar_dados(self):
        print("Nome: ",self.nome)
        print(f"Idade: {self.idade} anos")
        print("Endereço: ",self.endereco)
        print("Email: ",self.email)
        print("Sexo: ",self.sexo)

aluno1 = Aluno("Shen Li",27,"Rua A, 123","aksocardio@linkon.com","M")
aluno2 = Aluno("Xia Yazhou", 25,"Rua B, 456","daacolonel@ever.com","M")

print(f"Aluno 1: {aluno1.nome}\nIdade:{aluno1.idade} anos\nEndereço:{aluno1.endereco}\nContato:{aluno1.email}\nSexo:{aluno1.sexo}")

aluno2.mostrar_dados()

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


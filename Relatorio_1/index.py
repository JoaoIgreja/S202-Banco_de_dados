class Professor:
    def __init__(self, nome):#Função especial(__)
        self.nome = nome
    
    def ministrar_aula(self, assunto):
        return f"O professor {self.nome} esta ministrando uma aula sobre {assunto}."'\n'

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        return f"O aluno {self.nome} esta presente."

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno) #(append é um método utilizado para adicionar elementos a uma lista/array)
    
    def listar_presenca(self):
        presenca_alunos = '\n'.join([aluno.presenca() for aluno in self.alunos]) #(.join é utilizado para concatenar elementos de uma sequência)
        return f"Presenca na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n{presenca_alunos}"

# Exemplo de uso
professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")

aula = Aula(professor, "Programacao Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)

print(professor.ministrar_aula(aula.assunto))
print(aula.listar_presenca())

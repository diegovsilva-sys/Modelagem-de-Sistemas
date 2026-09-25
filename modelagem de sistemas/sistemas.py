
# Definir a classe Aluno
class Aluno:

    # Método construtor
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    # Método para mostrar dados
    def mostrar_dados(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Curso: ", self.curso)


# Criando alunos (usando a classe Aluno)
aluno1 = Aluno("João", 18, "Informática")
aluno2 = Aluno("Maria", 19, "Administração")

# Mostra alunos
print("=== Dados dos Alunos ===")
aluno1.mostrar_dados()

print("\n")
aluno2.mostrar_dados()
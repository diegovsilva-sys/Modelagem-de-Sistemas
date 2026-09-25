class Professor:
    def __init__(self, nome, endereço , quantidade_de_turmas):
        self.nome = nome
        self.endereço = endereço
        self.quantidade_de_turmas = quantidade_de_turmas

    def mostrar_dados(self):
        print("Nome: ", self.nome)
        print("Endereço: ", self.endereço)
        print("Quantidade de turmas: ", self.quantidade_de_turmas)

professor1 = Professor("Carla", "Rua-Cleriston Andrade, 340", 5 )
professor2 = Professor("Pedro", "Rua-Dom Pedro I, 58", 3)
professor3 = Professor("João", "Bairro-Santo Ântonio de Jesus, 278", 2)

print("=== Dados dos Professores ===")
professor1.mostrar_dados()

print("\n")
professor2.mostrar_dados()
print("\n")

professor3.mostrar_dados()
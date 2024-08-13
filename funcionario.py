class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade 
        self.salario = salario

    def exibir_detalhes(self):
        return("Nome: {}, Idade: {}, Salário: R${}" .format(self.nome, self.idade, self.salario))

    def calcular_bonus(self):
        return 'Implementação específica da classes filhas'
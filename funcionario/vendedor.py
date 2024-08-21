from funcionario import Funcionario

#Classe Filha 2 - Vendedor
class Vendedor(Funcionario):
    def __init__(self, nome, idade, salario, comissao):
        super().__init__(nome, idade, salario)
        self.comissao = comissao

    def calcular_bonus(self):
        return(self.salario * 0.05) + self.comissao

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f'{detalhes}, Comissão: R${self.comissao:.2f}, Bonus: R${self.calcular_bonus():.2}'

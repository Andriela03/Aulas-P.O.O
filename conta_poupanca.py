from conta_bancaria import Conta_bancaria

class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, saldo, taxa_rendimento):
        super().__init__(titular, cpf, saldo)
        self.taxa_rendimento = taxa_rendimento 

    def calcular_rendimento(self):
        rendimento = self.saldo * (self.taxa_rendimento / 100)
        return f'Rendimento da conta: {rendimento:.2f}'

    def aplicar_rendimento(self):
        rendimento = self.saldo * (self.taxa_rendimento / 100)
        self.saldo += rendimento
        return f'Rendimento de {rendimento:.2f} aplicado. Novo saldo: {self.saldo:.2f}'
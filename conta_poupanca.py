from conta_bancaria import Conta_bancaria

class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, saldo, redimento):
        super().__init__(titular, cpf, saldo)
        self.redimento = redimento 

    def ver_redimento(self):
        return f'Redimento da conta: {self.ver_redimento}'

    def render(self, redimento):
        self.render = redimento * (2/100)









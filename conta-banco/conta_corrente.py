from conta_bancaria import Conta_bancaria

class Conta_corrente(Conta_bancaria):
    def __init__(self, titular, cpf, saldo, numerocc):
        super().__init__(titular, cpf, saldo)
        self.numerocc = numerocc


    def mostrarcc(self, numerocc):
        self.mostrarcc = numerocc
        return self.numerocc







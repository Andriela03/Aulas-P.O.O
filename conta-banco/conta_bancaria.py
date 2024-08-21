class Conta_bancaria:
    def __init__(self, titular, cpf, saldo):
        self.titular = titular 
        self.cpf = cpf
        self.saldo = saldo 

    def mostrar_conta(self):
        return f'Titular: {self.titular} CPF: {self.cpf} Saldo: {self.saldo:.2f}'
    
    def depositar(self, valor):
        valor += self.saldo
        return f'O valor de {valor:.2f} foi depositado com sucesso. Saldo atual: {self.saldo:.2f}'

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f'Você sacou {valor:.2f}. Saldo restante: {self.saldo:.2f}'
        else:
            return 'Você não possui saldo suficiente para esse saque.'

    def verificar_saldo(self):
        return f'Saldo: {self.saldo:.2f}'

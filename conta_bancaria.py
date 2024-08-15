class Conta_bancaria:
    def __init__(self, titular, cpf, saldo):
        self.titular = titular 
        self.cpf = cpf
        self.saldo = saldo 

    def mostrar_conta(self):
        return f'Titular: {self.titular} CPF:{self.cpf} Saldo{self.saldo:.2f}'
    
    def depositar(self, depositar):
        self.depositar = depositar
        self.depositar = self.saldo + depositar 
        return f'O valor a ser depositado é: {self.depositar}'


    def sacar(self, sacar):
        if sacar <= self.saldo:
            self.sacar =  self.saldo - sacar 
            return f'Valor sacado {self.sacar:.2f}'

        else:
            print('Você não possui esse valor em seu saldo')

    def verificar_saldo(self):
        return f'Saldo: {self.saldo}'





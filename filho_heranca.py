from pessoa import *
class Professor(Pessoa):
    def __init__(self, nome, endereco, telefone, email, salario):
        super().__init__(nome, endereco, telefone, email)
        self.__salario = salario

    def get_salario(self):
        return(self.__salario)

    def set_salario(self, salario):
        self.__salario = salario
        return("Sucesso")

exemplo = Professor("Elouise", "rua galdino", "(84)9999-9999", "luizinhadograu06@gmail.com", '200.000,00')
print(exemplo.get_nome())
print(exemplo.get_salario())
print(exemplo.get_endereco())
print(exemplo.get_telefone())


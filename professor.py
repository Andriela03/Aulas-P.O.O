from filho_heranca import *
class Professor_substituto(Professor):
    def __init__(self, nome, endereco, telefone, email, salario, tempo_contrato):
        super().__init__(nome, endereco, telefone, email, salario)
        self.__tempo_contrato = tempo_contrato

    def mostrar_professor (self):
        print(self.get_nome())
        print(self.get_email())
        print(self.__tempo_contrato)

professora1 = Professor_substituto("Elouise", "Rua André Matias", "(84) 99999-9999", "luizinhadograu06@gmail.com")
    


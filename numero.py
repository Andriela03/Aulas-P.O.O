class Numero:
    def __init__(self, num):
        self.num = num

    def sucessor(self):
        valor = self.num + 1 
        print(f'O sucessor de {self.num} é {valor}')

    def antecessor(self):
        valor = self.num - 1 
        print(f'O antecessor de {self.num} é {valor}')

    def dobro(self):
        valor = self.num * 2 
        print(f'O dobro de {self.num} é {valor}')

    def triplo(self):
        valor = self.num * 3 
        print(f'O triplo de {self.num} é {valor}')

    def metade(self):
        valor = self.num/2
        print(f'O metade de {self.num} é {valor}')


numero1 = Numero(2)
numero1.sucessor()
numero1.antecessor()
numero1.dobro()
numero1.triplo()
numero1.metade()


numero2 = Numero(8)
numero2.sucessor()
numero2.antecessor()
numero2.dobro()
numero2.triplo()
numero2.metade()




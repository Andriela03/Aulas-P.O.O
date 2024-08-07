class Cofrinho:

    def __init__(self, valor, meta):
        self.valor = valor
        self.meta = meta 
    
    def adicionar(self, quantia):
        self.valor = self.valor + quantia

    def falta(self):
        if self.meta ==  self.valor:
            print('Parabéns, você chegou na meta')
        elif self.valor > self.meta:
            print('Você ultrapassou a sua meta')
        else:
            x = self.meta - self.valor
            print("Falta {} para os {} da sua meta".format(x, self.meta))
    
meta_rennan = Cofrinho(7000, 20000)
meta_rennan.adicionar(400)
meta_rennan.falta()
meta_rennan.adicionar(350)
meta_rennan.falta()
meta_rennan.adicionar(15000)
meta_rennan.falta()
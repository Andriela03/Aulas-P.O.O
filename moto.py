class Moto:
    def __init__(self, marca, modelo, cilindradas):
        self.marca = marca
        self.modelo = modelo
        self.cilindradas = cilindradas 
    
    def dados(self):     
        print('A moto {} possui {} cilindradas.' .format(self.modelo, self.cilindradas))

moto1 = Moto('Honda', 'Honda CB 500F', 500)
moto1.dados('Honda', 500)
print('Marca: {} \nModelo: {} \nCilindradas: {}' .format(moto1.marca, moto1.modelo, moto1.cilindradas))

moto2 = Moto('Yamaha','Yamaha YZF-R6', 600)
moto2.dados('Yamaha', 600)
print('Marca: {} \nModelo: {} \ncilindradas: {}' .format(moto2.marca, moto2.modelo, moto2.cilindradas))

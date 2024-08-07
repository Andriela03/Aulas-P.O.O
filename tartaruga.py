class Tartaruga:
    def __init__(self, nome, posicao_x, posicao_y):
        self.nome = nome 
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        
    def andar_pra_frente(self, passos):
        self.posicao_x = self.posicao_x + passos

    def onde_estou(self):
        print('Eu sou a tartaruga', self.nome, "Estou na posição X:", self.posicao_x, ' Y: ', self.posicao_y)
    
    def andar_pra_tras(self):


tartaruga = Tartaruga('Moana', 0, 0)
tartaruga.onde_estou()
tartaruga.andar_pra_frente(10)
tartaruga.onde_estou()
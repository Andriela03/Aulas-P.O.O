class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome 
        self.__preco = preco 
        self.__quantidade = quantidade
        
    def get_nome(self):
        return self.__nome 
    
    def get_preco(self):
        return self.__preco
    
    def get_quantidade(self):
        return self.__quantidade
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_preco(self, preco):
        if self.__preco >= 0:
            self.__preco = preco
        
    def set_quantidade (self, quantidade):
        if self.__quantidade >= 0:
            self.__quantidade = quantidade 
            
    
        
         
        
        
         
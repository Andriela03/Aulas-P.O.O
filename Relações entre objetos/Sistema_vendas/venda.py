from produto import Produto

class Venda(Produto):
    def __init__(self, nome, preco, quantidade, dataVenda):
        super().__init__(nome, preco, quantidade)
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = 0.0
        
    def get_produtos(self):
        return self.__produtos
    
    def get_dataVenda(self):
        return self.__dataVenda
    
    def get_total(self):
        return self.__total
    
    def set_produtos(self, produtos):
        self.__produtos = produtos
        
    def set_dataVenda(self, dataVenda):
            self.__dataVenda = dataVenda
        
    def set_total(self, total):
        self.__total = total
        
    def calcularTotal(self):
        self.total = sum(produto.get_preco() for produto in self.__produtos)
        
    def adicionar_produto(self, produto):
        self.__produtos.append(produto)
        self.calcularTotal()
        
    def  remover_produto(self, nome):
        for produto in self.__produtos:
         if produto.get_nome() == nome:
             self.calcularTotal()
             return True
        return False
    
    def listar_produtos(self):
        return self.__produtos


    
    
             
from autor import Autor

class Livro(Autor):
    def __init__(self, nome, nacionalidade, data_nascimento, titulo, anoPublicacao):
        super().__init__(nome, nacionalidade, data_nascimento)
        self.__titulo = titulo
        self.__anoPublicacao = anoPublicacao

    def get_titulo(self):
        return self.__titulo

    def get_anoPublicacao(self):
        return self.__anoPublicacao

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_anoPublicacao(self, anoPublicacao):
        self.__anoPublicacao = anoPublicacao

    def exibir_livro(self):
        print(f'Título: {self.__titulo}')
        print(f'Autor: {self.__nome}')
        print(f'Ano de Publicação: {self.__anoPublicacao}')
    



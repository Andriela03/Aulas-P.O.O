from livro import Livro

class Biblioteca(Livro):
    def __init__(self, nome, nacionalidade, data_nascimento, titulo, autor, anoPublicacao):
        super().__init__(nome, nacionalidade, data_nascimento, titulo, autor, anoPublicacao)
        self.__livros = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def buscar_livro(self, titulo):
        for livro in self.__livros:
            if livro.get_titutlo().lower() == titulo.lower():
                return livro
        return None

    def remover_livro(self, titulo):
        livro = self.buscarLivro(titulo)
        if livro:
            self.__livros.remove(livro)
            return True
        return False

    def listar_livros(self):
        if not self.__livros:
            print('Você não possui esse livro em sua biblioteca.')
        else:
            for livro in self.__livros:
                livro.exibirLivro()




       

    
from livro import Livro

class Biblioteca(Livro):
    def __init__(self, nome, nacionalidade, dataNascimento, titulo, autor, anoPublicacao, livros):
        super().__init__(nome, nacionalidade, dataNascimento, titulo, autor, anoPublicacao)
        self.__livros = []

    def adicionarLivro(self, livro):
        self.__livros.append(livro)

    def buscarLivro(self, titulo):
        for livro in self.__livros:
            if livro.get_titutlo().lower() == titulo.lower():
                return livro
        return None

    def removerLivro(self, titulo):
        livro = self.buscarLivro(titulo)
        if livro:
            self.__livros.remove(livro)
            return True
        return False

    def listarLivros(self):
        if not self.__livros:
            print('Você não possui esse livro em sua biblioteca.')
        else:
            for livro in self.__livros:
                livro.exibirLivro()




       

    
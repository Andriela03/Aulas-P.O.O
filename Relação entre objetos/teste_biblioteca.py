from autor import Autor
from livro import Livro
from biblioteca import Biblioteca

def novo_livro():
    titulo = str(input('Digite o título do livro: '))
    nome = str(input('Digite o nome do autor: '))
    nacionalidade = str(input('Digite a nacionalidade do livro: '))
    anoPublicacao = int(input('Digite o ano que o livro foi publicado: '))
    
    return Livro(titulo, nome, nacionalidade, anoPublicacao)

    
    
    

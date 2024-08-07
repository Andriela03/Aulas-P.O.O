class Livros:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor 
        self.paginas = paginas 
    
    def informacoes (self):
        print('O livro {}  do autor {} possui {} paginas \n' .format(self.titulo, self.autor, self.paginas))

livro1 = Livros('Harry Potter e a Pedra Filosofal', 'J.K Rowling', 323)
livro1.informacoes()
livro1.paginas = 223
livro1.informacoes()
print('Livro: {} \nAutor: {} \nPáginas: {} \n' .format(livro1.titulo, livro1.autor, livro1.paginas))


livro2 = Livros('A culpa é a das Estrelas', 'John Green', 313)
livro2.informacoes()
print('Livro: {} \nAutor: {} \nPáginas: {}\n' .format(livro2.titulo, livro2.autor, livro2.paginas))


livro3 = Livros('A menina que roubava livros','Markus Zusak', 596 )
livro3.informacoes()
print('Livro: {} \nAutor: {} \nPáginas: {}' .format(livro3.titulo, livro3.autor, livro3.paginas))



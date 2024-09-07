from autor import Autor
from livro import Livro
from biblioteca import Biblioteca

def criar_livro():
    titulo = input('Digite o título do livro: ')
    nome = input('Digite o nome do autor: ')
    data_nascimento = int(input('Digite a data de nascimento do autor: '))
    nacionalidade = input('Digite a nacionalidade do autor: ')
    anoPublicacao = int(input('Digite o ano que o livro foi publicado: '))
    
    nome = Autor(nome, nacionalidade, data_nascimento)
    return Livro(titulo, nome, nacionalidade, anoPublicacao)

def exibir_menu():
    print('*** BEM-VINDO! ***')
    print('MENU:')
    print('1. Adicionar um novo livro')
    print('2. Remover um livro')
    print('3. Buscar um novo livro')
    print('4. Listar todos os livros disponíveis')
    print('5. SAIR')

biblioteca = Biblioteca()

while True:
    exibir_menu()
    opcao = input('O que deseja fazer? ')
    
    if opcao == '1':
        livro = criar_livro()
        biblioteca.adicionar_livro(livro)
        print('Adicionado com sucesso!')
        
    elif opcao == '2':
        titulo = input('Digite o título do livro que deseja remover: ')
        if biblioteca.remover_livro(titulo):
            print('O livro foi removido com sucesso!')
        else:
            print('Livro não encontrado.')
            
    elif opcao =='3':
        titulo = input('Digite o título do livro que deseja buscar: ')
        livro = biblioteca.buscar_livro(titulo)
        if livro:
            livro.exibir_livro()
        else:
            print('Livro não encontrado.')
            
    elif opcao == '4':
        biblioteca.listar_livros()
        
    elif opcao == '5':
        print('Saindo...')
        break
    
    else:
        print('Opção inválida. Tente novamente.')
           
    



    
    
    

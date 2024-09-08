from produto import Produto
from venda import Venda

def criar_produtos():
    nome = input('Digite o nome do produto: ')
    preco = input('Digite o preço do produto: ')
    quantidade = int(input('Quantidade de produtos: '))
    
    venda = Venda(nome, preco, quantidade)
    venda.criar_produtos(produto)
    
    
def exibir_menu():
    print('*** BEM-VINDO ***')
    print('MENU:')
    print('1. Adicionar um novo produto')
    print('2. Remover um produto da venda')
    print('3. Listar produtos')
    print('4. Mostrar total da venda')
    print('5. SAIR')
    

vendas = Venda()

while True:
    exibir_menu()
    opcao = input('O que deseja fazer? ')
    
    if opcao == '1':
        produto = criar_produtos()
        vendas.adicionar_produto(produto)
        print('Adicionado com sucesso!')
       
    if opcao == '2':
        nome = input("Nome do produto a ser removido: ")
        if vendas.remover_produto(nome):
            print(f"Produto {nome} removido com sucesso!")
        else:
            print(f"Produto {nome} não encontrado!")
        
    if opcao == '3':
        produto.listar_produtos()
        
    if opcao == '4':
        total = vendas.calcularTotal()
        print(f"Total da venda: R$ {total:.2f}")
        
    elif opcao == '5':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
        
        
        
        
        
    
    
    
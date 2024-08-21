from funcionario import Funcionario
from vendedor import Vendedor
from gerente import Gerente

print('*** Bem-vindo ao RH ***')
print('1)Cadastrar novo funcionário')
print('2)Listar funcionário da empresa')
print('3)SAIR')

lista_de_funcionario = []


opcao = int(input('Digite a sua opção: '))
while opcao != 3:
    #O usuário digitou a opção de cadastrar novo funcionário
    if opcao == 1:
        nome = input('Informe o nome do funcionário:')
        idade = int(input('Informe a idade do funcionário: '))
        salario = float(input("Informe o salário do funcionário"))
        tipo = int(input('Informe o teipo de funcionário: '))


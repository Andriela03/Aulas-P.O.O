from conta_bancaria import Conta_bancaria
from conta_corrente import Conta_corrente
from conta_poupanca import Conta_poupanca

print('***Bem-vindo ao banco do Brasil***')
print("1) Cadastrar conta corrente")
print("2) Cadastrar conta poupança")
print("3) SAIR")

opcao = int(input('Digite sua opção: '))
while (opcao != 3):

    if opcao == 1:
        titular = str(input('Digite seu nome completo: '))
        cpf = int(input("Digite o seu CPF: "))
        print('Sua conta corrente já está pronta para o seu uso!!')
        opcoes = int(input('Informe o que deseja fazer: 1) Sacar 2) Depositar 3) Ver o saldo 4) SAIR'))
        if opcoes == 1:








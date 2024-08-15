from conta_bancaria import Conta_bancaria
from conta_corrente import Conta_corrente
from conta_poupanca import Conta_poupanca

print('***Bem-vindo ao banco do Brasil***')
print("1) Entrar")
print("2) Cadastrar uma conta")

opcao = int(input('Digite sua opção: '))
while (opcao != 3):

    if opcao == 1:
        titular = str(input('Digite seu nome completo: '))
        cpf = int(input("Digite o seu CPF: "))
        n_conta = float(input('Digite o número da sua conta: '))
        print(f'Seja bem-vindo {titular}')
        opcoes = int(input('Informe o que deseja fazer: 1) Sacar \n 2) Depositar \n 3) Ver o saldo \n 4) Conta Corrente \n 5) Conta Poupança \n 6) SAIR'))

        if opcoes == 1:
            sacar = float(input('Informe quanto você quer sacar: '))
            print(Conta_bancaria.sacar())

        elif opcoes == 2:
            depositar = float(input('Quanto você deseja depositar?'))
            print(Conta_bancaria.depositar())
            print('O valor foi depositado com sucesso')

        elif opcoes == 3:
            Conta_bancaria.saldo()
        elif opcoes == 4:
            print('Informações da sua conta corrente:', Conta_corrente.mostrarcc(n_conta))

        elif opcoes == 5:
            print('Rendimento da sua conta: ', Conta_poupanca.ver_rendimento())

    if opcao == 2:
        titular = str(input('Digite seu nome completo: '))
        cpf = int(input("Digite o seu CPF: "))
        print('Sua conta foi cadastrada com sucesso!!')
        print(f'Seja bem-vindo {titular}')
        opcoes = int(input('Informe o que deseja fazer: 1) Sacar \n 2) Depositar \n 3) Ver o saldo \n 4) Conta Corrente \n 5) Conta Poupança \n  6) SAIR'))
            
        if opcoes == 1:
            sacar = float(input('Informe quanto você quer sacar: '))
            print(Conta_bancaria.sacar())

        elif opcoes == 2:
            depositar = float(input('Quanto você deseja depositar?'))
            print(Conta_bancaria.depositar())
            print('O valor foi depositado com sucesso')

        elif opcoes == 3:
            Conta_bancaria.saldo()
        elif opcoes == 4:
            print('Informações da sua conta corrente:', Conta_corrente.mostrarcc(n_conta))

        elif opcoes == 5:
            redimento = float(input('Aplique um redimento na sua conta:'))
            print('Rendimento da sua conta: ', Conta_poupanca.render())

    elif opcoes !=3:
        print('***OPÇÃO INVÁLIDA***')

print('***Bem-vindo ao banco do Brasil***')
print("1) Entrar")
print("2) Cadastrar uma conta")

opcao = int(input('Digite sua opção: '))




        














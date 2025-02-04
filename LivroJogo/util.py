class JogoUtil: 
    @staticmethod
    def exibir_opcoes(opcoes):
        for i, opcao in numerate(opcoes, 1):
            print(f'{i}. {opcao}')

@staticmethod
def fazer_escolha(opcoes): 
    while True:
        try:
            escolha = int(input('\n Escolha uma opção:')) - 1
            if 0 <= escolha < len(opcoes):
                return escolha
            else:
                print('Ops!... Tente novamente.')     
        except ValueError:
            print("Escolha inválida. Tente novamente")
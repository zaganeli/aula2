from funcao5 import converter_metros_para_centimetros
from funcao6 import calcular_area_circulo
from funcao7 import calcular_area_quadrada

def menu():
    while True:
        print('\n -- Menu de Opções --')
        print('1 - Converter metros para centímetros')
        print('2 - Calcular area do circulo')
        print('3 - Calcular area dobrada do quadrado')
        print(' 0 - Sair')

        opcao = input('Escolha uma opção:  ')
        if opcao == '1':
            converter_metros_para_centimetros()
        elif opcao == '2':
            calcular_area_circulo()
        elif opcao == '3':
            calcular_area_quadrada()
        elif opcao == '0':
            print('Saindo do programa! Até logo!')
            break
        else:
            print('Opção Inválida!! - Tente Novamente....')

#iniciar o Menu
if __name__== "__main__":
    menu()












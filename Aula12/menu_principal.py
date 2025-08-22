

import runpy


def menu():
    while True:
        print('\n -- Menu de Opções --')
        print('1 - Converter metros para centímetros')
        print('2 - Calcular area do circulo')
        print('3 - Calcular area dobrada do quadrado')
        print(' 0 - Sair')

        opcao = input('Escolha uma opção:  ')
        if opcao == '1':
           #runpy.run_path("5.py")
            exec(open("5.py").read())
        elif opcao == '2':
            exec(open("6.py").read())
           # runpy.run_path("6.py")
            exec(open("7.py").read())
        elif opcao == '3':
           #runpy.run_path("7.py")
        elif opcao == '0':
            print('Saindo do programa! Até logo!')
            break
        else:
            print('Opção Inválida!! - Tente Novamente....')

#iniciar o Menu
if __name__== "__main__":
    menu()



























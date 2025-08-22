""" enunciados (referencia)

Exercício 5: Faça um Programa que converta metros para centímetros.
Exercício 6: Faça um Programa que peça o
raio de um círculo, calcule e mostre sua área.
Exercício 7:Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário."""

def converter_metros_para_centimetros():
    metros = float(input('Metros:'))
    centimetros= metros * 100
    print(f'{metros} m = {centimetros} cm')
          
def calcula_area_circulo():
    raio = float(input('Informe o raio de um circulo: '))
    area = float((raio**2) * 3.14) # (A = π r²) pi=3,1415
    print(f'Coim um circulo de raio {raio} temos u, circulo de area {area}.')


def menu():
    while True:
        print('\n -- Menu de Opções')
        print('1- Converter metros para centimetros')
        print('2- Calcular área do Círculo') 
        print('0- Sair')

        opcao = input('Escolha uma opção')
        if opcao == '1':
            converter_metros_para_centimetros()
        elif opcao =='2':
           calcula_area_circulo()
        elif opcao =='0':
            print('Saindo do programa.até logo !')
            break
        else:
            print('Opção inválida! - Tente novamente')
            # Iniciar Menu
menu()




















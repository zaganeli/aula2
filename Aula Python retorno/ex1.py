"""Faça um programa que peça uma nota, entre zero e dez.Mostre uma mensagem caso o valor seja invalido e continue pedindo até que o ususario informe um valor valido."""

while True:
    nota = int(input('Digite uma nota entre [0 e 10]')) 
    if nota < 0 or nota > 10:
        print('Digite um valor válido')
    else:
        print('Você digitou um valor válido')
        break








































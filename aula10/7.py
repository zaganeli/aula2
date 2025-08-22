"""7.  Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.   """

vetor = []
soma = multiplicacao= 0

for i in range(5):
    n = int(input(f'digite o {i+1}° Numero'))
vetor.append(n)
#soma = soma + n
soma += n 
multiplicacao*=n

print('Os números são ....')
for i in range(5):
    print(f'{i+1}° Número : {vetor[i]}')
    print(f'A soma é {soma} e a m1 multiplicação {multiplicacao}')

























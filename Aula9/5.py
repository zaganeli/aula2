"""5.  Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

vetor = []
vetorpar = []
vetorimpar = []

for i in range(5):
    n = int(input(f'Digite o {i+1}° numero'))
    vetor.append(n)
    if n % 2 == 0:
        vetorpar.append(n)
    else:
        vetorimpar.append(n)
# imprimir os dados dos vetoress
print(f'Vetor {vetor}')      
print(f'Vetor Par {vetorpar}') 
print(f'Vetor {vetorimpar}')
































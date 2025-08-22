""""4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. """
# vogais = ['a','e','i','o','u']
# consoantes = []

# for i in range(10):
#     v = (input(f'Digite as consoantes: ')).lower()

#     if len(v) == 1 and v.isalpha() and v not in vogais:
#      consoantes.append(v)
     
# print('----------')

# print('A quantidade de consoantes é igual a: ',len(consoantes))

vetor = []
total = 0

for i in range(10):
    letra = input(f'Digite a {i+1}º letra ==>   ')
    vetor.append(letra)
    if letra.isalpha() and letra not in 'aeiou':
        total += 1
        print(f'letra{vetor[i]}')
print(f'Foi informado {total} consoantes')




































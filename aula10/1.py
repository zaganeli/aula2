"""6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. """
nmaior7 = 0
vetormedia = []
# range 3 é o total de alunos
for i in range(3):# para não criar um teste logo coloquei 3
# faixa de notas ==> 4 [0,1,2,3]
    for j in range(4):
        nota = float(input(f'Digite a {j+1}° Nota do {i+1}° Aluno'))
        soma =soma + nota
    vetormedia.append(media)
    
    for i in range(3):
        if  vetormedia[i] >=7:
            nmaior7 = nmaior7 +1
        #nmaior7 +=1
        print(f'A quantidade de alunos que tiveram nota maior que 7 foi {nmaior7}')





















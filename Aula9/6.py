"""" 6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

vetormedia = []
soma = media = nota = 0
for i in range(3): #total de alunos alterado de 10 para 3
    for j in range(4): # 4 notas para cada aluno,faixa de 4 sendo 1  para cada nota
        nota = float(input(f'digite a {j+1}° nota do {i+1}° Aluno'))
        soma = soma + nota
        media = soma/4
        vetormedia.append(media)
        soma = 0 # inicializar a soma senão irá acumular





























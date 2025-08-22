"""Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';.
 """
# entrada do nome
nome = input('Digite o nome')
while len(nome)<3:
     print('Nome invalido! Redigite o nome')
         nome = input('Digite o seu nome')
     # entrada idade
     idade = int(input('Digite a idade')) 
     # validação da idade
     while idade<0 or idade>150:
          print('Idade invalida! Redigite Idade')
          idade + int(input('Digite a idade[0 - 150]'))









































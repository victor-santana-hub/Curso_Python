# Desafio 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Insira um número inteiro: '))
div = num % 2

if div == 0:
    print('O número digitado é PAR.')
else:
    print('O número digitado é ÍMPAR.')

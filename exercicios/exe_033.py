# Desafio 033 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Insira um ano: '))
n = ano % 4

if n == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))

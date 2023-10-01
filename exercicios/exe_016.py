# Desafio 016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

num = float(input('Digite um número real qualquer: '))

print('A parte inteira é: {}'.format(math.trunc(num)))

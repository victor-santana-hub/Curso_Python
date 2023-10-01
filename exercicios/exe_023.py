# Desafio 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# numero = (input('Digite um número de 0 a 9999: '))

# print('Unidade: {}\n'
#      'Dezena: {}\n'
#     'Centena: {}\n'
#      'Milhar: {}'.format(numero[3], numero[2], numero[1], numero[0]))

num = int(input('Digite um número entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(u, d, c, m))
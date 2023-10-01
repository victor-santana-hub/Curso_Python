# Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Insira um número: '))

print('Seu dobro é {}\n'
      'Seu triplo é {} \n'
      'E sua raiz quadrada é {:.2f}.'
      .format(n*2, n*3, n**(1/2)))

# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente,

from math import sin, cos, tan

angulo = float(input('Digite um ângulo qualquer: '))

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print('Para o ângulo de {}º, \n'
      'O seno é {:.2f} \n'
      'O cosseno é {:.2f} \n'
      'A tangente é {:.2f}'
      .format(angulo, seno, cosseno, tangente))

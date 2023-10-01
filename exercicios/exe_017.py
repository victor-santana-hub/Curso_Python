# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('Um triângulo cujo Cateto Oposto é {} e o Cateto Adjacente é {}, \n'
      'tem sua Hipotenusa igual a: {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))

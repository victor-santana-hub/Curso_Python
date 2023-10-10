# Desafio 55 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso
# lidos.

pesos = []

for c in range(1, 6):
    pesos.append(float(input('Digite o {}º peso: '.format(c))))

pesos.sort()
print('O menor peso da lista é {}Kg e o maior peso é {}Kg'.format(pesos[0], pesos[4]))

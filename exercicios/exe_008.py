# Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
# e milímetros.

n = int(input('Digite o valor em metros: '))

print('{} metro(s) é igual a {} centímetros e {} milímetros.'.format(n, n*100, n*1000))

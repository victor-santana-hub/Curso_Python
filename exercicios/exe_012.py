# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Insira o preço do produto: R$'))

print('O valor com desconto de 5% é de R${:.2f}'.format((preco*0.95)))

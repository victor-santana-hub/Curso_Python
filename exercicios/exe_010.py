# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar.  Considerando US$1.00 = R$4,97.

reais = float(input('Valor disponível em reais: R$ '))
dolar = 4.97

print('Você pode comprar US${:.2f}.'.format(reais/dolar))

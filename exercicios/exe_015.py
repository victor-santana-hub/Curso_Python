# Desafio 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Dias de aluguel: '))
km = float(input('Kilômetros rodados com o carro: '))

preco = (dias * 60) + (km * 0.15)

print('O valor total do aluguel do carro é de R${:.2f} \n'
      '{} dias de aluguel = R${:.2f} \n'
      '{} kilômetros rodados = R${:.2f}'
      .format(preco, dias, (dias * 60), km, (km * 0.15)))

# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcula a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Insira a altura da parede, em metros: '))
largura = float(input('Insira a largura da parede, em metros: '))
area = (altura * largura)
litros = (area / 2)

print('Você precisará de {:.2f} litros de tinta para pintar a parede.'.format(litros))

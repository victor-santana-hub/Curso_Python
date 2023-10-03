# Desafio 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('ATENÇÃO! RADAR! \n')
velocidade = int(input('Insira a velocidade do seu carro: '))

multa = float((velocidade - 80) * 7.00)

if velocidade <= 80:
    print('Você está dentro do limite de velocidade. Boa viagem!')
else:
    print('Você ultrapassou o limite de velocidade!! \n'
          'Você receberá uma multa no valor de R${:.2f}!'.format(multa))

# Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

print('\033[35mCALCULADORA DE IMC\033[m')
peso = float(input('Insira seu peso em Kg: '))
altura = float(input('Insira sua altura em Mts: '))
imc = peso / pow(altura, 2)
status = 'Abaixo do Peso'

if 18.5 <= imc <= 25:
    status = 'Peso Ideal'
elif 25 < imc <= 30:
    status = 'Sobrepeso'
elif 30 < imc <= 40:
    status = 'Obesidade'
elif imc > 40:
    status = 'Obesidade Mórbida'

print('Seu IMC é de {:.1f} e seu status é: \033[4m{}\033[m!'.format(imc, status))

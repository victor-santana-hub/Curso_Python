# Desafio 031 - Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0.50/Km para viagens até 200Km e R$0.45/Km para viagens mais longas.

distancia = float(input('Olá! Insira a distância da sua viagem em Km: '))

if distancia <= 200.0:
    valor = float(distancia * 0.50)
    print('O valor da sua passagem é R${:.2f}.'.format(valor))
else:
    valor = float(distancia * 0.45)
    print('O valor da sua passagem é R${:.2f}'.format(valor))

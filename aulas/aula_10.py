# Estruturas Condicionais: Condições Simples e Compostas

# if condicao():
#   True
# else:
#   False
#
# tempo = int(input('Quantos anos tem seu carro? '))
#
# if tempo <= 3:
#     print('Seu carro é novo!')
# else:
#     print('Seu carro está velho')
#
# print('Carro novo' if tempo <= 3 else 'Carro velho')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('Sua média é {:.1f}.'.format(m))

if m >= 6:
    print('Parabéns, sua média está boa.')
else:
    print('Sua nota está abaixo da média, estude mais!')

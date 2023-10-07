# Desafio 042 - Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
# formado: -Equilátero  -Isósceles  -Escaleno

reta_1 = float(input('Digite o comprimento da primeira reta: '))
reta_2 = float(input('Digite o comprimento da segunda reta: '))
reta_3 = float(input('Digite o comprimento da terceira reta: '))

condicao_1 = 0
condicao_2 = 0
condicao_3 = 0
tipo = 'Isósceles'

if (reta_2 - reta_3) < reta_1 < (reta_2 + reta_3):
    condicao_1 = 1

if (reta_1 - reta_3) < reta_2 < (reta_1 + reta_3):
    condicao_2 = 1

if (reta_1 - reta_2) < reta_3 < (reta_1 + reta_2):
    condicao_3 = 1

triangulo = condicao_1 * condicao_2 * condicao_3

if triangulo == 1:
    if reta_1 == reta_2 == reta_3:
        tipo = 'Equilátero'
    elif reta_1 != reta_2 != reta_3:
        tipo = 'Escaleno'
    print('As retas informadas \033[32mFORMAM\033[m um Triângulo \033[33m{}\033[m!'.format(tipo))

else:
    print('As retas informadas \033[31mNÃO\033[m formam um triângulo!')

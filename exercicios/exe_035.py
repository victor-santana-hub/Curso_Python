# Desafio 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

reta_1 = float(input('Digite o comprimento da primeira reta: '))
reta_2 = float(input('Digite o comprimento da segunda reta: '))
reta_3 = float(input('Digite o comprimento da terceira reta: '))

condicao_1 = 0
condicao_2 = 0
condicao_3 = 0

if (reta_2 - reta_3) < reta_1 and reta_1 < (reta_2 + reta_3):
    condicao_1 = 1

if (reta_1 - reta_3) < reta_2 and reta_2 < (reta_1 + reta_3):
    condicao_2 = 1

if (reta_1 - reta_2) < reta_3 and reta_3 < (reta_1 + reta_2):
    condicao_3 = 1

if (condicao_1 + condicao_2 + condicao_3) == 3:
    print('As retas informadas FORMAM um triângulo!')
else:
    print('As retas informadas NÃO formam um triângulo!')

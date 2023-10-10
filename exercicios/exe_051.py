# Desafio 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

print('\033[1;33mPROGRESSÃO ARITMÉTICA\033[m')
termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

for c in range(1, 11):
    print('{}º Termo: {}'.format(c, termo))
    termo += razao

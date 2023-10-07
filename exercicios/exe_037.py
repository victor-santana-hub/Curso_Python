# Desafio 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 - binário, 2 - octal, 3 - hexadecimal.

print('\033[1;31mCONVERSOR DE BASES NUMÉRICAS\033[m \n')
num = int(input('Digite um número inteiro: '))
base = int(input('Seleciona a base de conversão:\n'
                 '1. Binário\n'
                 '2. Octal\n'
                 '3. Hexadecimal\n'))

if base == 1:
    print('O número {} convertido para Binário é: {}'.format(num, bin(num)))
elif base == 2:
    print('O número {} convertido para Octal é: {}'.format(num, oct(num)))
elif base == 3:
    print('O número {} convertido para Hexadecimal é: {}'.format(num, hex(num)))

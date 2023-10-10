# Desafio 52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('TESTE DE NÚMERO PRIMO')

n = int(input('Insira o número que deseja testar: '))

if n < 2 or n % 2 == 0 and n != 2:
    print('O número {} \033[31mNÃO\033[m é primo!'.format(n))
    exit()
elif n % 2 != 0:
    for c in range(3, 8, 2):
        if n != c and n % c == 0:
            print('O número {} \033[31mNÃO\033[m é primo!'.format(n))
            exit()
        elif c == 7:
            print('O número {} \033[32mÉ\033[m primo!'.format(n))
else:
    print('O número {} \033[32mÉ\033[m primo!'.format(n))

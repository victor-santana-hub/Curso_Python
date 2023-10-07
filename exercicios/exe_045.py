# Desafio 45 - Crie um programa que faça o computador jogar Jokenpô com você.

import random

print('\033[4;36mPEDRA, PAPEL OU TESOURA\033[m\n')
opcoes = ['Pedra', 'Papel', 'Tesoura']
pc = random.randint(0, 2)

jogador = int(input('0 = Pedra \n'
                    '1 = Papel \n'
                    '2 = Tesoura \n'
                    'Faça sua escolha: '))

print('\nVocê escolheu: {}'.format(opcoes[jogador]))
print('O PC escolheu: {}'.format(opcoes[pc]))

if pc == jogador:
    print('Você \033[1;33mEMPATOU\033[m!')
elif pc == 0 and jogador == 1 or pc == 1 and jogador == 2 or pc == 2 and jogador == 0:
    print('Você \033[1;32mGANHOU\033[m! ')
else:
    print('Você \033[1;31mPERDEU\033[m!')

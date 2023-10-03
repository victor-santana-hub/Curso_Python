# Desafio 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador.

import random

print('Tente adivinhar em qual número estou pensando!!')
n_pc = random.randint(0, 5)
n_usuario = int(input('Digite um número entre 0 e 5: '))

if n_usuario == n_pc:
    print('Parabéns!! Você acertou! \nO número que eu pensei foi {}.'.format(n_pc))
else:
    print('Ah, você errou! \nO número que eu pensei foi {}.'.format(n_pc))

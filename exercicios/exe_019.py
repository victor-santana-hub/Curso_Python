# Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome dos alunos e escrevendo o nome escolhido.

import random

aluno_1 = input('Digite o nome do Primeiro Aluno: ')
aluno_2 = input('Digite o nome do Segundo Aluno: ')
aluno_3 = input('Digite o nome do Teceiro Aluno: ')
aluno_4 = input('Digite o nome do Quarto Aluno: ')

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

print('O aluno escolhido é: {}'.format(random.choice(alunos)))


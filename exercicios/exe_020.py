# Desafio 020 - O professor que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o
# nome dos quatro alunos e mostre a ordem.

import random

aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno ')

alunos = [aluno1, aluno2, aluno3, aluno4]
ordem = random.sample(alunos, 4)

print('A ordem dos alunos que irão apresetar é: {}'.format(ordem))

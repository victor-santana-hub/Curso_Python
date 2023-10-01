# Desafio 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: '))
nomes = cidade.split()

print('O nome da cidade começa com Santo? \n', 'SANTO' in nomes[0].upper())

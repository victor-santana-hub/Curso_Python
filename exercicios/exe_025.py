# Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite seu nome completo: ')

print('Existe "Silva" no seu nome? \n'
      'Resposta: {}'.format('SILVA' in nome.upper()))

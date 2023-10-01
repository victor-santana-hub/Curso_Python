# Desafio 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.

nome = input('Digite seu nome completo: ')
nomes = nome.split()
n = (len(nomes)) - 1

print('Seu primeiro nome é: {} \n'
      'Seu último nome é: {}'.format(nomes[0], nomes[n]))

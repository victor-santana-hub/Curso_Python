# Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. Todas as letras maiúsculas ; 2. Todas Minúsculas ; 3. Quantas letras no total, sem considerar espaços
# 4. Quantas letras tem o primeiro nome

nome = input('Insira seu nome completo: ')
espacos = nome.count(' ')
nomes = nome.split()

print('1. ', nome.upper())
print('2. ', nome.lower())
print('3. ', (len(nome)) - espacos)
print('4. ', len(nomes[0]))

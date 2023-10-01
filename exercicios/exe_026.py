# Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre: 1. Quantas vezes aparece a letra "A"
# 2. Em que posição ela aparece a primeira vez  3. Em que posição ela aparece a última vez.

frase = input('Digite uma frase qualquer: ')

a = frase.upper().count('A')

print('1. A letra "A" aparece {} vezes na sua frase!'.format(a))
print('2. A letra "A" aparece primeiro na posição {}'.format(frase.upper().find('A')))
print('3. A letra "A" aparece por último na posição {}'.format(frase.upper().rfind('A')))

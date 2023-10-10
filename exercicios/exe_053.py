# Desafio 53 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ')
frase = frase.replace(' ', '')
frase = frase.lower()
letras = len(frase)

cont = 0

for c in range(letras - 1, -1, -1):
    if frase[c] == frase[cont]:
        cont += 1
        if cont == letras:
            print('A frase digitada é um palíndromo!!')
    else:
        print('A frase digitada NÃO é um palíndromo...')
        exit()

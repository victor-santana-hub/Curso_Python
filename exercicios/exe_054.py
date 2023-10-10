# Desafio 54 - Crie um programa que leio o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores de idade.

menores = 0
maiores = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if 2023 - ano < 21:
        menores += 1
    else:
        maiores += 1

print('Número de pessoas maiores de idade: {}\n'
      'Número de pessoas menores de idade: {}'.format(maiores, menores))

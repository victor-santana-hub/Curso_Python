# Desafio 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre a sua categoria, de acordo com a idade: -Até 9 anos: MIRIM  -Até 14 anos: INFANTIL  -Até 19 anos: JUNIOR
# -Até 20 anos: SÊNIOR   -Acima: MASTER

print('\033[1;33mSistema de Classificação de Atletas da Confederação Nacional de Natação\033[m')

ano = int(input('Insira o seu ano de nascimento: '))
idade = 2023 - ano

if idade <= 9:
    classe = 'MIRIM'
elif 9 < idade <= 14:
    classe = 'INFANTIL'
elif 14 < idade <= 19:
    classe = 'JUNIOR'
elif idade == 20:
    classe = 'SÊNIOR'
else:
    classe = 'MASTER'

print('Você tem {} anos! \n'
      'A sua classificação é \033[4m{}\033[m!'.format(idade, classe))

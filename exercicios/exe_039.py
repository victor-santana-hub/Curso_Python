# Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar ; - Se é a hora de se alistar ; - Se já passou do tempo do
# alistamento.  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('\033[1;31mCALCULADORA DE ALISTAMENTO AO SERVIÇO MILITAR\033[m \n')
ano = int(input('Insira o ano em que você nasceu: '))
idade = 2023 - ano

if idade < 18:
    print('Você ainda precisa se alistar! Falta(m) {} ano(s) para \n'
          'você atingir a idade de alistamento!'.format(18 - idade))
elif idade > 18:
    print('Atenção! Já passou da hora de se alistar! Faz {} ano(s) \n'
          'que você deveria ter se alistado!'.format(idade - 18))
else:
    print('Você está completando 18 anos e está na hora de se alistar para o serviço militar!')

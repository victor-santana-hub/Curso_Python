# Desafio 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250.00:
    aumento = salario * 0.1
    print('Seu salário com aumento agora é R${:.2f}'.format(salario + aumento))
else:
    aumento = salario * 0.15
    print('Seu salário com aumento agora é R${:.2f}'.format(salario + aumento))

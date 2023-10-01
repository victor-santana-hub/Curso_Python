# Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário atual: R$'))

print('Após seu aumento de 15%, seu novo salário é R${:.2f}'.format((salario*1.15)))

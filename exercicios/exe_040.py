# Desafio 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média baixo de 5.0: REPROVADO  - Média entre 5.0 e 6.9: RECUPERAÇÃO - Média 7.0 ou superior: APROVADO

print('CALCULE SUA MÉDIA NA MATÉRIA! \n')

nota_1 = float(input('Insira a primeira nota: '))
nota_2 = float(input('Insira a segunda nota: '))
media = (nota_1 + nota_2) / 2

print('Sua média é {:.1f}'.format(media))

if media < 5.0:
    print('Você está \033[1;31mREPROVADO\033[m!')
elif 5.0 <= media <= 6.9:
    print('Você está de \033[1;33mRECUPERAÇÃO\033[m!')
else:
    print('Parabéns! Você está \033[1;32mAPROVADO\033[m!')

# Condições Aninhadas
#
# if (condicao):
# elif (condicao):
# .
# .
# else:
#
# Pode usar quantos elif forem necessários

nome = input('Qual é seu nome? ')

if nome == 'Victor':
    print('Que nome bonito!')
elif nome == 'Alessandra' or nome == 'Arthur':
    print('Seu nome é bem popular!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, \033[1;31m{}\033[m!'.format(nome))


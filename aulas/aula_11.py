# Cores no Terminal
#
# ANSI - \ + código de cor
# Ex: \033[s;t;b m
# s = style   t = text   b = background
#
# Padrão - \033[m
#
# Módulo colorize

print('\033[0;30;41mHello, World!\033[m')
print('\033[4;33;44mHello, World!\033[m')
print('\033[1;35;43mHello, World!\033[m')
print('\033[30;42mHello, World!\033[m')
print('\033[37mHello, World!\033[m')
print('\033[7;97mHello, World!\033[m')

nome = 'Victor Santana'
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;97m',
         'negrito': '\033[1m'}

print('Olá {}{}{}! Seja bem-vindo ao programa!'.format(cores['pretoebranco'], nome, cores['limpa']))

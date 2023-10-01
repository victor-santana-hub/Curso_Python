# Tipos de variáveis primitivas

# int(input('Números inteiros'))
# float(input('Números Reais, com ponto!'))
# bool(input('Variável booleana, True ou False'))
# str(input('Texto'))

n = (input('Digite algo: '))
print('O valor digitado é um número? ', n.isnumeric())
print('O valor digitado é letra? ', n.isalpha())
print('O valor digitado é número ou letra? ', n.isalnum())
print('O valor digitado está em letras maíusculas? ', n.isupper())
print('O valor digitado está em letras minúsculas? ', n.islower())

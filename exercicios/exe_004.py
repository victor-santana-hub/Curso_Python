n = (input('Digite algo: '))

print('Você digitou "{}", que é uma variável do tipo {}'.format(n, type(n)))

print('O valor digitado é um número? ', n.isnumeric())
print('O valor digitado é letra? ', n.isalpha())
print('O valor digitado é alfanumérico? ', n.isalnum())
print('O valor digitado está em letras maíusculas? ', n.isupper())
print('O valor digitado está em letras minúsculas? ', n.islower())
print('O valor digitado está capitalizado? ', n.istitle())
print('O valor digitado é um espaço? ', n.isspace())
print('O valor digitado é um decimal? ', n.isdecimal())
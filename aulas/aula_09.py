# Manipular Cadeias de Texto
# Cadeia de Caracteres (string) = 'Exemplo' ou "Exemplo"
# Cada caractere ocupa um espaço na memória, e cada um recebe um índice (0,1,2,3...)
#
# Fatiamento:
# É possível selecionar a letra dentro do índice da memória
# Ex: frase = 'Curso em Video Python'
#     print(frase[9]) = V
#     print(frase[9:13]) = Vide (inclui 9 até 12, não inclui 13)
#

frase = 'Curso em Video Python'

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3], '\n')

print(len(frase))
print(frase.count('e'))
print(frase.count('o',5,20))
print(frase.count('so'))
print('Vi' in frase, '\n')

print(frase.replace('Python','Programação'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title(), '\n')

frase1 = '   Curso em Video    '
print(frase1.strip())
print(frase1.rstrip())
print(frase1.lstrip())

frase2 = frase.split()
print(frase2)
print('-'.join(frase2))

# Laços de Repetição - Parte 1
#
#   for c in range(0, 10):
#       o que quer repetir

for c in range(0, 6):  # De 0 até 5
    print('Oi {}'.format(c))
print('FIM\n')

for c in range(1, 6):  # De 1 até 5
    print('Oi {}'.format(c))
print('FIM\n')

for c in range(6, 0, -1):   # Diminui um por vez
    print('Oi {}'.format(c))
print('FIM\n')

for c in range(0, 6, 2):   # De 2 em 2
    print('Oi {}'.format(c))
print('\n')

# n = int(input('Digite um número: '))
# for count in range(0, n+1):
#     print(count)
# print('FIM\n')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for count in range(inicio, fim+1, passo):
    print(count)
print('FIM\n')

soma = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    soma += n
print('A soma dos valores é {}'.format(soma))

nomes = ['', '', '', '']
for c in range(0, 4):
    nomes[c] = input('Digite o nome do aluno: ')
for c in range(0, 4):
    print('Aluno {}: {}'.format(c+1, nomes[c]))

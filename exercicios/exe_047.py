# Desafio 47 - Crie um programa que mostre na tela todos os pares que estão no intervalo entre 1 e 50.

inicio = int(input('Digite o primeiro número: '))
fim = int(input('Digite o último número: '))

print('NUMEROS PARES ENTRE {} e {}'.format(inicio, fim))
for c in range(inicio, fim+1):
    if c % 2 == 0:
        print(c)
print('FIM :)')

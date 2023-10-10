# Desafio 49 - Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
# um laço for.

print("\033[1;31mPROGRAMA DE TABUADA\033[m")
n = int(input('Insira o número que deseja ver a tabuada: '))

print('\nTABUADA DO {}'.format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(c, n, c * n))

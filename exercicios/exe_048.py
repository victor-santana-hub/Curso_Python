# Desafio 48 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
        soma += c

print('A soma dos números é: {}'.format(soma))




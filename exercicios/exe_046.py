# Desafio 46 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo
# de 10 até 0, com uma pausa de 1 segundo entre eles.

import time
import emoji

print('CONTAGEM REGRESSIVA')
for c in range(10, -1, -1):
    print(c)
    if c == 0:
        print(emoji.emojize('🚀'*10))
    time.sleep(1)

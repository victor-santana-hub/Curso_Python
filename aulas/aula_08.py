# Módulos

# import biblioteca
#   obs: para chamar uma função, deve-se digitar biblioteca.funcao
# from biblioteca import funcao
#   obs: para chamar a função que foi importada, chama direto a função (ex: funcao(1, 5))

from math import sqrt, ceil, exp
import random

n = int(input('Digite um numero: '))
raiz = sqrt(n)
num = random.randint(0, 25)
num_1 = random.randrange(2)


# print('A raiz de {} é igual {:.2f}!'.format(n, raiz))
print('O número aleatório é {}.'.format(num))
print(num_1)




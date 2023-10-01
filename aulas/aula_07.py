#   Operações Aritméticas
#   +   (Adição)
#   -   (Substração)
#   *   (Multiplicação)
#   /   (Divisão)
#   **  ou  pow(base,potencia)  (Potência)
#   //  (Divisão Inteira)
#   %   (Resto da Divisão)
#   n**(1/2)  (Raiz Quadrada)
#   n**(1/3)  (Raiz Cúbica)

# Ordem: 1. ()
#        2. **
#        3. * ou / ou // ou %
#        4. + ou -

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {:*^20}!' .format(nome))

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
produto = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
potencia = n1 ** n2

print('A soma é: {} \n'
      'O produto é: {} \n'
      'A divisão é: {:.2f} \n'
      'A divisão inteira é: {} \n'
      'E a potência é: {}'
      .format(soma, produto, divisao, divisao_inteira, potencia))
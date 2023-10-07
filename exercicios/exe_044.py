# Desafio 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:  - À vista dinheiro/pix: 10% de desconto   - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal  - 3x ou mais no cartão: 20% de juros

preco_normal = float(input('Qual o preço do produto? R$'))
preco_final = preco_normal * 0.9

print('Selecione a forma de pagamento: \n'
      '1. À vista - Dinheiro ou PIX \n'
      '2. À vista - 1x Cartão \n'
      '3. Em até 2x no Cartão \n'
      '4. 3x ou mais no Cartão')
pagamento = int(input(': '))

if pagamento == 1:
    preco_final = preco_final
elif pagamento == 2:
    preco_final = preco_normal * 0.95
elif pagamento == 3:
    preco_final = preco_normal
elif pagamento == 4:
    preco_final = preco_normal * 1.2
else:
    print('\033[31mForma de Pagamento Inválida, favor tentar novamente!!\033[m')
    exit()

print('O valor total da compra é R${:.2f}'.format(preco_final))

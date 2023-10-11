# Desafio 56 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo; O nome do homem mais velho; Quantas mulheres têm menos de 20 anos.

# Variáveis
pessoas = []
homens = []
homens_idades = []
homem_velho = []
mulheres = []
mulheres_menores = 0
soma = 0
media = 0
nome = 0
idade = 1
sexo = 2

# Aquisição dos dados
for c in range(0, 4):
    print('\nDigite os dados da {}ª pessoa:'.format(c+1))
    pessoas.append([input('Nome: '), int(input('Idade: ')), input('Sexo (M/F): ')])


# Encontrando a media das idades
for c in range(0, 4):
    anos = pessoas[c][idade]
    soma += anos
    media = soma / (c + 1)
print('\n- A média das idades do grupo é de {} anos!'.format(media))


# Separando os homens e mulheres
for c in range(0, 4):
    if 'm' in pessoas[c][2].lower():
        homens.append([pessoas[c][nome], pessoas[c][idade]])
    else:
        mulheres.append([pessoas[c][nome], pessoas[c][idade]])


# Encontrar o homem mais velho
if len(homens) == 0:
    print('- Não foram digitados os dados de nenhum homem!', end='')
elif len(homens) == 1:
    homem_velho = homens[0][nome]
else:
    for c in range(0, len(homens)):
        homens_idades.append([homens[c][idade]])
    homens_idades.sort(reverse=True)
    for c in range(0, len(homens)):
        if homens[c][idade] == homens_idades[0][0]:
            homem_velho.append(homens[c][nome])
    print('- O(s) homem(ns) mais velho(s) é/são:')
    for c in range(0, len(homem_velho)):
        print(' ', homem_velho[c].title(), end='; ')

# Número de mulheres menores de 20 anos
if len(mulheres) == 0:
    print('\n- Não foram digitados os dados de nenhuma mulher!')
else:
    for c in range(0, len(mulheres)):
        if mulheres[c][idade] < 20:
            mulheres_menores += 1
    print('\n- \033[32m{}\033[m mulher(es) têm menos de 20 anos!'.format(mulheres_menores))

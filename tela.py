import random
from constantes import *

print(' ')
print('Bem-vindo ao INSPER - Batalha Naval')
print(' ')
print('Iniciando o jogo!')
print(' ')

lista_paises = []
for pais in PAISES.keys():
    lista_paises.append(pais)

pais_escolhido = random.choice(lista_paises)

print(f'Computador está alocando os navios de guerra do país {pais_escolhido}.')
print('Computador já está em posição de batalha!')
print(' ')


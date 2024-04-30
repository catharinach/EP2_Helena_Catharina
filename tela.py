import time
import random
from constantes import *
from operacoes import *

print(' ')
print('Bem-vindo ao INSPER - Batalha Naval')
print(' ')
print('Iniciando o jogo!')
print(' ')

#escolhendo pais aleatorio para o computador
lista_paises = []
for pais in PAISES.keys():
    lista_paises.append(pais)

pais_escolhido = random.choice(lista_paises)

print(f'Computador está alocando os navios de guerra do país {pais_escolhido}.')
print('Computador já está em posição de batalha!')

novo_dicionario = {}
num = 1
for pais in PAISES:
    novo_dicionario[num] = pais
    num += 1

for numero, pais in novo_dicionario.items():
    if pais in PAISES:
        print('')
        print(f'{numero} - {pais}:')
        for navio, qtd in PAISES[pais].items():
            n_navio = navio.capitalize()
            print(f'    {n_navio}: {qtd}')

print('')
x = int(input('Qual o número da nação da sua frota? ')) 
while x not in novo_dicionario:
    print('Frota não encontrada... Escolha uma das nações disponíveis!') 
    x = int(input('Qual o número da nação da sua frota? '))  

frota_escolhida = { }
for numero, pais in novo_dicionario.items(): 
    if x == numero: 
        pais_escolhido = pais 
        for navio, qtd in PAISES[pais_escolhido].items(): 
            frota_escolhida[navio] = qtd
        break 


def imprimir_navios_restantes(frota_escolhida): 
    print('Navios restantes:')
    for navio, qtd in frota_escolhida.items():
        print(f'{qtd} {navio if qtd == 1 else navio + "s"}')

print('')
print(f'Você irá disputar com a frota do país {pais_escolhido}!' ) 
print('Os navios disponíveis para combate são: ', end='') 

for i, (navio, qtd) in enumerate(frota_escolhida.items()):
    nome_navio = navio.capitalize() 
    if qtd < 2: 
        print(f'{qtd} {nome_navio}', end=", " if i <len(frota_escolhida) - 1 else '!')
    else: 
        print (f'{qtd} {nome_navio}s', end=", " if i <len(frota_escolhida) - 1 else '!')

print('\nSe prepare para alocá-los!') 
print()

mapa_usuario, matriz_adversario = criar_mapa()
print_maps(matriz_adversario, mapa_usuario)


lista = []
for pais, info in PAISES.items():
    if pais == pais_escolhido:
        for navio, qtd in info.items():
            for i in range(qtd):
                lista.append(CONFIGURACAO[navio])

mapa_u, mapa_adv = criar_mapa()
mapa_computador = aloca_navios(mapa_adv, lista)
mapa_computador = aloca_navios(matriz_adversario, lista)

print()

while len(frota_escolhida) > 0: 
    navio, qtd = list(frota_escolhida.items())[0]  # Pegar o primeiro navio da frota
    tamanho_navio = CONFIGURACAO[navio]
    
    print(f'Navio a ser alocado: 1 {navio} (Tamanho: {tamanho_navio} blocos)')
    print() 
    fila = int(input(f"Digite o número da fila para o {navio}: "))
    coluna = ALFABETO.index(input(f"Digite a letra da coluna para o {navio} (A-J): ").upper()) + 1
    orientacao = input("Digite 'h' para horizontal ou 'v' para vertical: ") 

    x = posicao_suporta(mapa_usuario, tamanho_navio, fila, coluna, orientacao) 

    while not x:
        print('Não é possível colocar um navio nessa posição... Tente novamente.')
        fila = int(input(f"Digite o número da fila para o {navio}: "))
        coluna = ALFABETO.index(input(f"Digite a letra da coluna para o {navio} (A-J): ").upper()) + 1
        orientacao = input("Digite 'h' para horizontal ou 'v' para vertical: ") 
        x = posicao_suporta(mapa_usuario, tamanho_navio, fila, coluna, orientacao)
        print('')
    
    y = alocando(mapa_usuario, tamanho_navio, fila, coluna, orientacao)

    mapa_usuario, matriz_adversario = mapa_formatado(y, mapa_computador)

    print ('')
    print_maps(matriz_adversario, mapa_usuario)

    frota_escolhida[navio] -= 1
    if frota_escolhida[navio] == 0: 
        del frota_escolhida[navio]

    print("Muito bem! Você está pronto para o combate!")


countdown = [5, 4, 3, 2, 1]
for i in countdown:
    time.sleep(1)
    print(i)


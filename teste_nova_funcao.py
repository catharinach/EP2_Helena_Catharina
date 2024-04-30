import time
from constantes import *
from operacoes import *
import random

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

lista = []
for pais, info in PAISES.items():
    if pais == pais_escolhido:
        for navio, qtd in info.items():
            for i in range(qtd):
                lista.append(CONFIGURACAO[navio])


mapa_u, mapa_adv = criar_mapa2()

mapa_computador = aloca_navios2(mapa_adv, lista)

print()

def aloca_navios3(mapa):
    for navio, qtd in list(frota_escolhida.items()):
        for _ in range(qtd):
            print(f'Alocando navio {navio}:')
            fila = int(input("Digite o número da fila (1-10): "))
            coluna = ALFABETO.index(input("Digite a letra da coluna (A-J): ").upper()) + 1
            orientacao = input("Digite 'h' para horizontal ou 'v' para vertical: ")

            x = posicao_suporta(mapa, CONFIGURACAO[navio], fila, coluna, orientacao)
            while x == False:
                print('Não é possível colocar um navio nessa posição. Tente novamente.')
                fila = int(input("Digite o número da fila (1-10): "))
                coluna = ALFABETO.index(input("Digite a letra da coluna (A-J): ").upper()) + 1
                orientacao = input("Digite 'h' para horizontal ou 'v' para vertical: ")
                x = posicao_suporta(mapa, CONFIGURACAO[navio], fila, coluna, orientacao)

            mapa_u = alocando2(mapa, CONFIGURACAO[navio], fila, coluna, orientacao)

            print("Mapa do adversário:".center(20), "Seu mapa:".center(40))
            print()
            for linha_adv, linha_jog in zip(mapa_adv, mapa_u):
                print(" ".join(linha_adv).ljust(30), "  ", " ".join(linha_jog))

    return mapa_u

while frota_escolhida: 
    for navio, qtd in list(frota_escolhida.items()): 
        tamanho_navio = CONFIGURACAO[navio] 
        if qtd > 0: 
           print(f'Navio a ser alocado: 1 {navio} (Tamanho: {tamanho_navio} blocos)')
           print() 
           z = aloca_navios3(mapa_u)
        print ('')

        print("Mapa do adversário:".center(20), "Seu mapa:".center(40))
        print()
        for linha_adv, linha_jog in zip(mapa_adv, y):
            print(" ".join(linha_adv).ljust(30), "  ", " ".join(linha_jog))

        frota_escolhida[navio] -= 1
        if frota_escolhida[navio] == 0: 
            del frota_escolhida[navio]
        break 

countdown = [5, 4, 3, 2, 1]
for i in countdown:
    time.sleep(1)
    print(i)

from constantes import *
import random

linhas = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ' ', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

def cria_mapa(n):
    lista = [' ']*n
    lista2 = [lista]*n
    return lista2

def posicao_suporta(mapa, blocos, linha, coluna, orientacao): 
    tamanho = len(mapa)
    
    if linha < 1 or coluna < 1 or linha >= tamanho or coluna >= tamanho:
        return False
    
    if orientacao == 'v': 
        if linha + blocos > tamanho:
            return False 
        for i in range(linha, linha + blocos): 
            if mapa[i][coluna] != ' ': 
                return False 
    elif orientacao == 'h': 
        if coluna + blocos > tamanho: 
            return False 
        for j in range(coluna,  coluna + blocos): 
            if mapa[linha][j] != ' ': 
                return False 
            

def alocando(mapa, b, l, c, o):
    if o == 'v':
        for i in range(l, l+b):
            if i >= 1:  
                mapa[i][c] = u'\u001b[35mN\u001b[0m'

    elif o == 'h':
        if l >= 1: 
            for j in range(c, c+b):
                mapa[l][j] = u'\u001b[35mN\u001b[0m'

    return mapa 

def alocando2(mapa, b, l, c, o):
    if o == 'v':
        for i in range(l, l+b):
            mapa[i][c] = u'\u001b[35mN\u001b[0m'

    elif o == 'h':
        for j in range(c, c+b):
            mapa[l][j] = u'\u001b[35mN\u001b[0m'

    return mapa 


def aloca_navios(mapa, lista):
    n = len(mapa)
    for bloco in lista:
        x = False
        while not x:
            linha = random.randint(1, n - 2)  # Evita a linha 0 e a última linha
            coluna = random.randint(1, n - 1)
            orientacao = random.choice(['h', 'v'])
            x = posicao_suporta(mapa, bloco, linha, coluna, orientacao)
        mapa = alocando(mapa, bloco, linha, coluna, orientacao)
    return mapa

def foi_derrotado(matriz):
    x = True
    for lista in matriz:
        if 'N' in lista:
            x = False
    return x    



# Imprimir navios a serem alocados 

def imprimir_navios_restantes(frota_escolhida): 
    print('Navios restantes:')
    for navio, qtd in frota_escolhida.items():
        print(f'{qtd} {navio if qtd == 1 else navio + "s"}')


    imprimir_navios_restantes(frota_escolhida)

print("Muito bem! Você está pronto para o combate!")
# Correcao na impressao dos mapas 

def criar_mapa():
    matriz_adversario = []
    matriz_jogador = []

    for i in range(12):
        linha_adversario = []
        linha_jogador = []

        if i == 0 or i == 11:
            linha_adversario = [' '] + [letra for letra in ALFABETO[:10]] + [' ']
            linha_jogador = [' '] + [letra for letra in ALFABETO[:10]] + [' ']
        else:
            linha_adversario = [' '] * 12
            linha_jogador = [' '] * 12

        if 1 <= i <= 10:
            nmr = str(i)
            linha_adversario[0] = nmr
            linha_jogador[0] = nmr
            linha_adversario[-1] = nmr
            linha_jogador[-1] = nmr

        matriz_adversario.append(linha_adversario)
        matriz_jogador.append(linha_jogador)

    return matriz_jogador, matriz_adversario

# Correcao na impressao dos mapas 

def criar_mapa():
    matriz_adversario = []
    matriz_jogador = []

    for i in range(12):
        linha_adversario = []
        linha_jogador = []

        if i == 0 or i == 11:
            linha_adversario = [' '] + [letra for letra in ALFABETO[:10]] + [' ']
            linha_jogador = [' '] + [letra for letra in ALFABETO[:10]] + [' ']
        else:
            linha_adversario = [' '] * 12
            linha_jogador = [' '] * 12

        if 1 <= i <= 10:
            nmr = str(i)
            linha_adversario[0] = nmr
            linha_jogador[0] = nmr
            linha_adversario[-1] = nmr
            linha_jogador[-1] = nmr

        matriz_adversario.append(linha_adversario)
        matriz_jogador.append(linha_jogador)

    return matriz_jogador, matriz_adversario


def mapa_formatado(mapa_jogador, mapa_adversario):
    matriz_jogador = []
    matriz_adversario = []

    max_rows = max(len(mapa_jogador), len(mapa_adversario))

    for i in range(max_rows):
        linha_jogador = [' '] * 12
        linha_adversario = [' '] * 12

        if 0 < i < 11:
            if i < len(mapa_jogador):
                linha_jogador[:len(mapa_jogador[i])] = mapa_jogador[i]
            if i < len(mapa_adversario):
                linha_adversario[:len(mapa_adversario[i])] = mapa_adversario[i]

        if i == 0 or i == 11:
            linha_jogador = [' '] + [letra for letra in ALFABETO[:10]] + [' ']
            linha_adversario = [' '] + [letra for letra in ALFABETO[:10]] + [' ']

        matriz_jogador.append(linha_jogador)
        matriz_adversario.append(linha_adversario)

    return matriz_jogador, matriz_adversario


def print_maps(matriz_adversario, mapa_usuario):
    print("Mapa do adversário:".center(30), "Seu mapa:".center(40))
    print()

    for linha_adv, linha_jog in zip(matriz_adversario, mapa_usuario):
        linha_adv_str = " ".join(linha_adv).ljust(30)
        linha_jog_str = " ".join(linha_jog).ljust(40)
        print(linha_adv_str, "   ", linha_jog_str)



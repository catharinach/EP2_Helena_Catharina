from constantes import *
import random

linhas = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ' ', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

def cria_mapa(n):
    lista = [' ']*n
    lista2 = [lista]*n
    return lista2

def posicao_suporta(mapa, blocos, linha, coluna, orientacao): 
    tamanho = len(mapa)
    if mapa[linha][coluna] != ' ': 
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
            
    return True 
            
def aloca_navios2(mapa, lista):
    n = 10
    linha = random.randint(0, n-1)
    coluna = random.randint(0, n-1)
    orientacao = random.choice(['h', 'v'])
    for bloco in lista:
        x = posicao_suporta(mapa, bloco, linha, coluna, orientacao)
        while x == False:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            x = posicao_suporta(mapa, bloco, linha, coluna, orientacao)
        mapa_computador = alocando2(mapa, bloco, linha, coluna, orientacao)

    return mapa_computador

# Tentativa de usar as cores nos mapas 
def alocando(mapa, b, l, c, o):
    if o == 'v':
        for i in range(l, l+b):
            if i >= 1:  
                mapa[i][c] = u'\u001b[35m \u001b[0m'

    elif o == 'h':
        if l >= 1: 
            for j in range(c, c+b):
                mapa[l][j] = u'\u001b[35m \u001b[0m'

    return mapa 

def alocando2(mapa, b, l, c, o):
    if o == 'v':
        for i in range(l, l+b):
            mapa[i][c] = 'N'

    elif o == 'h':
        for j in range(c, c+b):
            mapa[l][j] = 'N'

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
        mapa = alocando2(mapa, bloco, linha, coluna, orientacao)
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

def criar_mapa2():
    matriz_adversario = []
    matriz_jogador = []

    for i in range(1, 11):
        linha_adversario = [' '] * 11
        linha_jogador = [' '] * 11
        if i >= 1 and i <= 9:
            nmr = str(i)
            lista = [' ', nmr]
            linha_adversario[0] = str(i)
            linha_jogador[0] = str(i)
            linha_adversario[-1] = ''.join(lista)
            linha_jogador[-1] = ''.join(lista)
        elif i == 10:
            linha_adversario[0] = str(i)
            linha_jogador[0] = str(i)
            linha_adversario[-1] = str(i)
            linha_jogador[-1] = str(i)
        matriz_adversario.append(linha_adversario)
        matriz_jogador.append(linha_jogador)
    
    matriz_adversario.insert(0, [' '] + [letra for letra in ALFABETO[:10]] + [' '])
    matriz_jogador.insert(0, [' '] + [letra for letra in ALFABETO[:10]] + [' '])
    matriz_adversario.insert(11, [' '] + [letra for letra in ALFABETO[:10]] + [' '])
    matriz_jogador.insert(11, [' '] + [letra for letra in ALFABETO[:10]] + [' '])
    
    print("Mapa do adversário:".center(20), "Seu mapa:".center(30))
    print( )
    for linha1, linha2 in zip(matriz_jogador, matriz_adversario):
        print("{:<25} {:<25}".format(" ".join(linha1), " ".join(linha2))) 

    matrizes = [matriz_jogador, matriz_adversario]
    return matrizes  

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

def mapa_formatado(mapa_jogador, mapa_adversario):
    matriz_jogador = []
    matriz_adversario = []

    for i in range(12):
        linha_jogador = []
        linha_adversario = []

        if i == 0 or i == 11:
            linha_jogador = [' '] + [letra for letra in ALFABETO[:10]] + [' ']
            linha_adversario = [' '] + [letra for letra in ALFABETO[:10]] + [' ']
        else:
            linha_jogador = mapa_jogador[i]
            linha_adversario = mapa_adversario[i]

        matriz_jogador.append(linha_jogador)
        matriz_adversario.append(linha_adversario)

    return matriz_jogador, matriz_adversario 

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
            if i >= 1 and i <= 9:
                nmr = str(i)
                lista = [' ', nmr]
                linha_adversario[0] = str(i)
                linha_jogador[0] = str(i)
                linha_adversario[-1] = ''.join(lista)
                linha_jogador[-1] = ''.join(lista)
            elif i == 10:
                linha_adversario[0] = str(i)
                linha_jogador[0] = str(i)
                linha_adversario[-1] = str(i)
                linha_jogador[-1] = str(i)
        matriz_adversario.append(linha_adversario)
        matriz_jogador.append(linha_jogador)
    


    print("Mapa do adversário:".center(20), "Seu mapa:".center(40))
    print( )
    for linha_adv, linha_jog in zip(matriz_adversario, matriz_jogador):
        print(" ".join(linha_adv).ljust(30), "", " ".join(linha_jog)) 

    matrizes = [matriz_jogador, matriz_adversario]
    return matrizes  

def atirar(mapa):
    print(' ')
    linha = int(input("Em qual linha você deseja atirar? (1-10): ")) + 1 
    coluna = ALFABETO.index(input("Em qual coluna você deseja atirar? (A-J): ").upper()) + 1 
    
    if mapa[linha][coluna] == 'N':
        print("Você acertou um navio!")
        mapa[linha][coluna] = 'X'
    else:
        print("Tiro na água!")
        mapa[linha][coluna] = 'A'

def atirar_computador(mapa):
    linha = random.randint(1, 10)
    coluna = random.randint(1, 10)
    
    if mapa[linha][coluna] == 'N':
        print("O computador acertou um de seus navios!")
        mapa[linha][coluna] = 'X'
    else:
        print("O computador atirou na água!")
        mapa[linha][coluna] = 'A'


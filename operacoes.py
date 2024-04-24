from constantes import * 
import random
linhas = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

def cria_mapa(n):
    lista = [' ']*n
    lista2 = [lista]*n
    return lista2

def posicao_suporta (mapa, blocos, linha, coluna, orientacao): 
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

def alocando(mapa, b, l, c, o):
    y = len(mapa)
    if o == 'v':
        for i in range(l, l+b):
            mapa[i][c] = 'N'

    elif o == 'h':
        for i in range(c, c+b):
            mapa[l][i] = 'N'

    return mapa

def aloca_navios(mapa, lista):
    n = len(mapa)
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
        y = alocando(mapa, bloco, linha, coluna, orientacao)
        mapa = y

    return mapa

def foi_derrotado(matriz):
    x = True
    for lista in matriz:
        if 'N' in lista:
            x = False
    return x    

def criar_mapa (): 
    matriz = [ ] 

    for i in range(11):
        if i == 0:
            linha = [letra for letra in ALFABETO[:10]]
        else:
            linha = [''] * 10
        matriz.append(linha)

    
    for i, linha in enumerate(matriz):
        linha_formatada = f"{linhas[i]:>2s} "
        print(linha_formatada, end="")
        print(" ".join(linha))

    
criar_mapa() 
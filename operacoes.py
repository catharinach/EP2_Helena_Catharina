from constantes import * 
import random
from tela import * 
linhas = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ' ', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

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
        mapa_computador = y

    return mapa_computador

def foi_derrotado(matriz):
    x = True
    for lista in matriz:
        if 'N' in lista:
            x = False
    return x    

#
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
        print(" ".join(linha_adv).ljust(30), "   ", " ".join(linha_jog)) 

    matrizes = [matriz_jogador, matriz_adversario]
    return matrizes  

# Imprimir navios a serem alocados 

def imprimir_navios_restantes(): 
    print('Navios restantes:')
    for navio, qtd in frota_escolhida.items():
        print(f'{qtd} {navio if qtd == 1 else navio + "s"}')


imprimir_navios_restantes()


while frota_escolhida:
    for navio, qtd in list(frota_escolhida.items()): 
        if qtd > 0:
            print(f'Navio a ser alocado: 1 {navio if qtd == 1 else navio + "s"}')
            print()
            frota_escolhida[navio] -= 1
            if frota_escolhida[navio] == 0:
                del frota_escolhida[navio]
            break  
    imprimir_navios_restantes()

print("Muito bem! Você está pronto para o combate!")
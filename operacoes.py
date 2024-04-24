from constantes import * 

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


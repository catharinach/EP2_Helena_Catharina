from constantes import *
from operacoes import *
import random

print(' ')
print('Bem-vindo ao INSPER - Batalha Naval')
print(' ')
print('Iniciando o jogo!')
print(' ')

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
    print("Mapa do adversário:".center(20), "Seu mapa:".center(40))
    print( )
    for linha1, linha2 in zip(matriz_jogador, matriz_adversario):
        print("{:<25} {:<25}".format(" ".join(linha1), " ".join(linha2))) 

    matrizes = [matriz_jogador, matriz_adversario]
    return matrizes  

mapa_u, mapa_adv = criar_mapa2()

mapa_computador = aloca_navios2(mapa_adv, lista)

print()

while frota_escolhida: 
    for navio, qtd in list(frota_escolhida.items()): 
        tamanho_navio = CONFIGURACAO[navio] 
        if qtd > 0: 
           print(f'Navio a ser alocado: 1 {navio} (Tamanho: {tamanho_navio} blocos)')
           print() 
           fila = int(input(f"Digite o número da fila para o {navio}: "))
           coluna = ALFABETO.index(input(f"Digite a letra da coluna para o {navio} (A-J): ").upper()) + 1
           orientacao = input("Digite 'h' para horizontal ou 'v' para vertical: ") 

           x = posicao_suporta(mapa_u, tamanho_navio, fila, coluna, orientacao) 
           
           while x == False:
               print('Não é possível colocar um navio nessa posição... Tente novamente.')
               fila = int(input(f"Digite o número da fila para o {navio}: "))
               coluna = ALFABETO.index(input(f"Digite a letra da coluna para o {navio} (A-J): ").upper()) + 1
               orientacao = input("Digite 'h' para horizontal ou 'v' para vertical: ") 
               x = posicao_suporta(mapa_u, tamanho_navio, fila, coluna, orientacao)
               print('')
        y = alocando(mapa_u, tamanho_navio, fila, coluna, orientacao)
        
        print ('')

        print("Mapa do adversário:".center(20), "Seu mapa:".center(40))
        print()
        for linha_adv, linha_jog in zip(mapa_adv, y):
            print(" ".join(linha_adv).ljust(30), "  ", " ".join(linha_jog))

        frota_escolhida[navio] -= 1
        if frota_escolhida[navio] == 0: 
            del frota_escolhida[navio]
        break 


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

#print("Mapa do adversário:".center(20), "Seu mapa:".center(40))
#print()
#for linha_adv, linha_jog in zip(matriz_adversario, mapa_usuario):
#print(" ".join(linha_adv).ljust(30), "   ", " ".join(linha_jog))

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
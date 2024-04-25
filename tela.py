import random
from constantes import *
from operacoes import * 

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

mapas = criar_mapa()
mapa_usuario = mapas[0]
while frota_escolhida: 
    for navio, qtd in list(frota_escolhida.items()): 
        tamanho_navio = CONFIGURACAO[navio] 
        if qtd > 0: 
           print(f'Navio a ser alocado: 1 {navio} (Tamanho: {tamanho_navio} blocos)')
           print() 
           coluna = input('Em qual coluna deseja alocar? ')
           linha = int(input('Em qual linha deseja alocar? '))
           orientacao = str(input('Escolha a orientação do navio (h/v): ')) 

           x = alocando(mapa_usuario, tamanho_navio, linha, coluna, orientacao)
           frota_escolhida[navio] -= 1
           if frota_escolhida[navio] == 0: 
               del frota_escolhida[navio]
           break 

    

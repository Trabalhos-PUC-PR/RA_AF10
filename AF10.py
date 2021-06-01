'''
1) Elabore uma App em Python para ler do teclado uma matriz 3x3 de valores reais. A App devera chamar uma função que 
receba essa matriz como parâmetro de entrada e retorne o valor da soma de todos os elementos. A App deverá imprimir a
matriz de entrada e o valor da soma. 

2) Elabore uma App em Python para ler do teclado uma matriz 5x5 de valores inteiros. A App devera chamar uma função que
receba essa matriz como parâmetro de entrada e retorne o valor da soma de todos os elementos da diagonal principal. A App
deverá imprimir a matriz de entrada e o valor da soma. 

3) Elabore uma App que leia uma matriz de 3x4 de caracteres, imprima se existe entre os elementos um caractere ʻBʼ e em que
linha e coluna ele foi encontrado. A App devera chamar uma função que receba a matriz lida e retorne a linha e coluna onde o 
caractere foi encontrado. Caso ele não esteja presente a função deverá retornar (-1, -1). 
'''
import numpy as np

escolha = int(input("Escolha a atividade (1-3): "))
if(escolha>3 or escolha<1):
    exit("Atividade não existente")

#---------------------------------------------------------------ATIVIDADE 1
def recebeMatriz(matriz):
    soma = 0 #variavel q recebe a soma da matriz
    for c in range(len(matriz)): #repete [numero de colunas] vezes
        for l in range(len(matriz)): #repete [numero de linhas] vezes
            soma += matriz[l][c] #matriz x=l, y=c | soma recebe esse valor
    return soma

if(escolha==1):
    matriz = [] 
    for c in range(0, 3): #repete 3 vezes
        matriz_2 = [] #essa lista serve pra receber os valores digitados e coloca na lista "matriz" 
        for i in range(0, 3):
            matriz_2.append(float(input("Digite um número: "))) #recebe valor real e manda pra lista
        matriz.append(matriz_2)#depois de rodar ali em cima 4 vezes, coloca a lista matriz_2 dentro da lista matriz
    for i in matriz:
        print(i)
    print(recebeMatriz(matriz))
    exit()


#---------------------------------------------------------------ATIVIDADE 2
def recebeMatrizDiagonal(matriz):
    soma = 0
    for c in range(len(matriz)):
        soma += matriz[c][c] #pega a diagonal (0,0), (1,1) e por ai vai
    return soma

if(escolha==2): #mesma coisa do código de cima
    matriz = []
    for c in range(0, 5):
        matriz_2 = []
        for i in range(0, 5):
            matriz_2.append(float(input("Digite um número: ")))
        matriz.append(matriz_2)
    for i in matriz:
        print(i)
    print(recebeMatrizDiagonal(matriz))
    exit()

#---------------------------------------------------------------ATIVIDADE 3
'''
coluna é o len(matriz[0]), sem isso é a linha
o matriz[0] representa as colunas pois pega o numero de posições na primeira linha
lembrando que as coordenadas são: matriz[x][y]
'''
def recebeMatrizProcura(matriz): #
    tem = 0
    for l in range(len(matriz)): #linha
        for c in range(len(matriz[0])): #coluna
            if(matriz[l][c] == "B"): #se na linha l e na coluna c tem B
                print("Existe um ",matriz[l][c]," na",l+1,"° linha e na",c+1,"° coluna")
                tem = 1
    if(tem != 0):
        return
    else:
        return print(-1, -1) 

if(escolha==3):
    matriz = []
    for c in range(0, 3):
        matriz_2 = []
        for l in range(0, 4):
            matriz_2.append(input("Digite um caractere: "))
        matriz.append(matriz_2)
    for l in matriz:
        print(l)
    recebeMatrizProcura(matriz)
    exit()
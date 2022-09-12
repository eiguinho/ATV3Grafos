'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

from io import StringIO
import numpy as np

def tipoGrafo(matriz):
    qtdVertices = np.shape(matriz)[0]
    tipo = 0 # se for grafo simples, ja recebendo um zero antes das verificacoes dos outros tipos
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        if(matriz[vi][vi] > 0): #pseudografo
            tipo = 3
            return tipo
        for vj in range(0, qtdVertices):  # Para cada vértice vj
            if(matriz[vi][vj] > 1): #multigrafo, pois tem arestas paralelas
                tipo = 2
            if(matriz[vi][vj] != matriz[vj][vi]): #digrafo, pois a matriz eh assimetrica
                tipo = 1
    print('Tipo do grafo:', tipo, '\n')
    return tipo

'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes


def calcDensidade(matriz):
    qtdVertices = np.shape(matriz)[0]
    arestas = 0
    tipo = 0  # se for grafo simples, ja recebendo um zero antes das verificacoes dos outros tipos
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        for vj in range(0, qtdVertices):  # Para cada vértice vj
            if (matriz[vi][vj] != matriz[vj][vi]):  # digrafo, pois a matriz eh assimetrica
                tipo = 1
            arestas += matriz[vi][vj]
    if(tipo == 0):
        result = (2*arestas)/(qtdVertices*(qtdVertices-1))
    else:
        result = (arestas) / (qtdVertices * (qtdVertices - 1))
    print('A densidade dessa matriz é: ', result, '\n')
    return result

# insere aresta nos pontos vi e vj, onde é realizada de forma simetricamente, depois retorna a matriz atualizada
def insereAresta(matriz, vi, vj):
    matriz[vi][vj] += 1
    matriz[vj][vi] += 1
    print('Aresta entre',vi, 'e', vj, 'inserida \n')
    return matriz

# a função insere vertice recebe o id do vertice a ser criado e atualiza a matriz com o mesmo
def insereVertice(matriz, vi):
    qtdVertices = np.shape(matriz)[0] # recebe a qtd de vertice
    strg = "" #string usada para criar a nova matriz
    for v in range(0, qtdVertices+1):  # Para cada vértice vi
        for vj in range(0, qtdVertices+1):  # Para cada vértice vj
            if(v==qtdVertices) or (vj==qtdVertices):
                strg+= "0 " # aqui é onde o vertice esta sendo inserido, com o valor 0 para todas suas posicoes
            else:
                if (matriz[v][vj] > 0): # se a matriz for maior que 0 ele envia o valor para a string
                    aux = str(matriz[v][vj]) + " " # recebe o str com uma variavel auxiliar
                    strg += aux #add na string
                else:   # se nao for maior, entao é sempre 0, enviando tambem para a string
                    aux = str(matriz[v][vj]) + " "
                    strg += aux
        strg += "\n"    # pula uma linha na string
    s = StringIO(strg) # transforma a string para a matriz
    data = np.genfromtxt(s) # nova matriz de adjacencia criada.
    print('Vertice', vi, 'inserida \n')
    return data

def removeAresta(matriz, vi, vj):
    qtdVertices = np.shape(matriz)[0] # recebe a qtd de vertice
    tipo = 0 # tipo simples se nao cair em outro if
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        for vj in range(0, qtdVertices):  # Para cada vértice vj
            if (matriz[vi][vj] != matriz[vj][vi]):  # digrafo, pois a matriz eh assimetrica
                tipo = 1 # depois de verificar se eh digrafo recebe 1 se sim
    if(tipo == 1):
        matriz[vi][vj] -=1  # se for digrafo so altera um valor na matriz, pois n é simetrico
    else:   # se nao for digrafo altera dois valores, pois precisa ter simetria
        matriz[vi][vj] -= 1
        matriz[vj][vi] -= 1
    print('Aresta entre', vi, 'e', vj, 'removida \n')
    return matriz

def removeVertice(matriz, vi): # funcao que remove um vertice desejado, enviado como parametro
    qtdVertices = np.shape(matriz)[0] # recebe a qtd de vertice
    strg = "" #string usada para criar a nova matriz
    if(vi == qtdVertices): # se o vertice for o ultimo, ele cai aqui, entao so ira mudar a string com a qtdVertices - 1, dessa forma ele ira remover a ultima coluna e linha da matriz, removendo o vertice
        for v in range(0, qtdVertices-1):  # Para cada vértice vi
            for vj in range(0, qtdVertices-1):  # Para cada vértice vj
                if (matriz[v][vj] > 0):
                    aux = str(matriz[v][vj]) + " "
                    strg += aux
                else:
                    aux = str(matriz[v][vj]) + " "
                    strg += aux
            strg += "\n"
    else:   # se nao for, ele precisa verificar onde nao passa pelo vertice, pulando quando estiver na posicao dele, removendo dessa forma
        for v in range(0, qtdVertices):  # Para cada vértice vi
            for vj in range(0, qtdVertices):  # Para cada vértice vj
                if (v != vi) and (vj != vi):
                    if (matriz[v][vj] > 0):
                        aux = str(matriz[v][vj])+ " "
                        strg += aux
                    else:
                        aux = str(matriz[v][vj]) + " "
                        strg += aux
            if(v!=vi):
                strg += "\n"
    s = StringIO(strg) # transforma a string para a matriz
    data = np.genfromtxt(s) # nova matriz data
    print('Vertice', vi, 'removido \n')
    return data # matriz atualizada


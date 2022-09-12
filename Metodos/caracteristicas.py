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

def insereAresta(matriz, vi, vj):
    matriz[vi][vj] += 1
    matriz[vj][vi] += 1
    print('Aresta entre',vi, 'e', vj, 'inserida \n')
    return matriz

def insereVertice(matriz, vi):
    qtdVertices = np.shape(matriz)[0]
    strg = ""
    for v in range(0, qtdVertices+1):  # Para cada vértice vi
        for vj in range(0, qtdVertices+1):  # Para cada vértice vj
            if(v==qtdVertices) or (vj==qtdVertices):
                strg+= "0 "
            else:
                if (matriz[v][vj] > 0):
                    aux = str(matriz[v][vj]) + " "
                    strg += aux
                else:
                    aux = str(matriz[v][vj]) + " "
                    strg += aux
        strg += "\n"
    s = StringIO(strg)
    data = np.genfromtxt(s)
    print('Vertice', vi, 'inserida \n')
    return data

def removeAresta(matriz, vi, vj):
    qtdVertices = np.shape(matriz)[0]
    tipo = 0
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        for vj in range(0, qtdVertices):  # Para cada vértice vj
            if (matriz[vi][vj] != matriz[vj][vi]):  # digrafo, pois a matriz eh assimetrica
                tipo = 1
    if(tipo == 1):
        matriz[vi][vj] -=1
    else:
        matriz[vi][vj] -= 1
        matriz[vj][vi] -= 1
    print('Aresta entre', vi, 'e', vj, 'removida \n')
    return matriz

def removeVertice(matriz, vi):
    qtdVertices = np.shape(matriz)[0]
    strg = ""
    if(vi == qtdVertices):
        for v in range(0, qtdVertices-1):  # Para cada vértice vi
            for vj in range(0, qtdVertices-1):  # Para cada vértice vj
                if (matriz[v][vj] > 0):
                    aux = str(matriz[v][vj]) + " "
                    strg += aux
                else:
                    aux = str(matriz[v][vj]) + " "
                    strg += aux
            strg += "\n"
    else:
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
    s = StringIO(strg)
    data = np.genfromtxt(s)
    print('Vertice', vi, 'removido \n')
    return data


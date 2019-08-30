import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle
from collections import defaultdict

mpl.use('Agg')


def gera_lista_aleatoria(tamanho):
    lista = list(range(1, tamanho + 1))
    shuffle(lista)
    return lista

def desenha_grafico(x, y, figura, xLabel="Entradas", yLabel="Saídas"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Bucket Sort")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(figura)


def bucket_sort(lista):
    maior_numero = max(lista)
    tamanho_lista = len(lista)
    size = maior_numero / tamanho_lista
    cesta = [[] for _ in range(tamanho_lista)]

    for i in range(tamanho_lista):
        j = int(lista[i] / size)
        if j != tamanho_lista:
            cesta[j].append(lista[i])
        else:
            cesta[tamanho_lista - 1].append(lista[i])

    for i in range(tamanho_lista):
        insertion_sort(cesta[i])

    resultado = []

    for i in range(tamanho_lista):
        resultado = resultado + cesta[i]

    return resultado


def insertion_sort(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while (j >= 0 and temp < lista[j]):
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = temp

lista_com_tamanhos = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo_lista_aleatoria = []

for i in range(len(lista_com_tamanhos)):
    lista_aleatoria = gera_lista_aleatoria(lista_com_tamanhos[i])
    tempo_lista_aleatoria.append(
        timeit.timeit("bucket_sort({})".format(lista_aleatoria),
                      setup="from __main__ import bucket_sort", number=1))

desenha_grafico(lista_com_tamanhos, tempo_lista_aleatoria, "Tempo.png")

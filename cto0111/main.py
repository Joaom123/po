import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')

def gera_lista_aleatoria(tamanho):
    lista = list(range(1, tamanho + 1))
    shuffle(lista)
    return lista

def desenha_grafico(x, y, figura, xLabel="Entradas", yLabel="Saídas"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Lista aleatória")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(figura)


def gnome_sort(lista):
    tamanho_lista = len(lista)
    indice = 0
    while indice < tamanho_lista:
        if indice == 0:
            indice = indice + 1
        if lista[indice] >= lista[indice - 1]:
            indice = indice + 1
        else:
            lista[indice], lista[indice - 1] = lista[indice - 1], lista[indice]
            indice = indice - 1
    return lista


lista_com_tamanhos = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo_lista_aleatoria = []

for i in range(len(lista_com_tamanhos)):
    lista_aleatoria = gera_lista_aleatoria(lista_com_tamanhos[i])
    tempo_lista_aleatoria.append(
        timeit.timeit("gnome_sort({})".format(lista_aleatoria),
                      setup="from __main__ import gnome_sort", number=1))
desenha_grafico(lista_com_tamanhos, tempo_lista_aleatoria, "Tempo.png", 'Tamanho da lista', 'Tempo')
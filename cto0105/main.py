import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')

def gera_lista_aleatoria(tamanho):
    lista = list(range(1, tamanho + 1))
    shuffle(lista)
    return lista

def desenha_grafico(x, y, figura, xLabel ="Entradas", yLabel ="Saídas"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label ="Lista aleatória")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(figura)


def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        E = lista[:meio]
        D = lista[meio:]
        merge_sort(E)
        merge_sort(D)

        i = j = k = 0
        while i < len(E) and j < len(D):
            if E[i] < D[j]:
                lista[k] = E[i]
                i += 1
            else:
                lista[k] = D[j]
                j += 1
            k += 1

        while i < len(E):
            lista[k] = E[i]
            i += 1
            k += 1

        while j < len(D):
            lista[k] = D[j]
            j += 1
            k += 1


lista_com_tamanhos = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo_lista_aleatoria = []

for i in range(len(lista_com_tamanhos)):
    lista_aleatoria = gera_lista_aleatoria(lista_com_tamanhos[i])
    tempo_lista_aleatoria.append(timeit.timeit("shell_sort({})".format(lista_aleatoria), setup="from __main__ import shell_sort", number=1))

desenha_grafico(lista_com_tamanhos, tempo_lista_aleatoria, "Tempo.png", 'Tamanho da lista', 'Tempo')
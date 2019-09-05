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

def radix_sort(lista):
    base_exp = 1
    maior_numero = max(lista)

    while maior_numero/base_exp > 0:
        indice = len(lista) + 1
        numero_ocorrencias = [0] * indice

        for i in lista:
            numero_ocorrencias[i] += 1

        k = 0
        for i in range(indice):
            for j in range(numero_ocorrencias[i]):
                lista[k] = i
                k += 1
        base_exp *= 10


def heap_sort(lista):
    for inicio in range((len(lista) - 2) // 2, -1, -1):
        peneira(lista, inicio, len(lista) - 1)

    for fim in range(len(lista) - 1, 0, -1):
        lista[fim], lista[0] = lista[0], lista[fim]
        peneira(lista, 0, fim - 1)
    return lista


def peneira(lista, inicio, fim):
    raiz = inicio
    while True:
        filho = raiz * 2 + 1
        if filho > fim: break
        if filho + 1 <= fim and lista[filho] < lista[filho + 1]:
            filho += 1
        if lista[raiz] < lista[filho]:
            lista[raiz], lista[filho] = lista[filho], lista[raiz]
            raiz = filho
        else:
            break

lista_com_tamanhos = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo_lista_aleatoria = []

for i in range(len(lista_com_tamanhos)):
    lista_aleatoria = gera_lista_aleatoria(lista_com_tamanhos[i])
    tempo_lista_aleatoria.append(
        timeit.timeit("heap_sort({})".format(lista_aleatoria),
                      setup="from __main__ import heap_sort", number=2))

#lista_com_tamanhos = [100000, 200000, 400000, 500000, 1000000, 2000000]
desenha_grafico(lista_com_tamanhos, tempo_lista_aleatoria, "Tempo.png", 'Tamanho da lista', 'Tempo')
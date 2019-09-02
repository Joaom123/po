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

lista_com_tamanhos = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo_lista_aleatoria = []

for i in range(len(lista_com_tamanhos)):
    lista_aleatoria = gera_lista_aleatoria(lista_com_tamanhos[i])
    tempo_lista_aleatoria.append(
        timeit.timeit("radix_sort({})".format(lista_aleatoria),
                      setup="from __main__ import radix_sort", number=1))

#lista_com_tamanhos = [100000, 200000, 400000, 500000, 1000000, 2000000]
desenha_grafico(lista_com_tamanhos, tempo_lista_aleatoria, "Tempo.png", 'Tamanho da lista', 'Tempo')
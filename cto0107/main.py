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
    ax.plot(x, y, label="Lista aleatória")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(figura)

def count_sort(lista):
    menor_numero_da_lista = min(lista)
    maior_numero_da_lista = max(lista)
    contagem = defaultdict(int)

    for i in lista:
        contagem[i] += 1
    resultado = []

    for j in range(menor_numero_da_lista, maior_numero_da_lista + 1):
        resultado += [j] * contagem[j]

    return resultado

lista_com_tamanhos = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo_lista_aleatoria = []

for i in range(len(lista_com_tamanhos)):
    lista_aleatoria = gera_lista_aleatoria(lista_com_tamanhos[i])
    tempo_lista_aleatoria.append(
        timeit.timeit("bucket_sort({})".format(lista_aleatoria),
                      setup="from __main__ import bucket_sort", number=1))

desenha_grafico(lista_com_tamanhos, tempo_lista_aleatoria, "Tempo.png", 'Tamanho da lista', 'Tempo')

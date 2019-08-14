import random
import timeit
import matplotlib.pyplot as plt

def particao(lista, inicio, fim):
    pivo = lista[fim - 1]
    for i in range(inicio, fim):
        if not lista[i] > pivo:
            lista[inicio], lista[i] = lista[i], lista[inicio]
            inicio += 1
    return inicio - 1

def pivoAleatorio(lista, inicio, fim):
    rand = random.randrange(inicio, fim)
    lista[fim - 1], lista[rand] = lista[rand], lista[fim - 1]
    return particao(lista, inicio, fim)

def quickSort(lista, inicio, fim):
    if inicio < fim:
        pivo = pivoAleatorio(lista, inicio, fim)
        quickSort(lista, inicio, pivo)
        quickSort(lista, pivo + 1, fim)
    return lista

def desenha_grafico(x, y, file_name, label1, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


lista_tamanhos = [100000, 200000, 400000, 500000, 1000000, 2000000]
lista_tempo = []

for i in range(len(lista_tamanhos)):
    lista_invertida = list(range(lista_tamanhos[i], 0, -1))
    lista_tempo.append(timeit.timeit("quickSort({}, {}, {})".format(lista_invertida, 0, len(lista_invertida)),
                                     setup="from __main__ import quickSort, pivoAleatorio, particao", number=1))


desenha_grafico(lista_tamanhos, lista_tempo, "Grafico.png", "Tempo", xl="Tamanho da lista", yl="Tempo")
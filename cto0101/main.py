from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

mpl.use('Agg')

def bolha(lista):
    quantidade_de_trocas = 0
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if(lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                quantidade_de_trocas += 1
    return quantidade_de_trocas



def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", z = 'Graph.png', l = "Melhor tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = l)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(z)

   
x2 = [10000,20000,50000,100000]
y = []
y2= []

for i in range(4):
    listaAleatoria = geraLista(x2[i])

    y.append(timeit.timeit("bolha({})".format(listaAleatoria),setup="from __main__ import bolha",number=1))
  
    y2.append(bolha(listaAleatoria))

#print(y)
#print(y2)
desenhaGrafico(x2,y)
desenhaGrafico(x2,y2, z = 'Graph2.png', l = "Quantidade de Operações")


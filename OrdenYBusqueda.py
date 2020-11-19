
#####################################
############# QUICKSORT #############
#####################################
def quickSort(lista):
    quickSortAux(lista, 0, lista.len()-1)


def quickSortAux(lista, inicio, fin):
    if inicio < fin:
        particion = particionar(lista, inicio, fin)
        quickSortAux(lista, inicio, particion-1)
        quickSortAux(lista, particion+1, fin)


def particionar(lista, inicio, fin):
    pivote = lista.get(inicio)
    izquierda = inicio + 1
    derecha = fin
    terminado = False
    while terminado is False:
        while izquierda <= derecha and lista.get(izquierda) <= pivote:
            izquierda += 1
        while izquierda <= derecha and lista.get(derecha) >= pivote:
            derecha -= 1
        if derecha < izquierda:
            terminado = True
        else:
            lista.intercambiarDatos(izquierda, derecha)
    lista.intercambiarDatos(inicio, derecha)
    return derecha


######################################
########## BUSQUEDA BINARIA ##########
######################################
# recibe una lista, un elemento, y los indices minimo y maximo donde se hara la busqueda
# retorna el indice del elemento
def binarySearch(lista, elemento, indiceIzq, indiceDer):
    medio = (indiceIzq + indiceDer) // 2
    resultado = None
    if indiceIzq <= indiceDer:
        if lista.get(medio) > elemento:
            resultado = binarySearch(lista, elemento, indiceIzq, medio - 1)
        elif lista.get(medio) < elemento:
            resultado = binarySearch(lista, elemento, medio + 1, indiceDer)
        else:
            resultado = medio
    return resultado
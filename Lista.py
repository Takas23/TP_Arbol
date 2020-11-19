from OrdenYBusqueda import *


###################
###### NODO #######
###################
class NodoLista:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def __repr__(self):
        strOut = str(self.dato)
        if self.tieneSiguiente():
            strOut = strOut + " > " + self.siguiente.__repr__()
        return strOut

    def tieneSiguiente(self):
        return self.siguiente is not None

# reemplazado por insertarOrden()
    def append(self, nodoNuevo):
        if not self.tieneSiguiente():
            self.siguiente = nodoNuevo
        else:
            self.siguiente.append(nodoNuevo)

    def len(self):
        cant = 1
        if self.tieneSiguiente():
            cant = cant + self.siguiente.len()
        return cant

    def get(self, pos, posActual=0):
        dato = None
        if pos == posActual:
            dato = self.dato
        else:
            dato = self.siguiente.get(pos, posActual+1)
        return dato

#    def getNodo(self, pos, posActual=0):
#        dato = None
#        if pos == posActual:
#            dato = self
#        elif self.tieneSiguiente():
#           dato = self.siguiente.get(pos, posActual+1)
#        return dato

    def eliminarPos(self, pos, posAct = 0):
        if posAct == pos -1:
            self.siguiente = self.siguiente.siguiente
        else:
            self.siguiente.eliminarPos(pos, posAct+1)

#    def getPos(self, elemento, posActual=0):
#        posicion = None
#        if elemento == self.dato:
#            posicion = posActual
#        elif self.tieneSiguiente():
#            posicion = self.siguiente.getPos(elemento, posActual+1)
#        return posicion

    def insertarOrden(self, nodoNuevo):
        if self.tieneSiguiente():
            if self.dato < nodoNuevo.dato:
                if nodoNuevo.dato < self.siguiente.dato:
                    nodoNuevo.siguiente = self.siguiente
                    self.siguiente = nodoNuevo
                elif nodoNuevo.dato > self.siguiente.dato:
                    self.siguiente.insertarOrden(nodoNuevo)
        else:
            self.siguiente = nodoNuevo

    def eliminarRep(self):
        if self.tieneSiguiente():
            if self.dato == self.siguiente.dato:
                self.siguiente = self.siguiente.siguiente
                self.eliminarRep()
            else:
                self.siguiente.eliminarRep()


####################
###### LISTA #######
####################
class Lista:
    def __init__(self):
        self.primero = None

    def __repr__(self):
        strOut = ""
        if not self.estaVacia():
            strOut = self.primero.__repr__()
        return strOut

    def estaVacia(self):
        return self.primero is None

# reemplazado por append()
# OK - agrega al final,
    # Recursiva en NodoLista
    def append(self, dato):
        nodoNuevo = NodoLista(dato)
        if self.estaVacia():
            self.primero = nodoNuevo
        else:
            self.primero.append(nodoNuevo)

# append modificado para que siempre este ordenada
# Puede dar ERROR al hacer un append(lista). usar appendList()
    def appendOrd(self, dato):
        self.insertarOrden(dato)

# OK
    # Recursiva en NodoLista
    def len(self):
        cant = 0
        if not self.estaVacia():
            cant = self.primero.len()
        return cant

# OK - retorna el DATO en la posicion dada.
    # Recursiva en NodoLista
    def get(self, pos):
        dato = None
        if self.estaVacia():
            raise Exception("Lista vacia")
        elif 0 <= pos < self.len():
            dato = self.primero.get(pos)
        else:
            raise Exception("Posicion no valida")
        return dato

# OK - elimina el nodo en la posiocion dada
    # recursiva en nodo
    def eliminarPos(self, pos):
        if 0 <= pos < self.len():
            if pos == 0:
                self.primero = self.primero.siguiente
            else:
                self.primero.eliminarPos(pos)

# OK - devuelve la POSICION en que esta el elemento buscado
    def getPos(self, elemento):
        return binarySearch(self, elemento, 0, self.len() - 1)

# OK - Agrega los nodos de una lista a otra (Sin repetidos y en orden alfabetico)
    def appendList(self, lista):
        count = 0
        while count < lista.len():
            if not self.contiene(lista.get(count)):
                self.append(lista.get(count))
            count += 1

# OK - true si existe en la lista
    def contiene(self, elemento):
        salida = False
        if not self.estaVacia():
            if self.getPos(elemento) is not None:
                salida = True
        return salida

# OK - inserta el elemento de manera ordenada
    # recursiva en nodo
    def insertarOrden(self, elemento):
        nodoNuevo = NodoLista(elemento)
        if self.estaVacia():
            self.primero = nodoNuevo
        elif self.primero.dato > elemento:
            nodoNuevo.siguiente = self.primero
            self.primero = nodoNuevo
        else:
            self.primero.insertarOrden(nodoNuevo)

# OK - elimina los elementos repetidos de la lista
    def eliminarRep(self):
        if not self.estaVacia():
            self.primero.eliminarRep()

# OK - recibe 2 posiciones de una lista e intercambia sus DATOS
# pos1 < pos2
    def intercambiarDatos(self, pos1, pos2):
        if self.len() > pos2:
            datoAux1 = self.get(pos1)
            datoAux2 = self.get(pos2)
            nodoActual = self.primero
            posAct = 0
            while posAct < pos1:
                nodoActual = nodoActual.siguiente
                posAct += 1
            nodoActual.dato = datoAux2
            while posAct < pos2:
                nodoActual = nodoActual.siguiente
                posAct += 1
            nodoActual.dato = datoAux1




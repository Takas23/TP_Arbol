from Lista import *
#from graphviz import Digraph


###################
###### NODO #######
###################
class NodoArbolDeCanciones:
    def __init__(self, interprete):
        self.interprete = interprete
        self.canciones = Lista()
        self.izquierdo = None
        self.derecho = None

    def __repr__(self):
        return str(self.interprete)

    def tieneIzquierdo(self):
        return self.izquierdo is not None

    def tieneDerecho(self):
        return self.derecho is not None

    def grado(self):
        grado = 0
        if self.tieneIzquierdo():
            grado += 1
        if self.tieneDerecho():
            grado += 1
        return grado

    def maximo(self):
        nodoMax = self
        if self.tieneDerecho():
            nodoMax = self.derecho.maximo()
        return nodoMax

    def predecesor(self):
        pred = None
        if self.tieneIzquierdo():
            pred = self.izquierdo.maximo()
        return pred

# a > A
    def insertarInterprete(self, nodoNuevo):
        if nodoNuevo.interprete < self.interprete:
            if not self.tieneIzquierdo():
                self.izquierdo = nodoNuevo
            else:
                self.izquierdo.insertarInterprete(nodoNuevo)
        elif nodoNuevo.interprete > self.interprete:
            if not self.tieneDerecho():
                self.derecho = nodoNuevo
            else:
                self.derecho.insertarInterprete(nodoNuevo)
        else:
            raise Exception("El Interprete esta cargado")

    def mostrarPreOrden(self):
        print(self.interprete)
        if self.tieneIzquierdo():
            self.izquierdo.mostrarPreOrden()
        if self.tieneDerecho():
            self.derecho.mostrarPreOrden()

    def buscarInterprete(self, interprete):
        nodo = None
        if self.interprete == interprete:
            nodo = self
        elif self.interprete > interprete:
            if self.tieneIzquierdo():
                nodo = self.izquierdo.buscarInterprete(interprete)
        else:
            if self.tieneDerecho():
                nodo = self.derecho.buscarInterprete(interprete)
        return nodo

    def insertarListaCanciones(self, lista):
        self.canciones.appendList(lista)

    def interpretesDeCancion(self, nombreCancion):
        interpretes = Lista()
        if self.canciones.contiene(nombreCancion):
            interpretes.appendOrd(self.interprete)
        if self.tieneIzquierdo():
            interpretes.appendList(self.izquierdo.interpretesDeCancion(nombreCancion))
        if self.tieneDerecho():
            interpretes.appendList(self.derecho.interpretesDeCancion(nombreCancion))
        return interpretes

    def eliminarInterprete(self, interprete):
        if interprete < self.interprete:
            if self.tieneIzquierdo() and self.izquierdo.interprete == interprete:
                if self.izquierdo.grado() == 2:
                    nodoPred = self.izquierdo.predecesor()
                    self.izquierdo.eliminarInterprete(nodoPred.interprete)
                    nodoPred.izquierdo = self.izquierdo.izquierdo
                    nodoPred.derecho = self.izquierdo.derecho
                    self.izquierdo = nodoPred
                elif self.izquierdo.tieneIzquierdo():
                    self.izquierdo = self.izquierdo.izquierdo
                elif self.izquierdo.tieneDerecho():
                    self.izquierdo = self.izquierdo.derecho
                else:
                    self.izquierdo = None
            elif self.tieneIzquierdo():
                self.izquierdo.eliminarInterprete(interprete)
        elif interprete > self.interprete:
            if self.tieneDerecho() and self.derecho.interprete == interprete:
                if self.derecho.grado() == 2:
                    nodoPred = self.derecho.predecesor()
                    self.derecho.eliminarInterprete(nodoPred.interprete)
                    nodoPred.izquierdo = self.derecho.izquierdo
                    nodoPred.derecho = self.derecho.derecho
                    self.derecho = nodoPred
                elif self.derecho.tieneIzquierdo():
                    self.derecho = self.derecho.izquierdo
                elif self.derecho.tieneDerecho():
                    self.derecho = self.derecho.derecho
                else:
                    self.derecho = None
            elif self.tieneDerecho():
                self.derecho.eliminarInterprete(interprete)

    def eliminarCancion(self, cancion):
        if self.canciones.contiene(cancion):
            self.canciones.eliminarPos(self.canciones.getPos(cancion))
        if self.tieneIzquierdo():
            self.izquierdo.eliminarCancion(cancion)
        if self.tieneDerecho():
            self.derecho.eliminarCancion(cancion)

    def altura(self):
        alturaNodo = 0
        if self.grado() == 2:
            alturaNodo = 1 + max(self.izquierdo.altura(), self.derecho.altura())
        elif self.tieneIzquierdo():
            alturaNodo = 1 + self.izquierdo.altura()
        elif self.tieneDerecho():
            alturaNodo = 1 + self.derecho.altura()
        return alturaNodo

# OK - creo
    def cancionesEnNivel(self, nivel):
        nivelActual = 0
        cancionesNivel = Lista()
        while nivel >= nivelActual:
            if nivel == nivelActual:
                cancionesNivel.appendList(self.canciones)
            else:
                if self.tieneIzquierdo():
                    nivelActual += 1
                    cancionesNivel = self.izquierdo.cancionesEnNivel(nivel)
                if self.tieneDerecho():
                    nivelActual += 1
                    cancionesNivel = self.derecho.cancionesEnNivel(nivel)
            nivelActual += 1

        return cancionesNivel

    def cantidadTotalInterpretes(self, palabra):
        cant = 0
        if palabra in self.interprete:
            cant += 1
        if self.tieneIzquierdo():
            cant = cant + self.izquierdo.cantidadTotalInterpretes(palabra)
        if self.tieneDerecho():
            cant = cant + self.derecho.cantidadTotalInterpretes(palabra)
        return cant

    def interpretesConMasCanciones(self, cantidadCancionesMinima):
        cantidadInterpretes = 0
        if self.canciones.len() >= cantidadCancionesMinima:
            cantidadInterpretes += 1
        if self.tieneIzquierdo():
            cantidadInterpretes += self.izquierdo.interpretesConMasCanciones(cantidadCancionesMinima)
        if self.tieneDerecho():
            cantidadInterpretes += self.derecho.interpretesConMasCanciones(cantidadCancionesMinima)
        return cantidadInterpretes

    def internosAlfabetico(self):
        interpretes = Lista()
        if self.grado() != 0:
            interpretes.append(self.interprete)
        if self.tieneIzquierdo():
            interpretes.appendList(self.izquierdo.internosAlfabetico())
        if self.tieneDerecho():
            interpretes.appendList(self.derecho.internosAlfabetico())
        return interpretes


####################################################
####################################################
#    def treePlot(self, dot):
#        if self.tieneIzquierdo():
#            dot.node(str(self.izquierdo.interprete), str(self.izquierdo.interprete)+"\n"+str(self.izquierdo.canciones))
#            dot.edge(str(self.interprete), str(self.izquierdo.interprete))
#            self.izquierdo.treePlot(dot)
#        else:
#            dot.node("None"+str(self.interprete)+"l", "None")
#            dot.edge(str(self.interprete), "None"+str(self.interprete)+"l")
#        if self.tieneDerecho():
#            dot.node(str(self.derecho.interprete), str(self.derecho.interprete)+"\n"+str(self.derecho.canciones))
#            dot.edge(str(self.interprete), str(self.derecho.interprete))
#            self.derecho.treePlot(dot)
#        else:
#            dot.node("None"+str(self.interprete)+"r", "None")
#            dot.edge(str(self.interprete), "None"+str(self.interprete)+"r")


#####################
####### ARBOL #######
#####################
class ArbolDeCanciones:
    def __init__(self):
        self.raiz = None

# ok - retorna T si esta vacio
    def estaVacio(self):
        return self.raiz is None

# OK - agrega las canciones (sin Repetidas) al artista o crea el artista con las canciones
    def insertarCanciones(self, listaCanciones, nombreInterprete):
        if self.buscarInterprete(nombreInterprete) is None:
            self.insertarInterprete(nombreInterprete)
        self.buscarInterprete(nombreInterprete).insertarListaCanciones(listaCanciones)

# OK - retorna el o los artistas que tienen una cancion con ese nombre, o lista vacia
    # Recursiva en nodo
    def interpretesDeCancion(self, nombreCancion):
        listaInterpretes = Lista()
        if not self.estaVacio():
            listaInterpretes.append(self.raiz.interpretesDeCancion(nombreCancion))
        quickSort(listaInterpretes)
        return listaInterpretes

# OK - retorna una lista de canciones compartidads entre la lista de artistas recibida
    def buscarCanciones(self, listaInterpretes):
        interpretes = listaInterpretes.len() - 1
        lCancionesComun = Lista()
        lCancionesAux = self.cancionesDe(listaInterpretes.get(interpretes))
        count = 0
        while interpretes > 0:
            while count < lCancionesAux.len():
                if self.cancionesDe(listaInterpretes.get(interpretes-1)).contiene(lCancionesAux.get(count)):
                    lCancionesComun.append(lCancionesAux.get(count))
                count += 1
            interpretes -= 1
            count = 0
        quickSort(lCancionesComun)
        lCancionesComun.eliminarRep()
        return lCancionesComun

# OK - elimina el interprete recibido
    # recursiva en nodo
    def eliminarInterprete(self, nombreInterprete):
        if not self.estaVacio():
            if self.raiz.interprete == nombreInterprete:
                if self.raiz.grado() == 2:
                    nodoPred = self.raiz.predecesor()
                    self.raiz.eliminarInterprete(nodoPred.interprete)
                    nodoPred.izquierdo = self.raiz.izquierdo
                    nodoPred.derecho = self.raiz.derecho
                    self.raiz = nodoPred
                elif self.raiz.tieneIzquierdo():
                    self.raiz = self.raiz.izquierdo
                elif self.raiz.tieneDerecho():
                    self.raiz = self.raiz.derecho
                else:
                    self.raiz = None
            else:
                self.raiz.eliminarInterprete(nombreInterprete)

# OK - elimina la cancion de todos los interpretes donde se encuentre
    # recursiva en nodo
    def eliminarCancion(self, nombreCancion):
        if not self.estaVacio():
            self.raiz.eliminarCancion(nombreCancion)

# OK - retorna la cantidad de interpretes que contienen la palabra en su nombre (ej: ab -> dab)
    # recursiva en nodo
    def cantidadTotalInterpretes(self, palabra):
        cant = 0
        if not self.estaVacio():
            cant += self.raiz.cantidadTotalInterpretes(palabra)
        return cant

# OK - creo...
# retorna T si la diferencia de altura entre los subarboles de la raiz es menor o igual a 1
    def raizBalanceada(self):
        diferencia = 0
        if not self.estaVacio():
            if self.raiz.grado() == 2:
                diferencia = self.raiz.izquierdo.altura() - self.raiz.altura()
            if self.raiz.tieneIzquierdo():
                diferencia = self.raiz.izquierdo.altura()
            if self.raiz.tieneDerecho():
                diferencia = self.raiz.derecho.altura()
        return abs(diferencia) >= 1

# OK - retorna una lista con las canciones de todos los interpretes en ese niveldel arbol (sin repetidas y en orden)
    # recursiva en nodo
    def cancionesEnNivel(self, nivel):
        cancionesNivel = Lista()
        if self.altura() >= nivel:
            cancionesNivel = self.raiz.cancionesEnNivel(nivel)
        else:
            raise Exception("Nivel no valido")
        quickSort(cancionesNivel)
        cancionesNivel.eliminarRep()
        return cancionesNivel

# OK - retorna la cantidad de interpretes que tienen como minimo la cantidad recibida de canciones
    # recursiva en nodo
    def interpretesConMasCanciones(self, cantidadCancionesMinima):
        cantidadInterpretes = 0
        if not self.estaVacio():
            cantidadInterpretes = self.raiz.interpretesConMasCanciones(cantidadCancionesMinima)
        return cantidadInterpretes

# retorna una lista(en orden alfab) con los interpretes (que sean nodo interno. NO HOJA.
    # en este caso la raiz siempre estara incluida aunque sea el unico nodo)
    def internosAlfabetico(self):
        interpretes = Lista()
        if not self.estaVacio():
            interpretes.append(self.raiz.interprete)
            interpretes.appendList(self.raiz.internosAlfabetico())
        quickSort(interpretes)
        return interpretes

#######################
#######################
# OK
    # Recursiva en nodo
    def mostrarPreOrden(self):
        if not self.estaVacio():
            self.raiz.mostrarPreOrden()

# OK
    # recursiva en NodoArbolDeCanciones()
    def insertarInterprete(self, interprete):
        nodoNuevo = NodoArbolDeCanciones(interprete)
        if self.estaVacio():
            self.raiz = nodoNuevo
        else:
            self.raiz.insertarInterprete(nodoNuevo)

# OK - Busca un interprete y retorna el nodo
    # Recursiva en nodo
    def buscarInterprete(self, interprete):
        nodo = None
        if not self.estaVacio():
            nodo = self.raiz.buscarInterprete(interprete)
#        else:
#            raise Exception("Arbol vacio")
        return nodo

# OK - retorna la lista de canciones de un interprete
    def cancionesDe(self, interprete):
        return self.buscarInterprete(interprete).canciones

# OK - retorna la altura total del arbol
    def altura(self):
        altura = 0
        if not self.estaVacio():
            altura = self.raiz.altura()
        return altura

####################################################
####################################################
#    def treePlot(self, fileName='tree'):
#        if not self.estaVacio():
#            treeDot = Digraph()
#            treeDot.node(str(self.raiz.interprete), str(self.raiz.interprete+"\n"+str(self.raiz.canciones)))
#            self.raiz.treePlot(treeDot)
#            treeDot.render(fileName, view=True)
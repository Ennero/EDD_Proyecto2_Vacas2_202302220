from clases import Ruta
import graphviz

class NodoListaAdyacente:
    def __init__(self, origen:str):
        self.origen = origen
        self.siguiente:NodoListaAdyacente = None
        self.atras:NodoRuta = None


    def buscar(self, destino:str):
        aux = self.atras
        while aux:
            if aux.destino == destino:
                return aux
            aux = aux.atras
        return None

    def insertar(self, destino:str, peso:float):
        #Aquí busco si ya existe la ruta de destino
        aux = self.buscar(destino)
        if aux:
            aux.peso = peso
            return
        nuevo = NodoRuta(peso, destino)
        if self.atras is None:
            self.atras = nuevo
        else:
            aux = self.atras
            while aux.atras:
                aux = aux.atras
            aux.atras = nuevo


class NodoRuta:
    def __init__(self, peso:float, destino:str):
        self.peso:float = peso
        self.destino:str = destino
        self.atras:NodoRuta = None


class ListaAdyacente:
    def __init__(self):
        self.inicio = None

    def buscar(self, origen:str):
        aux = self.inicio
        while aux:
            if aux.origen == origen:
                return aux
            aux = aux.siguiente
        return None

    #Función para insertar una ruta
    def insertarRuta(self, origen:str, destino:str, peso:float):
        #Aquí busco que exista el nodo de origen
        aux = self.buscar(origen)
        if aux:
            aux.insertar(destino, peso)
            return
        
        nuevo = NodoListaAdyacente(origen)
        nuevo.insertar(destino, peso)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            aux = self.inicio
            while aux.siguiente:
                aux = aux.siguiente
            aux.siguiente = nuevo

#Función para generar el grafo
    def generarGrafo(self):
        grafica = graphviz.Digraph('Grafo', filename='Rutas.gv', format='pdf')
        grafica.attr(rankdir='LR', size='8,5')
        grafica.node_attr.update(color='lightblue2', style='filled')
        grafica.edge_attr.update(color='blue', style='dotted')
        grafica.attr('node', shape='circle')
        grafica.attr('edge', dir='none')
        aux = self.inicio
        while aux:
            grafica.node(aux.origen)
            aux2 = aux.atras
            while aux2:
                grafica.edge(aux.origen, aux2.destino, label=str(aux2.peso))
                aux2 = aux2.atras
            aux = aux.siguiente
        grafica.view()



listita=ListaAdyacente()
listita.insertarRuta("A","B",5)
listita.insertarRuta("A","C",7)
listita.insertarRuta("B","C",2)
listita.insertarRuta("B","D",4)
listita.insertarRuta("C","D",1)
listita.insertarRuta("C","E",3)
listita.insertarRuta("D","E",8)
listita.insertarRuta("D","F",6)
listita.generarGrafo()
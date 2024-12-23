from nodoArbol import NodoArbol
from graphviz import Digraph
from clases import Vehiculo

class ArbolB:
    def __init__(self, orden: int):
        self.orden: int = orden
        self.raiz: NodoArbol = NodoArbol(True)

    def insertarValor(self, valor: Vehiculo):
        raiz: NodoArbol = self.raiz

        self.insertarValorNoCompleto(raiz, valor)

        if (len(raiz.claves) > self.orden - 1):
            nodo: NodoArbol = NodoArbol()
            self.raiz = nodo
            nodo.hijos.insert(0, raiz)
            self.dividirNodo(nodo, 0)

    def insertarValorNoCompleto(self, raiz: NodoArbol, valor: Vehiculo):
        posicion: int = len(raiz.claves) - 1
        if raiz.hoja:
            #Inserto el valor en la página hoja
            raiz.claves.append(None)
            
            while posicion >= 0 and valor.getPlaca() < raiz.claves[posicion].getPlaca():
                raiz.claves[posicion + 1] = raiz.claves[posicion]
                posicion -= 1

            raiz.claves[posicion + 1] = valor

        else:

            while posicion >=0 and valor.getPlaca() < raiz.claves[posicion].getPlaca():
                posicion -= 1

            posicion += 1

            self.insertarValorNoCompleto(raiz.hijos[posicion], valor)

            if len(raiz.hijos[posicion].claves) > self.orden - 1:
                self.dividirNodo(raiz, posicion)

    def dividirNodo(self, raiz: NodoArbol, posicion: int):
        posicionMedia: int = int((self.orden - 1) / 2)

        hijo: NodoArbol = raiz.hijos[posicion]

        nodo: NodoArbol = NodoArbol(hijo.hoja)
        raiz.hijos.insert(posicion + 1, nodo)

        raiz.claves.insert(posicion, hijo.claves[posicionMedia])

        nodo.claves = hijo.claves[posicionMedia + 1:posicionMedia * 2 + 1]
        hijo.claves = hijo.claves[0:posicionMedia]

        if not hijo.hoja:
            nodo.hijos = hijo.hijos[posicionMedia + 1:posicionMedia * 2 + 2]
            hijo.hijos = hijo.hijos[0:posicionMedia + 1]
    

#-----------------------------------------------------
#GENERACIÓN DE LA GRAFICA

    #Función para generar el id único del nodito del arbol
    def crearIdNodo(self):
        #Contador interno
        self._counter += 1
        return f'node{self._counter}'

    #Función para visualizar el nodo del arbol
    def crearNodo(self, nodo: NodoArbol, nodo_id: str, grafica: Digraph):
        claves = '|'.join(str(k.getPlaca) for k in nodo.claves) #Uno las claves con un |
        #Creo el nodo en el grafo
        grafica.node(nodo_id, claves) 
        
        #Si el nodo tiene hijos, lo recorro recursivamente
        if not nodo.hoja:
            for i, hijo in enumerate(nodo.hijos):
                hijo_id = self.crearIdNodo()
                self.crearNodo(hijo, hijo_id, grafica)
                grafica.edge(nodo_id, hijo_id)

    #Función para generar la gráfica del arbol
    def generarGrafica(self, nombre='ReporteArbolB'):
        #Reinicia el contador de IDs
        self._counter = 0
        
        # Inicializar el Digraph
        grafica = Digraph(comment='Árbol B')
        grafica.attr(rankdir='TB')
        grafica.attr('node', shape='record')
        
        #Genera todo a partir de la raiz
        raiz_id = self.crearIdNodo()
        self.crearNodo(self.raiz, raiz_id, grafica)
        
        #Generar el PDF
        grafica.render(nombre, view=True, cleanup=True)
        print(f"Reporte del arbolB generado exitosamente: {nombre}.pdf")

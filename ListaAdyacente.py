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



# Clase para almacenar la información de los nodos en el algoritmo de Dijkstra
class NodoDistancia:
    def __init__(self, nodo: str):
        self.nodo = nodo
        self.distancia = float('inf') # Distancia acumulada
        self.visitado = False 
        self.siguiente = None #Referencia al siguiente nodo en la lista
        self.camino = None  #Referencia al primer nodo del camino

#Nodo para almacenar los nodos del camino
class NodoCamino:
    def __init__(self, nodo: str):
        self.nodo = nodo
        self.siguiente = None

#Clase para almacenar la estructura de los caminos
class EstructuraCaminos:
    def __init__(self):
        self.inicio = None

    #Función para insertar un nodo    
    def insertar(self, nodo: str):
        nuevo = NodoDistancia(nodo)
        if not self.inicio:
            self.inicio = nuevo
            return
        aux = self.inicio
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = nuevo

    #Función para copiar un camino
    def copiar_camino(self, caminoOrigen):
        if not caminoOrigen:
            return None
        nuevoInicio = NodoCamino(caminoOrigen.nodo)
        nuevoActual = nuevoInicio
        origenActual = caminoOrigen.siguiente
        
        while origenActual:
            nuevoActual.siguiente = NodoCamino(origenActual.nodo)
            nuevoActual = nuevoActual.siguiente
            origenActual = origenActual.siguiente
        
        return nuevoInicio

    def obtener_menor_distancia(self):
        if not self.inicio:
            return None
        menor = None
        aux = self.inicio
        while aux:
            if not aux.visitado:
                if menor is None or aux.distancia < menor.distancia:
                    menor = aux
            aux = aux.siguiente
        return menor

    def buscar(self, nodo: str):
        aux = self.inicio
        while aux:
            if aux.nodo == nodo:
                return aux
            aux = aux.siguiente
        return None










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
        # Insertar ruta original
        aux = self.buscar(origen)
        if aux:
            aux.insertar(destino, peso)
        else:
            nuevo = NodoListaAdyacente(origen)
            nuevo.insertar(destino, peso)
            if self.inicio is None:
                self.inicio = nuevo
            else:
                aux = self.inicio
                while aux.siguiente:
                    aux = aux.siguiente
                aux.siguiente = nuevo
        
        # Insertar ruta inversa automáticamente
        aux = self.buscar(destino)
        if aux:
            aux.insertar(origen, peso)
        else:
            nuevo = NodoListaAdyacente(destino)
            nuevo.insertar(origen, peso)
            if self.inicio is None:
                self.inicio = nuevo
            else:
                aux = self.inicio
                while aux.siguiente:
                    aux = aux.siguiente
                aux.siguiente = nuevo

#Función para generar el grafo
    def generarGrafo(self):
        grafica = graphviz.Digraph('Grafo', filename='Rutas', format='png')
        grafica.attr(rankdir='LR', size='8,5')
        grafica.node_attr.update(color='lightsalmon', style='filled')
        grafica.edge_attr.update(color='red', style='dotted')
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
        grafica.render()
        #grafica.view() Esto solo para comprobar de que sirva pero la veradad si sirve :)

#Aquí coloca las funciones para encontrar la ruta más corta usando dijkstra------------------------------------------

    def encontrarRutaCorta(self, origen: str, destino: str):
        caminos = EstructuraCaminos()
        
        aux = self.inicio
        while aux:
            caminos.insertar(aux.origen)
            aux = aux.siguiente
        
        nodo_origen = caminos.buscar(origen)
        if nodo_origen:
            nodo_origen.distancia = 0
            nodo_origen.camino = NodoCamino(origen)
        
        while True:
            actual = caminos.obtener_menor_distancia()
            if not actual or actual.nodo == destino:
                break
                
            actual.visitado = True
            nodo_lista = self.buscar(actual.nodo)
            
            if nodo_lista:
                vecino = nodo_lista.atras
                while vecino:
                    nodo_destino = caminos.buscar(vecino.destino)
                    if nodo_destino:
                        nueva_distancia = actual.distancia + vecino.peso
                        if nueva_distancia < nodo_destino.distancia:
                            nodo_destino.distancia = nueva_distancia
                            nodo_destino.camino = caminos.copiar_camino(actual.camino)
                            ultimo = nodo_destino.camino
                            while ultimo.siguiente:
                                ultimo = ultimo.siguiente
                            ultimo.siguiente = NodoCamino(vecino.destino)
                    vecino = vecino.atras
        
        nodo_final = caminos.buscar(destino)
        if nodo_final and nodo_final.camino:
            camino = []
            aux = nodo_final.camino
            while aux:
                camino.append(aux.nodo)
                aux = aux.siguiente
            return camino, nodo_final.distancia
        return None, float('inf')

    def mostrar_recorrido_paso_a_paso(self, origen: str, destino: str):
        camino, distancia_total = self.encontrarRutaCorta(origen, destino)
        
        if not camino:
            print(f"No existe ruta entre {origen} y {destino}")
            return
        
        print(f"\nRecorrido paso a paso de {origen} a {destino}:")
        print("-" * 50)
        
        distancia_acumulada = 0
        for i in range(len(camino) - 1):
            actual = camino[i]
            siguiente = camino[i + 1]
            
            nodo_actual = self.buscar(actual)
            peso = nodo_actual.buscar(siguiente).peso
            distancia_acumulada += peso
            
            print(f"Paso {i + 1}: {actual} -> {siguiente}")
            print(f"Distancia del tramo: {peso}")
            print(f"Distancia acumulada: {distancia_acumulada}")
            print("-" * 50)
        
        print(f"\nResumen del recorrido:")
        print(f"Ruta completa: {' -> '.join(camino)}")
        print(f"Distancia total: {distancia_total}")

    def visualizar_recorrido_lista(self, origen: str, destino: str):
        camino, distancia = self.encontrarRutaCorta(origen, destino)
        if not camino:
            print(f"No existe ruta entre {origen} y {destino}")
            return
        
        grafica = graphviz.Digraph('RecorridoLista', filename='RecorridoLista', format='png')
        grafica.attr(rankdir='TB')
        
        grafica.attr('node', shape='none', height='0', width='0')
        grafica.node('invisible', '')
        
        grafica.attr('node', shape='box', style='filled', color='lightblue')
        
        for i, nodo in enumerate(camino):
            nodo_id = f'nodo_{i}'
            
            if i < len(camino) - 1:
                siguiente = camino[i + 1]
                nodo_actual = self.buscar(nodo)
                peso = nodo_actual.buscar(siguiente).peso
                label = f"{nodo}\nDistancia al siguiente: {peso}"
            else:
                label = nodo
            
            grafica.node(nodo_id, label)
            
            if i == 0:
                grafica.edge('invisible', nodo_id)
            else:
                grafica.edge(f'nodo_{i-1}', nodo_id)
        
        grafica.render()

##Zona de pruebas------------------------------------------------------------------------------------------------------------
##Zona de pruebas------------------------------------------------------------------------------------------------------------
listita=ListaAdyacente()
# Insertamos las rutas en ambas direcciones
listita.insertarRuta("A","B",5)
listita.insertarRuta("A","C",7)
listita.insertarRuta("B","C",2)
listita.insertarRuta("B","D",4)
listita.insertarRuta("C","D",1)
listita.insertarRuta("C","E",3)
listita.insertarRuta("D","E",8)
listita.insertarRuta("D","F",6)


listita.generarGrafo()

# Ver el recorrido paso a paso
listita.mostrar_recorrido_paso_a_paso("A", "F")

# Visualizar el camino como lista vertical
listita.visualizar_recorrido_lista("A", "F")
    




##Aquí voy a meter la cosa depués para que se pueda encontrar la ruta más corta


    

    
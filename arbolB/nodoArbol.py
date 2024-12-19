class NodoArbol:
    #Constructor del nodo del arbol B
    def __init__(self, hoja: bool=False):
        self.hoja: bool = hoja #Para saber si es página hoja
        self.claves: list[int] = [] #Lista de claves (será de tipo vehículo)
        self.hijos: list[NodoArbol] = [] #Lista de hijos (será de tipo NodoArbol)



class NodoArbolB:
    #Constructor del nodo del nodo del arbol B
    def __init__(self, hoja: bool=False):
        self.hoja: bool = hoja #Para saber si es página hoja
        self.claves: list[int] = [] #Lista de claves (será de tipo vehículo)
        self.hijos: list[NodoArbolB] = [] #Lista de hijos (será de tipo NodoArbolB)

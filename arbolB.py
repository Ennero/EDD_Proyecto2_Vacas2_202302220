from nodoArbolB import NodoArbolB



class ArbolB:
    #Constructor
    def __init__(self, orden: int): #El orden será 5
        self.root: NodoArbolB = NodoArbolB(True) #Inicializo el arbol con un nodo
        self.orden: int = orden #El orden del arbol

    def insertarClave(self, valor: int):
        root:NodoArbolB = self.root
        
        if len(root.claves) == self.orden - 1:
            pass
        else:
            self.insertarValorNoCompleto(root,valor)

    def insertar(self, valor: int):
        self.insertarValor(root,valor);

    def insertarValorNoCompleto(self, nodo: NodoArbolB, valor: int):
        contador: int =len(raiz.claves)-1

        if (raiz.hoja):
            raiz.claves.append(None)

            while contador>= 0  and valor < raiz.claves[contador]:
                raiz.claves[contador+1] = raiz.claves[contador]
                contador -= 1

            raiz.claves[contador + 1] = valor
        else:
            while contado>= 0 and valor < raiz.claves[contador]:
                contador -= 1

            if len(raiz.hijos[contador].claves) == self.orden-1:
                pass
                
            self.insertarValor(raiz.hijos[contador],valor)
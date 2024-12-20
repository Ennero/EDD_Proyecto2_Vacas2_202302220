import math
from nodoArbol import NodoArbol

class ArbolB:
    #Constructor del arbol
    def __init__(self, orden: int=5): 
        self.raiz: NodoArbol = NodoArbol(True)
        self.orden: int = orden #El número máximo de hijos que puede tener
    
    #Metodo para insertar un valor en el arbol
    def insertarClavecita(self, valor: int):
        raiz: NodoArbol = self.raiz #Creo una copia del nodo raiz
        if len(raiz.claves) == self.orden - 1: #Si el nodo raiz esta lleno
            nodo: NodoArbol = NodoArbol() #Creo un nuevo nodo
            self.raiz = nodo #El nuevo nodo sera la raiz
            nodo.hijos.insert(0, raiz) #El nodo raiz sera el hijo del nuevo nodo
            self.dividirNodo(nodo, 0) #Divido el nodo raiz
            self.insertarValorNoCompleto(nodo, valor) #Inserto el valor en el nodo
        else:
            self.insertarValorNoCompleto(raiz, valor) #Inserto el valor en el nodo sin dividir la raiz
            
    def insertarValorNoCompleto(self, raiz: NodoArbol, valor: int):
        i: int = len(raiz.claves) - 1 

        if raiz.hoja:
            raiz.claves.append(None)
            while i >= 0 and valor < raiz.claves[i]:
                raiz.claves[i + 1] = raiz.claves[i]
                i -= 1
            raiz.claves[i + 1] = valor


        else:
            while i >= 0 and valor < raiz.claves[i]:
                i -= 1
            i += 1
            if len(raiz.hijos[i].claves) == self.orden - 1:

                
                self.dividirNodo(raiz, i)
                if valor > raiz.claves[i]:
                    i += 1
            self.insertarValorNoCompleto(raiz.hijos[i], valor)
            
    def dividirNodo(self, raiz: NodoArbol, pos: int):
        orden: int = self.orden
        hijo: NodoArbol = raiz.hijos[pos] #
        nodo: NodoArbol = NodoArbol(hijo.hoja)

        raiz.hijos.insert(pos + 1, nodo)
        raiz.claves.insert(pos, hijo.claves[(orden - 1) // 2])



        nodo.claves = hijo.claves[(orden - 1) // 2 + 1:]
        hijo.claves = hijo.claves[: (orden - 1) // 2]

        if not hijo.hoja:
            nodo.hijos = hijo.hijos[(orden - 1) // 2 + 1:]
            hijo.hijos = hijo.hijos[: (orden - 1) // 2 + 1]

    def imprimirUsuario(self):
        grafica: str = "digraph G {\nnode [shape=record];\n"
        grafica += self.imprimir(self.raiz,0)
        
        grafica += "\n}"
        return grafica

    def imprimir(self, nodo: NodoArbol, id:int):
        if nodo is None:
            return ""


        grafica: str = f"nodo{id} [label=\""

        i: int = 0

        while i < len(nodo.claves):
            if (i==0):
                grafica += f"<f{i}>"
            grafica+= f"|{nodo.claves[i]}|<f{i+1}>"
            i += 1

        grafica += f"\"];\n\t"


        siguienteId: int = id+1
        i=0
        while i<len(nodo.hijos):
            hijo=nodo.hijos[i]
            if hijo is not None:
                grafica += f"nodo{id}:f{i} -> nodo{siguienteId};\n"
                grafica += self.imprimir(hijo, siguienteId)
                siguienteId += len(hijo.hijos) if hijo.hijos else 1
            i += 1
        return grafica

    def __str__(self):
        return f"{self.raiz}"

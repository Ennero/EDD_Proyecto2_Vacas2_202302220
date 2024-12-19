from nodoArbol import NodoArbol

class ArbolB:
    def __init__(self, orden: int): 
        self.raiz: NodoArbol = NodoArbol(True)
        self.orden: int = orden
    
    def insertarClavecita(self, valor: int):
        raiz: NodoArbol = self.raiz
        if len(raiz.claves) == self.orden - 1:  
            nodo: NodoArbol = NodoArbol(False)
            self.raiz = nodo
            nodo.hijos.insert(0, raiz)
            self.dividirNodo(nodo, 0)
            self.insertarValorNoCompleto(nodo, valor)
        else:
            self.insertarValorNoCompleto(raiz, valor)
            
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
        hijo: NodoArbol = raiz.hijos[pos]
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
        grafica += self.imprimir(self.raiz)
        grafica += "\n}"
        return grafica

    def imprimir(self, nodo: NodoArbol, id: int=0):

        if nodo is None:
            return

        raiz: NodoArbol = nodo
        grafica: str = f"nodo{id} [label=\""

        i: int = 0
        for clave in raiz.claves:
            if (i == len(raiz.claves) - 1):
                grafica += f"<f{i}> |{clave}|"
                break
            grafica += f"<f{i}> |{clave}|"

            i += 1
        grafica += f"];\n\t"

        j: int = 0
        for hijo in raiz.hijos:
            padreId: int = id
            grafica += f"nodo{padreId}:f{j} -> nodo{id + 1};\n\t"
            id += 1
            grafica += self.imprimir(hijo, id)






        return grafica

    def __str__(self):
        return f"{self.raiz}"

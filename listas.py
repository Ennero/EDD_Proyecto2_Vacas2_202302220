
#--------------------------------------------------------------
#AQUÍ SE CREARA LA ----- LISTA SIMPLE------
class nodoListaSimple: #El nodo de la lista simple
    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente:nodoListaSimple = None

    def getValor(self):
        return self.__valor
    def getSiguiente(self):
        return self.__siguiente
    def setValor(self, valor):
        self.__valor = valor
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente


class listaSimple:
    def __init__(self, inicio = None, fin = None, tamano = 0):
        self.__inicio = inicio
        self.__fin = fin
        self.__tamano = tamano
    
    def getInicio(self):
        return self.__inicio
    def getFin(self):
        return self.__fin
    def getTamano(self):
        return self.__tamano
    def setInicio(self, inicio):
        self.__inicio = inicio
    def setFin(self, fin):
        self.__fin = fin
    def setTamano(self, tamano):
        self.__tamano = tamano


    def insertar(self, valor):
        nuevoNodo:nodoListaSimple = nodoListaSimple(valor)
        if self.__tamano==0:
            self.__inicio = nuevoNodo
            self.__fin = nuevoNodo
        else:
            aux:nodoListaSimple = self.__inicio
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()

            aux.setSiguiente(nuevoNodo)
            self.__fin=nuevoNodo
        self.__tamano += 1

    def encontrar(self, pos):
        if pos<0 or pos>=self.__tamano: print("Posición no válida")

        aux:nodoListaSimple = self.__inicio
        for i in range(pos):
            aux = aux.getSiguiente()
        return aux.getValor()

    def eliminar(self, pos):
        if pos<0 or pos>=self.__tamano: print("Posición no válida")

        if pos == 0:
            self.__inicio = self.__inicio.getSiguiente()
            if self.__tamano == 1:
                self.__fin = None
        else:
            aux:nodoListaSimple=self.__inicio
            for i in range(pos-1):
                aux = aux.getSiguiente()
            aux.setSiguiente(aux.getSiguiente().getSiguiente())
            if pos == self.__tamano-1:
                self.__fin = aux
        self.__tamano -= 1





#--------------------------------------------------------------
#AQUI SE CREARA LA ----- LISTA CIRCULAR DOBLEMENTE ENLAZADA------








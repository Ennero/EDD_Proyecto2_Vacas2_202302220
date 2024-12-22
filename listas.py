from clases import Cliente, Vehiculo, Viaje


#--------------------------------------------------------------
#AQUÍ SE CREARA LA ----- LISTA SIMPLE------
class nodoListaSimple: #El nodo de la lista simple
    def __init__(self, valor):
        self.__valor:Viaje = valor
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
class nodoListaCircularDoble: #El nodo de la lista circular doble
    def __init__(self, valor):
        self.__valor:Cliente = valor
        self.__siguiente:nodoListaCircularDoble = None
        self.__anterior:nodoListaCircularDoble = None

    def getValor(self):
        return self.__valor
    def getSiguiente(self):
        return self.__siguiente
    def getAnterior(self):
        return self.__anterior
    def setValor(self, valor:Cliente):
        self.__valor = valor
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def setAnterior(self, anterior):
        self.__anterior = anterior


class listaCircularDoble:
    def __init__(self):
        self.__tamano = 0
        self.__primero:nodoListaCircularDoble = None
        self.__ultimo:nodoListaCircularDoble = None

    def getTamano(self):
        return self.__tamano
    def getPrimero(self):
        return self.__primero
    def getUltimo(self):
        return self.__ultimo
    def setTamano(self, tamano:int):
        self.__tamano = tamano
    def setPrimero(self, primero:nodoListaCircularDoble):
        self.__primero = primero

    def insertar(self, valor:Cliente):
        nuevoNodo:nodoListaCircularDoble=nodoListaCircularDoble(valor)
        if self.__tamano == 0:
            self.__primero = nuevoNodo
            self.__ultimo = nuevoNodo
            nuevoNodo.setSiguiente(nuevoNodo)
            nuevoNodo.setAnterior(nuevoNodo)
        else:
            self.__ultimo.setSiguiente(nuevoNodo)
            nuevoNodo.setAnterior(self.__ultimo)
            nuevoNodo.setSiguiente(self.__primero)
            self.__primero.setAnterior(nuevoNodo)
            self.__ultimo = nuevoNodo #Solo es para actualizar el valor de la lista
        self.__tamano += 1
        self.ordenar() #Ordeno después de arreglar cada cosa

    def encontrar(self, pos:int):
        if pos<0 or pos>=self.__tamano: print("Posición no válida")

        aux:nodoListaCircularDoble = self.__primero
        for i in range(pos):
            aux = aux.getSiguiente()
        return aux.getValor()

    def ordenar(self):#ordenadno de forma descendente
        if (self.__primero==None or self.__ultimo==None): return
        else:
            aux:nodoListaCircularDoble = self.__primero
            while aux.getSiguiente() != self.__primero:
                aux2:nodoListaCircularDoble = aux.getSiguiente()
                while aux2 != self.__primero:
                    if aux.getValor().getDPI() > aux2.getValor().getDPI():
                        otroAux:nodoListaCircularDoble=aux
                        aux.setValor(aux2.getValor())
                        aux2.setValor(otroAux.getValor())
                    aux2 = aux2.getSiguiente()
                aux = aux.getSiguiente()

    #Función para encontrar un cliente en la lista por su dpi
    def encontrarCliente(self, dpi:str):
        aux:nodoListaCircularDoble = self.__primero
        while aux != self.__ultimo:
            if aux.getValor().getDPI() == dpi:
                return aux.getValor()
            
    #Función para eliminar al cliente de la lista
    def eliminarCliente(self, dpi:str):
        aux:nodoListaCircularDoble=self.encontrarCliente(dpi)
        if aux == None: return
        if aux == self.__primero:
            self.__primero = aux.getSiguiente()
            self.__primero.setAnterior(self.__ultimo)
            self.__ultimo.setSiguiente(self.__primero)
        elif aux == self.__ultimo:
            self.__ultimo = aux.getAnterior()
            self.__ultimo.setSiguiente(self.__primero)
            self.__primero.setAnterior(self.__ultimo)
        else:
            aux.getAnterior().setSiguiente(aux.getSiguiente())
            aux.getSiguiente().setAnterior(aux.getAnterior())


#----------------------------------------------------------------
#Area de pruebas de las listas







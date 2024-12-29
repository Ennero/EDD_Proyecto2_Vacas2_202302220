from clases import Cliente, Vehiculo, Viaje
import os
#--------------------------------------------------------------
#AQUÍ SE CREARA LA ----- LISTA SIMPLE------
class nodoListaSimple: #El nodo de la lista simple
    def __init__(self, valor:Viaje):
        self.__valor:Viaje = valor
        self.__siguiente:nodoListaSimple = None

    def getValor(self):
        return self.__valor
    def getSiguiente(self):
        return self.__siguiente
    def setValor(self, valor:Viaje):
        self.__valor = valor
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente


class listaSimple:
    def __init__(self, inicio:nodoListaSimple = None, fin:nodoListaSimple = None, tamano:int = 0):
        self.__inicio:nodoListaSimple = inicio
        self.__fin:nodoListaSimple = fin
        self.__tamano:int = tamano
    
    def getInicio(self):
        return self.__inicio
    def getFin(self):
        return self.__fin
    def getTamano(self):
        return self.__tamano
    def setInicio(self, inicio:nodoListaSimple):
        self.__inicio = inicio
    def setFin(self, fin:nodoListaSimple):
        self.__fin = fin
    def setTamano(self, tamano:int):
        self.__tamano = tamano

    def insertar(self, valor:Viaje):
        nuevoNodo:nodoListaSimple = nodoListaSimple(valor)
        if self.__tamano==0:
            nuevoNodo.getValor().setId(0)
            self.__inicio = nuevoNodo
            self.__fin = nuevoNodo
        else:
            aux:nodoListaSimple = self.__inicio
            id:int = 0
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
                id+=1
            nuevoNodo.getValor().setId(id+1)
            aux.setSiguiente(nuevoNodo)
            self.__fin=nuevoNodo
        self.__tamano += 1

    #Función para encontrar un viaje en la lista por su id (que es la posición)
    def encontrar(self, pos):
        if pos<0 or pos>=self.__tamano:
            print("Posición no válida")
            return

        aux:nodoListaSimple = self.__inicio
        for i in range(pos):
            aux = aux.getSiguiente()
        return aux.getValor()

    #Creo que este no serviría pero por si acaso si sirve xd
    def eliminar(self, pos):
        if pos<0 or pos>=self.__tamano:
            print("Posición no válida")
            return
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


    def crearCopiaOrdenada(self):
        if self.__tamano == 0: return None
        listaCopia:listaSimple = listaSimple()
        aux:nodoListaSimple = self.__inicio

#Aquí coloca las funciones de ordenamiento para los reportes :)
#-----------------------------------------------------------------------------

    def ordenarPorVehiculos(self):
        if self.__tamano <= 1: return
            
        for i in range(self.__tamano):
            actual = self.__inicio
            siguiente = actual.getSiguiente()
            
            for j in range(self.__tamano - i - 1):
                # Si el actual es mayor que el siguiente, intercambiamos los valores
                if actual.getValor().getVehiculo().getViajes() < siguiente.getValor().getVehiculo().getViajes() :
                    # Intercambiamos solo los valores, no los nodos
                    valorTemp = actual.getValor()
                    actual.setValor(siguiente.getValor())
                    siguiente.setValor(valorTemp)
                actual = siguiente
                siguiente = siguiente.getSiguiente()
    
    def ordenarPorClientes(self):
        if self.__tamano <= 1: return

        for i in range(self.__tamano):
            actual = self.__inicio
            siguiente = actual.getSiguiente()
            
            for j in range(self.__tamano -i-1):
                # Si el actual es mayor que el siguiente, intercambiamos los valores
                if actual.getValor().getCliente().getViajes() < siguiente.getValor().getCliente().getViajes():
                    # Intercambiamos solo los valores, no los nodos
                    valorTemp = actual.getValor()
                    actual.setValor(siguiente.getValor())
                    siguiente.setValor(valorTemp)
                actual = siguiente
                siguiente = siguiente.getSiguiente()


    def ordenarPorGanancias(self):
        if self.__tamano <= 1: return

        for i in range(self.__tamano):
            actual = self.__inicio
            siguiente = actual.getSiguiente()
            
            for j in range(self.__tamano -i-1):
                # Si el actual es mayor que el siguiente, intercambiamos los valores
                if (float(actual.getValor().getVehiculo().getPPS()) * float(actual.getValor().getTiempoRuta())) < (float(siguiente.getValor().getVehiculo().getPPS()) * float(siguiente.getValor().getTiempoRuta())):
                    # Intercambiamos solo los valores, no los nodos
                    valorTemp = actual.getValor()
                    actual.setValor(siguiente.getValor())
                    siguiente.setValor(valorTemp)
                actual = siguiente
                siguiente = siguiente.getSiguiente()


    def ordenarPorLargo(self):
        if self.__tamano <=1: return
        
        for i in range(self.__tamano):
            actual = self.__inicio
            siguiente = actual.getSiguiente()
            
            for j in range(self.__tamano-i-1):
                # Si el actual es mayor que el siguiente, intercambiamos los valores
                if actual.getValor().getPasos().tamano < siguiente.getValor().getPasos().tamano:
                    # Intercambiamos solo los valores, no los nodos
                    valorTemp = actual.getValor()
                    actual.setValor(siguiente.getValor())
                    siguiente.setValor(valorTemp)
                actual = siguiente
                siguiente = siguiente.getSiguiente()

#-----------------------------------------------------------------------------


    #Función para generar la estrcutura de la lista simple
    def generarEstructura(self):
        #Si no hay nada no genero nada :)
        if self.__inicio is None or self.__fin is None:
            return
        aux:nodoListaSimple = self.__inicio #Creo un nodo que recorrerá toda la lista
        
        reporte = "digraph ListaBaby {\n"
        reporte += "rankdir=LR;node [shape=record, style=filled, fillcolor=lightsalmon, margin=0.2];\n"
        reporte += "edge [style=solid, color=red];\n"
        reporte += "graph [ranksep=1.5, nodesep=1];\n"
        reporte += "graph [label=\"\", fontsize=20, fontcolor=black];\n"
        
        while aux != None:
            reporte += f"\"{aux.getValor().getId()}\" [label=\"{{"
            # Agregar los atributos que quieras mostrar
            reporte += f"ID: {aux.getValor().getId()}\\l"
            reporte += f"Origen: {aux.getValor().getOrigen()}\\l"
            reporte += f"Destino: {aux.getValor().getDestino()}\\l"
            reporte += f"Fecha y Hora de Inicio: {aux.getValor().getFechaHoraInicio()}\\l"
            reporte += f"DPI del Cliente: {aux.getValor().getCliente().getDPI()}\\l"
            reporte += f"Nombre del Cliente: {aux.getValor().getCliente().getNombre()} {aux.getValor().getCliente().getApellido()}\\l"
            reporte += f"Placa del Vehículo: {aux.getValor().getVehiculo().getPlaca()}\\l"
            reporte += f"Marca del Vehículo: {aux.getValor().getVehiculo().getMarca()}\\l"
            reporte += f"Tiempo de la Ruta: {aux.getValor().getTiempoRuta()}\\l"
            reporte += "}}\"];\n"

            # Conecto los nodos
            if aux.getSiguiente() != None:
                reporte += f"\"{aux.getValor().getId()}\" -> \"{aux.getSiguiente().getValor().getId()}\";\n"
            aux = aux.getSiguiente()  # Continuo con el ciclo

        reporte += "}\n"  # Cierro el grafo

        # Generar el archivo
        with open("EstructuraListaCircularSimple.dot", "w") as archivo:
            archivo.write(reporte)

        # Ejecutar el comando para generar el PDF
        os.system("dot -Tpdf EstructuraListaCircularSimple.dot -o EstructuraListaCircularSimple.pdf && start EstructuraListaCircularSimple.pdf")

    def stringViajes(self)->str:
        aux:nodoListaSimple = self.__inicio
        if aux == None: return "No hay viajes"
        cadena:str = ""
        while aux != self.__fin:
            cadena+="ID: "+str(aux.getValor().getId())+" - "+aux.getValor().getOrigen() + " - " + aux.getValor().getDestino() + " - " + aux.getValor().getFechaHoraInicio() + " - " + aux.getValor().getCliente().getDPI() + " - " + aux.getValor().getVehiculo().getPlaca() + " - " + str(aux.getValor().getTiempoRuta()) + "\n"
            aux = aux.getSiguiente()
        cadena+="ID: "+str(aux.getValor().getId())+" - "+aux.getValor().getOrigen() + " - " + aux.getValor().getDestino() + " - " + aux.getValor().getFechaHoraInicio() + " - " + aux.getValor().getCliente().getDPI() + " - " + aux.getValor().getVehiculo().getPlaca() + " - " + str(aux.getValor().getTiempoRuta()) + "\n"
        print(cadena)
        return cadena



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

    def insertar(self, valor: Cliente):
        nuevoNodo = nodoListaCircularDoble(valor)
        
        # Si la lista está vacía, inicializar con el nuevo nodo
        if self.__tamano == 0:
            self.__primero = nuevoNodo
            self.__ultimo = nuevoNodo
            nuevoNodo.setSiguiente(nuevoNodo)
            nuevoNodo.setAnterior(nuevoNodo)
        else:
            #Si el nuevo valor es menor que el primer nodo, asi insertar al inicio
            if valor.getDPI() < self.__primero.getValor().getDPI():
                nuevoNodo.setSiguiente(self.__primero)
                nuevoNodo.setAnterior(self.__ultimo)
                self.__primero.setAnterior(nuevoNodo)
                self.__ultimo.setSiguiente(nuevoNodo)
                self.__primero = nuevoNodo
            else:
                #Busco la posicion para ordenar
                actual = self.__primero
                while actual.getSiguiente() != self.__primero and actual.getSiguiente().getValor().getDPI() < valor.getDPI():
                    actual = actual.getSiguiente()
                
                #Inserto después del nodo actual	
                nuevoNodo.setSiguiente(actual.getSiguiente())
                nuevoNodo.setAnterior(actual)
                actual.getSiguiente().setAnterior(nuevoNodo)
                actual.setSiguiente(nuevoNodo)
                
                #Si se insertó al final, actualizo el último nodo
                if actual == self.__ultimo:
                    self.__ultimo = nuevoNodo

        # Incrementar el tamaño de la lista
        self.__tamano += 1

    def encontrar(self, pos:int):
        if pos<0 or pos>=self.__tamano: print("Posición no válida")

        aux:nodoListaCircularDoble = self.__primero
        for i in range(pos):
            aux = aux.getSiguiente()
        return aux.getValor()
        

    #Función para encontrar un cliente en la lista por su dpi
    def encontrarCliente(self, dpi:str)->nodoListaCircularDoble:
        if self.__tamano == 0: return None
        aux:nodoListaCircularDoble = self.__primero
        for _ in range(self.__tamano):
            if aux.getValor().getDPI() == dpi:
                return aux
            aux = aux.getSiguiente()
        return None
            
    #Función para eliminar al cliente de la lista
    def eliminarCliente(self, dpi:str):
        if self.__tamano == 0: return
        aux:nodoListaCircularDoble=self.encontrarCliente(dpi)
        if aux == None: return
        if self.__tamano == 1:
            self.__primero = None
            self.__ultimo = None
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
        self.__tamano -= 1

    #Función para imprimir los clientes de la lista
    def stringClientes(self)->str:
        aux:nodoListaCircularDoble = self.__primero
        if aux == None: return "No hay clientes"
        cadena:str = ""
        contador:int = 1
        while aux != self.__ultimo:
            cadena+=str(contador)+". "+aux.getValor().getDPI() +" - "+ aux.getValor().getNombre() + " " + aux.getValor().getApellido() + " - " + aux.getValor().getGenero()+ " - " + aux.getValor().getTelefono() + " - " + aux.getValor().getDireccion() + "\n"
            contador+=1
            aux = aux.getSiguiente()
        cadena+=str(contador)+". "+aux.getValor().getDPI()+" - "+aux.getValor().getNombre()+ " " + aux.getValor().getApellido() + " - " + aux.getValor().getGenero()+ " - " + aux.getValor().getTelefono() + " - " + aux.getValor().getDireccion() + "\n"
        return cadena
    
    def modificarCliente(self, dpi:str, nombre:str, apellido:str, genero:str, telefono:str, direccion:str):
        aux:nodoListaCircularDoble = self.encontrarCliente(dpi)
        if aux == None: return
        aux.getValor().setNombre(nombre)
        aux.getValor().setApellido(apellido)
        aux.getValor().setGenero(genero)
        aux.getValor().setTelefono(telefono)
        aux.getValor().setDireccion(direccion)

    #Función para generar la estrcutura de la lista doble
    def generarEstructura(self):
        #Si no hay nada no genero nada :)
        if self.__primero is None or self.__ultimo is None:
            return
        aux:nodoListaCircularDoble = self.__primero#Creo un nodo que recorrerá toda la lista
        
        reporte = "digraph listita {\n"
        reporte += "rankdir=LR;node [shape=record, style=filled, fillcolor=salmon, margin=0.2];\n"
        reporte += "edge [style=solid, color=red];\n"
        reporte += "graph [ranksep=1.5, nodesep=1];\n"
        reporte += "graph [label=\"\", fontsize=20, fontcolor=black];\n"

        #Recorro la lista
        banderita:bool = True
        
        while True:
            reporte += f"\"{aux.getValor().getDPI()}\" [label=\"{{"
            # Agregar los atributos que quieras mostrar
            reporte += f"DPI: {aux.getValor().getDPI()}\\l"
            reporte += f"Nombres: {aux.getValor().getNombre()}\\l"
            reporte += f"Apellidos: {aux.getValor().getApellido()}\\l"
            reporte += f"Genero: {aux.getValor().getGenero()}\\l"
            reporte += f"Teléfono: {aux.getValor().getTelefono()}\\l"
            reporte += f"Dirección: {aux.getValor().getDireccion()}\\l"
            reporte += "}}\"];\n"

            # Conecto los nodos
            if aux.getSiguiente() != self.__primero.getSiguiente():
                reporte += f"\"{aux.getValor().getDPI()}\" -> \"{aux.getSiguiente().getValor().getDPI()}\"[dir=both];\n"
            elif banderita:
                reporte += f"\"{aux.getValor().getDPI()}\" -> \"{aux.getSiguiente().getValor().getDPI()}\"[dir=both];\n"
            
            banderita = False
            aux = aux.getSiguiente()  # Continuo con el ciclo
            
            if aux == self.__primero:
                break

        reporte += "}\n"  # Cierro el grafo

        # Generar el archivo
        with open("EstructuraListaCircularDoble.dot", "w") as archivo:
            archivo.write(reporte)

        # Ejecutar el comando para generar el PDF
        os.system("dot -Tpdf EstructuraListaCircularDoble.dot -o EstructuraListaCircularDoble.pdf && start EstructuraListaCircularDoble.pdf")

#----------------------------------------------------------------
#Area de pruebas de las listas







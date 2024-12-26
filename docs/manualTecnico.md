# Manual Técnico - Proyecto 2
## Objetivos
### Objetivo General
- Analizar exhaustivamente la arquitectura y la implementación del programa "Llega Rapidito", con un enfoque particular en las estructuras de datos empleadas para su desarrollo, con el fin de documentar su diseño y funcionalidad.
### Objetivos Específicos
- Describir el funcionamiento algorítmico del código fuente del programa.
- Identificar y caracterizar las estructuras de datos fundamentales implementadas en el proyecto, tales como listas enlazadas, árboles y grafos, justificando su elección en función de los requerimientos del programa.

## Alcances del Sistema
El presente informe tiene como objetivo principal proporcionar una documentación completa y rigurosa del programa "Llega Rapidito", centrándose en el diseño y la implementación de sus estructuras de datos. Los alcances específicos de este informe son:
Documentar la arquitectura del programa, describiendo sus componentes principales y sus interacciones.
Explicar detalladamente las estructuras de datos utilizadas, incluyendo su justificación teórica, su implementación y su rendimiento.
Servir como una guía para la replicación o adaptación del programa en futuros proyectos que requieran el uso de estructuras de datos similares.

## Especificaciones técnicas
### Requisitos de Hardware
- Procesador con arquitectura x86
- Memoria RAM de 1GB
- Espacio libre en el disco duro de 2GB
- Pantalla
- Teclado (opcional)
- Mouse (opcional)
### Requisitos de Software 
- Sistema Operativo compatible con Python
- Editor de texto o IDE compatible con Python como VScode
- Compilador de Python
## Lógica y descripción de la solución
Para la creación del programa "Llega Rapidito" se utilizaron varios estructuras a travéz de la programación orientada a objetos y ciertos tipo de datos abstractos los cuales son:
### Clases
#### Cliente
Representa a un cliente con atributos como DPI, nombre, apellido, género, teléfono y dirección. Actúa como el tipo de dato que se almacenará en la lista circular doblemente enlazada.
```python
class Cliente:
    def __init__(self,dpi:str, nombre:str, apellido:str,genero:str,telefono:str,direccion:str):
        self.__dpi=dpi
        self.__nombre = nombre
        self.__apellido=apellido
        self.__genero=genero
        self.__telefono=telefono
        self.__direccion=direccion
#Getters y setters
    def getDPI(self):
        return self.__dpi
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getGenero(self):
        return self.__genero
    
    def getTelefono(self):
        return self.__telefono
    
    def getDireccion(self):
        return self.__direccion
    
    def setDPI(self,dpi:str):
        self.__dpi=dpi

    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setApellido(self,apellido:str):
        self.__apellido=apellido

    def setGenero(self,genero:str):
        self.__genero=genero

    def setTelefono(self,telefono:str):
        self.__telefono=telefono

    def setDireccion(self,direccion:str):
        self.__direccion=direccion
```
#### Vehiculo
Representa un vehículo con atributos como placa, marca, modelo y PPS (precio por el vehiculo)
```python
class Vehiculo:
    def __init__(self, placa:str,marca:str,modelo:str,pps:float):
        self.__placa=placa
        self.__marca=marca
        self.__modelo=modelo
        self.__pps=pps
#Getters y setters
    def getPlaca(self):
        return self.__placa
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getPPS(self):
        return self.__pps
    
    def setPlaca(self,placa:str):
        self.__placa=placa

    def setMarca(self,marca:str):
        self.__marca=marca

    def setModelo(self,modelo:str):
        self.__modelo=modelo

    def setPPS(self,pps:float):
        self.__pps=pps
```
#### Ruta
Representa una ruta con un origen, un destino y un tiempo de ruta.
```python
class Ruta:
    def __init__(self, origen:str, destino:str, tiempoRuta:float):
        self.origen=origen
        self.destino=destino
        self.tiempoRuta=tiempoRuta
    #getters y setters
    def getOrigen(self):
        return self.origen
    
    def getDestino(self):
        return self.destino
    
    def getTiempoRuta(self):
        return self.tiempoRuta
    
    def setOrigen(self,origen:str):
        self.origen=origen

    def setDestino(self,destino:str):
        self.destino=destino

    def setTiempoRuta(self,tiempoRuta:float):
        self.tiempoRuta=tiempoRuta
```
#### Viaje
Representa un viaje con atributos como ID (generado automáticamente), origen, destino, fecha y hora de inicio, cliente, vehículo y ruta.
```python
class Viaje:
    def __init__(self,origen:str,destino:str, fechaHoraInicio:str, cliente:Cliente, vehiculo:Vehiculo, ruta:Ruta):
        self.id=9999 #Este id se generará automáticamente
        self.origen=origen
        self.destino=destino
        self.fechaHoraInicio=fechaHoraInicio
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.ruta=ruta #En realidad debe ser la lista de las rutas cortas que tengo que hacer (es simple)
    #getters y setters
    def getId(self):
        return self.id

    def getOrigen(self):
        return self.origen
    
    def getDestino(self):
        return self.destino
    
    def getFechaHoraInicio(self):
        return self.fechaHoraInicio
    
    def getCliente(self):
        return self.cliente
    
    def getVehiculo(self):
        return self.vehiculo
    
    def getRuta(self):
        return self.ruta
    
    def setId(self,id:int):
        self.id=id
    
    def setOrigen(self,origen:str):
        self.origen=origen

    def setDestino(self,destino:str):
        self.destino=destino

    def setFechaHoraInicio(self,fechaHoraInicio:str):
        self.fechaHoraInicio=fechaHoraInicio

    def setCliente(self,cliente:Cliente):
        self.cliente=cliente

    def setVehiculo(self,vehiculo:Vehiculo):
        self.vehiculo=vehiculo

    def setRuta(self,ruta:Ruta):
        self.ruta=ruta
```
 ### Estructuras de datos de tipo lista
 #### Lista simple
Una lista simple enlazada es una estructura de datos que está compuesta por nodos que contienen los datos y una referencia al siguiente nodo que contendrá los datos del valor posterior.

Para este proyecto se realizó una lista simple para almacenar los datos todo los viajes en las clases de tipo "Viaje".

##### Componentes
- nodoListaSimple: Representa un nodo individual en la lista y sy apuntador al siguienete nodo. Contiene:
  - __valor: El objeto de la clase Viaje, que almacena la información del viaje.
  - __siguiente: Un puntero al siguiente nodo de la lista.
```python
class nodoListaSimple: #El nodo de la lista simple
    def __init__(self, valor):
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
```
- listaSimple: Representa la lista enlazada como tal. Contiene:
  - __inicio: Un puntero al primer nodo de la lista.
  - __fin: Un puntero al último nodo de la lista.
  - __tamano: Un entero que almacena la cantidad de nodos en la lista.

```python
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
```

##### Funcionalidades
- Inserción (insertar): Permite agregar un nuevo Viaje al final de la lista. Asigna un ID único al nuevo viaje, incrementando un contador interno. El ID único será el mismo que tendrá en la posicón dentro de la lista.
```python
    def insertar(self, valor:Viaje):
        nuevoNodo:nodoListaSimple = nodoListaSimple(valor)
        if self.__tamano==0:
            nuevoNodo.getValor().setID(1)
            self.__inicio = nuevoNodo
            self.__fin = nuevoNodo
        else:
            aux:nodoListaSimple = self.__inicio
            id:int = 0
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
                id+=1
            nuevoNodo.getValor().setID(id+1)
            aux.setSiguiente(nuevoNodo)
            self.__fin=nuevoNodo
        self.__tamano += 1
```
- Búsqueda por posición (encontrar): Permite acceder a un Viaje específico en la lista dada su posición (índice). Realiza una búsqueda desde el inicio de la lista.
```python
    def encontrar(self, pos):
        if pos<0 or pos>=self.__tamano:
            print("Posición no válida")
            return

        aux:nodoListaSimple = self.__inicio
        for i in range(pos):
            aux = aux.getSiguiente()
        return aux.getValor()
``` 
- Eliminación por posición (eliminar): Permite eliminar un Viaje de la lista dada su posición. Maneja todos los cases de eliminación.
```python
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
``` 

- Generación de estructura gráfica (generarEstructura): Genera un archivo .dot que describe la estructura de la lista en formato Graphviz. Luego, genera un archivo PDF con la representación gráfica de la lista.
```python
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
            reporte += f"Nombre del Cliente: {aux.getValor().getCliente().getNombre()}\\l"
            reporte += f"Placa del Vehículo: {aux.getValor().getVehiculo().getPlaca()}\\l"
            reporte += f"Modelo del Vehículo: {aux.getValor().getVehiculo().getModelo()}\\l"
            reporte += f"Origen: {aux.getValor().getRuta().getOrigen()}\\l"
            reporte += f"Destino: {aux.getValor().getRuta().getDestino()}\\l"
            reporte += f"Tiempo de la Ruta: {aux.getValor().getRuta().getTiempoRuta()}\\l"
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

``` 
 #### Lista Circular Doblemente Enlazada
Una lista circular doblemente enlazada es una estructura en la que cada nodo tiene un enlace tanto al nodo siguiente como al nodo anterior, formando un círculo. Esto significa que el último nodo apunta al primer nodo y el primer nodo apunta al último nodo, lo que permite que se pueda recorrer la lista en ambas direcciones indefinidamente. 

En este proyecto implementó la lista circular doblmente enlazada para almacenar lo objetos de tipo Cliente, dentro de los cuales se almacena la información de cada uno de los clientes.

##### Componentes

- nodoListaCircularDoble: Representa un nodo en la lista circular doble. Contiene:
  - __valor: Un objeto de la clase Cliente.
  - __siguiente: Un puntero al siguiente nodo.
  - __anterior: Un puntero al nodo anterior.
```python
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
```
- listaCircularDoble: Representa la lista circular doble. Contiene:
  - __tamano: Un entero que almacena el número de nodos.
  - __primero: Un puntero al primer nodo de la lista.
  - __ultimo: Un puntero al último nodo de la lista.

```python
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
```
##### Funcionalidades
- Inserción ordenada por DPI (insertar): Inserta un nuevo Cliente en la lista, manteniendo el orden ascendente según el DPI del cliente.
```python
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
```
- Búsqueda por posición (encontrar): Similar a la manera en la que trabaja la lista simple, busca un cliente por su posición en la lista.
```python
    def encontrar(self, pos:int):
        if pos<0 or pos>=self.__tamano: print("Posición no válida")

        aux:nodoListaCircularDoble = self.__primero
        for i in range(pos):
            aux = aux.getSiguiente()
        return aux.getValor()
```
- Búsqueda por DPI (encontrarCliente): Busca un Cliente específico en la lista basándose en su DPI.
```python
    #Función para encontrar un cliente en la lista por su dpi
    def encontrarCliente(self, dpi:str)->nodoListaCircularDoble:
        if self.__tamano == 0: return None
        aux:nodoListaCircularDoble = self.__primero
        for _ in range(self.__tamano):
            if aux.getValor().getDPI() == dpi:
                return aux
            aux = aux.getSiguiente()
        return None

```
- Eliminación por DPI (eliminarCliente): Elimina un Cliente de la lista buscando por su DPI. Maneja los casos especiales de eliminar el primer, el último y un nodo intermedio.
```python
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
```
- Representación en cadena de texto (stringClientes): Genera una cadena de texto que contiene la información de todos los clientes en la lista, formateada para su visualización.
```python
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
```
- Modificación de cliente (modificarCliente): Permite modificar los atributos de un cliente existente, identificado por su DPI.
```python
    def modificarCliente(self, dpi:str, nombre:str, apellido:str, genero:str, telefono:str, direccion:str):
        aux:nodoListaCircularDoble = self.encontrarCliente(dpi)
        if aux == None: return
        aux.getValor().setNombre(nombre)
        aux.getValor().setApellido(apellido)
        aux.getValor().setGenero(genero)
        aux.getValor().setTelefono(telefono)
        aux.getValor().setDireccion(direccion)
```
- Generación de estructura gráfica (generarEstructura): Similar a la lógica utilizada para la lista simple, genera un archivo .dot y un PDF con la representación gráfica de la lista circular doble, incluyendo los atributos de cada Cliente.
```python
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
```
### Arbol B
Un árbol B es un tipo de árbol de búsqueda balanceado que se utiliza principalmente en sistemas de bases de datos y sistemas de archivos. A diferencia de un árbol binario, donde cada nodo puede tener como máximo dos hijos, un nodo en un árbol B puede tener múltiples hijos.

Para este proyecto, se utilizo un arbol B de grado 5, lo que quiere decir que cada nodo puede tener como máximo 4 hijos y está compuesto por los siguiente elementos:

#### Nodo Arbol
Esta clase representa un nodo dentro del Árbol B. Un nodo en un Árbol B que puede ser una hoja o un nodo interno. 
##### Componentes
- hoja: bool: Un booleano que indica si el nodo es una hoja.
- claves: list[Vehiculo]: Una lista que almacena las claves del nodo. En este caso, las claves son objetos de la clase Vehiculo.
- hijos: list[NodoArbol]: Una lista que almacena punteros a los nodos hijos del nodo actual.
```python
class NodoArbol:
    #Constructor del nodo del arbol B
    def __init__(self, hoja: bool=False):
        self.hoja: bool = hoja #Para saber si es página hoja
        self.claves: list[Vehiculo] = [] #Lista de claves (ya es de tipo vehículo :>)
        self.hijos: list[NodoArbol] = [] #Lista de hijos (será de tipo NodoArbol)
```
#### ArbolB
Aquí se implementa la estructura del Árbol B.
##### Atributos
- orden: int: El orden del árbol B. Define el número máximo de hijos que puede tener un nodo y por lo tanto, el número máximo de claves + 1.
- raiz: NodoArbol: El nodo raíz del árbol.
```python
class ArbolB:
    def __init__(self, orden: int):
        self.orden: int = orden
        self.raiz: NodoArbol = NodoArbol(True)
```
##### Funcionalidades

- insertarValor(self, valor: Vehiculo): Inserta un nuevo Vehiculo en el árbol. Llama a insertarValorNoCompleto para realizar la inserción y maneja el caso especial de que la raíz se llene, lo que requiere dividir la raíz y crear una nueva raíz.
```python
    def insertarValor(self, valor: Vehiculo):
        raiz: NodoArbol = self.raiz

        self.insertarValorNoCompleto(raiz, valor)

        if (len(raiz.claves) > self.orden - 1):
            nodo: NodoArbol = NodoArbol()
            self.raiz = nodo
            nodo.hijos.insert(0, raiz)
            self.dividirNodo(nodo, 0)
```

- insertarValorNoCompleto(self, raiz: NodoArbol, valor: Vehiculo): Realiza la inserción recursiva del valor.

  -   Si el nodo actual (raiz) es una hoja, inserta el valor en la lista de claves, manteniendo el orden ascendente por la placa del vehículo.
  -   Si el nodo actual no es una hoja, busca el hijo apropiado donde insertar el valor y llama recursivamente a insertarValorNoCompleto en ese hijo.
  -   Después de la llamada recursiva, verifica si el hijo se ha llenado (número de claves > orden - 1) y, en ese caso, llama a dividirNodo para dividirlo.
```python
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
```
-  dividirNodo(self, raiz: NodoArbol, posicion: int): Divide un nodo hijo que se ha llenado.
  -   Calcula la posición media de las claves del hijo.
  -   Crea un nuevo nodo.
  -   Mueve la clave media del hijo al nodo padre (raiz).
  -   Mueve las claves mayores que la clave media al nuevo nodo.
  -   Si el hijo no es una hoja, también mueve los hijos correspondientes al nuevo nodo.
```python
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
```
- buscarValor(self, valor: str): Busca un vehículo por su placa en el árbol, llamando a la función recursiva buscarValorNodo.
```python
    def buscarValor(self, valor: str):
        return self.buscarValorNodo(self.raiz, valor)
```
- buscarValorNodo(self, raiz: NodoArbol, valor: str): Realiza la búsqueda recursiva del valor en el árbol.
```python
    def buscarValorNodo(self, raiz: NodoArbol, valor: str):
        if raiz==None:
            return None

        posicion: int = 0
        #Busco la posición entre las claves donde debería de estar el valor
        while posicion < len(raiz.claves) and valor > raiz.claves[posicion].getPlaca():
            posicion += 1
        #Si se encuentra el valor, se retorna
        if posicion < len(raiz.claves) and valor == raiz.claves[posicion].getPlaca():
            return raiz.claves[posicion]
        #Si no se encuentra el valor y es una hoja, se retorna None
        if raiz.hoja:
            return None
        #Se continúa la busqueda en los hijos
        return self.buscarValorNodo(raiz.hijos[posicion], valor)
```
- modificarValor(self, placa: str, marca: str, modelo: str, pps: float): Busca un vehículo por su placa y, si lo encuentra, modifica sus atributos.
```python
    def modificarValor(self, placa:str, marca:str, modelo:str, pps:float):
        vehiculo: Vehiculo = self.buscarValor(placa)
        if vehiculo != None:
            vehiculo.setMarca(marca)
            vehiculo.setModelo(modelo)
            vehiculo.setPPS(pps)
            return
        return
```
- stringVehiculos(self) y stringVehiculosNodo(self, raiz: NodoArbol, contador:list[int]): Genera una cadena de texto con la información de todos los vehículos en el árbol, utilizando un recorrido inorden para mostrar los vehículos ordenados por placa.
```python
    def stringVehiculos(self)->str:
        if self.raiz.claves == []:
            return "No hay vehículos"
        contador:list[int] = [0]
        return self.stringVehiculosNodo(self.raiz, contador)
```
```python
    def stringVehiculosNodo(self, raiz: NodoArbol, contador:list[int])->str:
        if raiz == None:
            return 'No hay vehículos'
        respuesta: str = ''

        #Voy hacia la hoja más a la izquierda
        if not raiz.hoja:
            respuesta += self.stringVehiculosNodo(raiz.hijos[0], contador)

        #Llegando a la hoja, proceso los valores
        for i in range(len(raiz.claves)):
            contador[0] += 1
            respuesta += str(contador[0])+". "+raiz.claves[i].getPlaca()+ " - "+ raiz.claves[i].getMarca() + " - "+ raiz.claves[i].getModelo() + " - "+ str(raiz.claves[i].getPPS()) + '\n'
        
            #Si no es la última clave, proceso el siguiente hijo
            if not raiz.hoja and len(raiz.hijos) > i+1:
                respuesta += self.stringVehiculosNodo(raiz.hijos[i+1], contador)
        return respuesta
```

- crearIdNodo(self): Genera un ID único para cada nodo para la generación del gráfico.
```python
    def crearIdNodo(self):
        #Contador interno
        self._counter += 1
        return f'node{self._counter}'
```


- crearNodo(self, nodo: NodoArbol, nodo_id: str, grafica: Digraph): Crea la representación visual de un nodo en el gráfico utilizando Graphviz.
```python
    def crearNodo(self, nodo: NodoArbol, nodo_id: str, grafica: Digraph):
        claves = '|'.join(str(k.getPlaca()+" - "+k.getMarca() + " - " + k.getModelo() + " - " + k.getPPS()) for k in nodo.claves) #Uno las claves con un |
        #Creo el nodo en el grafo
        grafica.node(nodo_id, claves) 
        
        #Si el nodo tiene hijos, lo recorro recursivamente
        if not nodo.hoja:
            for i, hijo in enumerate(nodo.hijos):
                hijo_id = self.crearIdNodo()
                self.crearNodo(hijo, hijo_id, grafica)
                grafica.edge(nodo_id, hijo_id)
```


- generarEstructura(self, nombre='ReporteArbolB'): Genera la representación gráfica del árbol B en un archivo PDF utilizando Graphviz.
```python
    def generarEstructura(self, nombre='ReporteArbolB'):
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
```
### Lista Adyacente






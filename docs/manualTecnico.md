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
        self.__viajes=0
#Getters y setters
    def getDPI(self):
        return self.__dpi

    def getViajes(self):
        return self.__viajes

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

    def setViajes(self,viajes:int):
        self.__viajes=viajes

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
        self.__viajes=0
#Getters y setters
    def getPlaca(self):
        return self.__placa

    def getViajes(self):
        return self.__viajes
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getPPS(self):
        return self.__pps
    
    def setPlaca(self,placa:str):
        self.__placa=placa

    def setViajes(self,viajes:int):
        self.__viajes=viajes

    def setMarca(self,marca:str):
        self.__marca=marca

    def setModelo(self,modelo:str):
        self.__modelo=modelo

    def setPPS(self,pps:float):
        self.__pps=pps
```
#### Viaje
Representa un viaje con atributos como ID (generado automáticamente), origen, destino, fecha y hora de inicio, cliente, vehículo.
```python
class Viaje:
    def __init__(self,origen:str,destino:str, fechaHoraInicio:str, cliente:Cliente, vehiculo:Vehiculo, ruta:Ruta, pasos:ListaAdyacente.ListaResultado, tiempoRuta):
        self.id=9999 #Este id se generará automáticamente
        self.origen=origen
        self.destino=destino
        self.fechaHoraInicio=fechaHoraInicio
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.pasos: ListaAdyacente.ListaResultado=pasos
        self.tiempoRuta=tiempoRuta
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
Una lista adyacente es una representación de un grafo que organiza los datos en una estructura eficiente para almacenar y manipular la conectividad de los nodos.

En este proyecto se utilizó para almacenar la información de todas las rutas para, posteriormente, utilizar Dijkstra para encontrar el camino más corto

#### NodoListaAdyacente
Representa un nodo en el grafo.

##### Atributos
- origen: str: El nombre o identificador del lugar de origen.
- siguiente: NodoListaAdyacente: Puntero al siguiente nodo en la lista principal de adyacencia (manejada por ListaAdyacente).
- atras: NodoRuta: Puntero al primer nodo de la lista enlazada de rutas que salen desde este nodo de origen.
```python
class NodoListaAdyacente:
    def __init__(self, origen:str):
        self.origen = origen
        self.siguiente:NodoListaAdyacente = None
        self.atras:NodoRuta = None
```
##### Métodos
- buscar(self, destino: str): Busca una ruta específica desde el nodo actual hasta un destino dado.
- insertar(self, destino: str, peso: float): Inserta una nueva ruta desde el nodo actual hasta un destino con un peso. Si la ruta ya existe, actualiza el peso.
```python
    def buscar(self, destino:str):
        aux = self.atras
        while aux:
            if aux.destino == destino:
                return aux
            aux = aux.atras
        return None

    def insertar(self, destino:str, peso:float):
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
```

#### NodoRuta
Representa una arista en el grafo, una ruta entre dos lugares
##### Atributos
- peso: float: El peso de la arista.
- destino: str: El nombre del lugar de destino.
- atras: NodoRuta: Puntero al siguiente nodo NodoRuta en la lista de rutas del mismo origen. (Esta nomenclatura atras es confusa, sería más claro siguiente o vecino)
```python
class NodoRuta:
    def __init__(self, peso:float, destino:str):
        self.peso:float = peso
        self.destino:str = destino
        self.atras:NodoRuta = None
```
#### NodoDistancia
Esta clase almacena información sobre la distancia a un nodo y si ya ha sido visitado.

##### Atributos

- nodo: str: El nombre del nodo.
- distancia: float: La distancia actual conocida desde el nodo origen hasta este nodo.
- visitado: bool: Indica si el nodo ya ha sido visitado.
- siguiente: NodoDistancia: Puntero al siguiente nodo en una lista para gestionar los nodos en el algoritmo de Dijkstra.
- camino: Almacena el camino recorrido hasta llegar a este nodo.

```python
class NodoDistancia:
    def __init__(self, nodo: str):
        self.nodo = nodo
        self.distancia = float('inf')
        self.visitado = False 
        self.siguiente = None
        self.camino = None
```
#### NodoCamino
Representa un nodo en el camino recorrido por el algoritmo de Dijkstra.
##### Atributos
- nodo: str: El nombre del nodo en el camino.
- siguiente: NodoCamino: Puntero al siguiente nodo en el camino.
```python
class NodoCamino:
    def __init__(self, nodo: str):
        self.nodo = nodo
        self.siguiente = None
```
#### ListaResultado
Almacena la secuencia de nodos que forman la ruta más corta.
##### Atributos 
- inicio: Puntero al primer nodo del camino.
- fin: Puntero al último nodo del camino.
- tamano: Tamaño del camino
```python
class ListaResultado:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamano = 0
```
##### Métodos
- agregar(self, nodo: str): Agrega un nodo al final del camino.
- convertir_a_string(self): Convierte el camino a una cadena de texto para su visualización.
```python
    def agregar(self, nodo: str):
        nuevo = NodoCamino(nodo)
        if not self.inicio:
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.fin.siguiente = nuevo
            self.fin = nuevo
        self.tamano += 1
    
    def convertir_a_string(self):
        resultado = ""
        actual = self.inicio
        while actual:
            resultado += actual.nodo
            if actual.siguiente:
                resultado += " -> "
            actual = actual.siguiente
        return resultado
```
#### EstructuraCaminos
Esta clase se usa para gestionar la información de distancias y nodos visitados

##### Métodos
- insertar(self, nodo: str): Inserta un nuevo nodo con distancia infinita y marcado como no visitado.
- copiar_camino(self, caminoOrigen): Copia un camino para reconstruir el camino cuando se encuentra una ruta más corta.
- obtenerMenorDistancia(self): Busca el nodo no visitado con la menor distancia.
- buscar(self, nodo: str): Busca un nodo por su nombre.
```python
    def insertar(self, nodo: str):
        nuevo = NodoDistancia(nodo)
        if not self.inicio:
            self.inicio = nuevo
            return
        aux = self.inicio
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = nuevo

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

    def obtenerMenorDistancia(self):
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
```
#### ListaAdyancente
##### Métodos
- insertarRuta(self, origen: str, destino: str, peso: float): Inserta una ruta en el grafo.
- generarGrafo(self): Genera una representación visual del grafo con graphviz.
- encontrarRutaCorta(self, origen: str, destino: str): Implementa el algoritmo de Dijkstra para encontrar la ruta más corta.
- mostrar_recorrido_paso_a_paso(self, origen: str, destino: str): Muestra el recorrido paso a paso y la distancia acumulada.
- visualizar_recorrido_lista(self, origen: str, destino: str): Genera una visualización del recorrido encontrado por Dijkstra.
```python
def buscar(self, origen:str):
        aux = self.inicio
        while aux:
            if aux.origen == origen:
                return aux
            aux = aux.siguiente
        return None

    def insertarRuta(self, origen:str, destino:str, peso:float):
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
        
        '''aux = self.buscar(destino)
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
                aux.siguiente = nuevo'''

    def generarGrafo(self):
        grafica = graphviz.Graph('Grafo', filename='Rutas', format='png', engine="neato")
        grafica.attr(rankdir='LR')
        grafica.attr(concentrate='true')
        grafica.node_attr.update(color='lightsalmon', style='filled', fontsize='9')
        grafica.edge_attr.update(color='red', style='dotted', fontsize='8')
        grafica.attr('node')
        aux = self.inicio
        while aux:
            grafica.node(aux.origen)
            aux2 = aux.atras
            while aux2:
                grafica.edge(aux.origen, aux2.destino, label=str(aux2.peso))
                aux2 = aux2.atras
            aux = aux.siguiente
        grafica.render()

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
            actual = caminos.obtenerMenorDistancia()
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
            resultado = ListaResultado()
            aux = nodo_final.camino
            while aux:
                resultado.agregar(aux.nodo)
                aux = aux.siguiente
            return resultado, nodo_final.distancia #Retorna el camino y la distancia
        return None, float('inf')

    def mostrar_recorrido_paso_a_paso(self, origen: str, destino: str):
        camino, distancia_total = self.encontrarRutaCorta(origen, destino)
        
        if not camino:
            print(f"No existe ruta entre {origen} y {destino}")
            return
        
        print(f"\nRecorrido paso a paso de {origen} a {destino}:")
        print("-" * 50)
        
        distancia_acumulada = 0
        actual = camino.inicio
        while actual and actual.siguiente:
            siguiente = actual.siguiente
            nodo_actual = self.buscar(actual.nodo)
            peso = nodo_actual.buscar(siguiente.nodo).peso
            distancia_acumulada += peso
            
            print(f"Paso: {actual.nodo} -> {siguiente.nodo}")
            print(f"Distancia del tramo: {peso}")
            print(f"Distancia acumulada: {distancia_acumulada}")
            print("-" * 50)
            actual = actual.siguiente
        
        print(f"\nResumen del recorrido:")
        print(f"Ruta completa: {camino.convertir_a_string()}")
        print(f"Distancia total: {distancia_total}")

    def visualizar_recorrido_lista(self, origen: str, destino: str):
        camino, distancia = self.encontrarRutaCorta(origen, destino)
        if not camino:
            print(f"No existe ruta entre {origen} y {destino}")
            return
        
        grafica = graphviz.Digraph('RecorridoLista', filename='RecorridoLista', format='pdf')
        grafica.attr(rankdir='LR')
        
        
        grafica.attr('node', shape='box', style='filled', color='lightsalmon')
        
        i = 0
        actual = camino.inicio
        prev_node_id = None
        peso=0
        prepeso=0
        #Ciclo para recorrer la lista de nodos y generar los nodos en la gráfica
        while actual:
            nodo_id = f'nodo_{i}'
            
            if actual.siguiente:
                siguiente = actual.siguiente
                nodo_actual = self.buscar(actual.nodo)
                label = f"{actual.nodo}\nDistancia recorrida: {peso}"
                if prepeso!=0:
                    label =f"{actual.nodo}\nDistancia recorrida: {prepeso}+{nodo_actual.buscar(siguiente.nodo).peso}={peso}"
                prepeso=peso
                peso += nodo_actual.buscar(siguiente.nodo).peso
            else:
                label =f"{actual.nodo}\nDistancia recorrida: \n{prepeso} + {nodo_actual.buscar(siguiente.nodo).peso} = {peso}"
            
            grafica.node(nodo_id, label)
            
            if i == 0:
                pass
            else:
                grafica.edge(prev_node_id, nodo_id)
            
            prev_node_id = nodo_id
            actual = actual.siguiente
            i += 1
        
        grafica.render(view=True)
```
### Interfaz Gráfica
#### Importaciones
- tkinter: Interfaz gráfica.
-Submódulos de tkinter: Label, PhotoImage, messagebox, simpledialog, filedialog, Tk, ttk (para la tabla).
- PIL (Pillow): Manejo de imágenes.
- re: Expresiones regulares.
- Módulos personalizados: arbolito (Árbol B), listas (listas enlazadas), clases (clases Cliente, Vehiculo, Viaje), ListaAdyacente (grafo con lista de adyacencia).
- datetime: Manejo de fechas y horas.
```python
import tkinter as tk
from tkinter import Label, PhotoImage, messagebox,simpledialog,filedialog,Tk
from tkinter import ttk
from PIL import Image, ImageTk
import re
from arbolito import ArbolB
from listas import listaCircularDoble, listaSimple,nodoListaCircularDoble,nodoListaSimple
import clases
from ListaAdyacente import ListaAdyacente,NodoListaAdyacente,NodoRuta
from datetime import datetime
```
#### Incialización de variables globales
- vehículos: ArbolB = ArbolB(5): Árbol B para vehículos.
- clientes: listaCircularDoble = listaCircularDoble(): Lista circular doblemente enlazada para clientes.
- viajes: listaSimple = listaSimple(): Lista simplemente enlazada para viajes.
- rutas: ListaAdyacente = ListaAdyacente(): Grafo para rutas.
- entrada1 = None, scroll1 = None, tabla = None: Variables globales para el segundo cuadro de texto, su barra de desplazamiento y la tabla.
- rutaGrafica: str = "C:/banderas/nono.png": Ruta de la imagen del grafo.
```python
#Inicializo las estructuras
vehículos: ArbolB=ArbolB(5)
clientes: listaCircularDoble =listaCircularDoble()
viajes: listaSimple = listaSimple()
rutas: ListaAdyacente=ListaAdyacente()

entrada1=None
scroll1=None
tabla=None

#Declarando mis variables globales
rutaGrafica:str="C:/banderas/nono.png"
```
#### Funciones auxiliares
- acerca_de(): Muestra información del autor.
- limpiar(): Limpia los campos de texto y la tabla.
```python
#Botones inútiles -----------------------------------------------------------------------------------------------------------
def acerca_de(): #Función para mostrar la información del autor (la mia)
    messagebox.showinfo("Acerca de","Nombre: Enner Esaí Mendizabal Castro\nCarné: 202302220\nCurso: Estructura de Datos\nSección: A")

def limpiar():
    entrada.config(state=tk.NORMAL)
    entrada.delete(1.0, tk.END)
    entrada.config(state=tk.DISABLED)

    #Limpio la segunda entrada
    if entrada1!=None:
        entrada1.config(state=tk.NORMAL)
        entrada1.delete(1.0, tk.END)
        entrada1.config(state=tk.DISABLED)
    #Limpio la tabla
    eliminarTablita()
#Fin de botones inútiles-----------------------------------------------------------------------------------------------------
 
```
- regenerarEntrada1(): Recrea el segundo cuadro de texto (entrada1). Debe ser un método de clase.
```python
def regenerarEntrada1():
    global entrada1, scroll1,tabla
    # Segunda entrada con scroll
    eliminarTablita()
    eliminarSegundaEntrada()

    scroll1 = tk.Scrollbar(fram33, orient="vertical")
    scroll1.pack(side="right", fill="y")

    entrada1 = tk.Text(fram33, height=11, width=75, yscrollcommand=scroll1.set)
    entrada1.pack(side="bottom", fill="both", expand=True)
    scroll1.config(command=entrada1.yview)
    entrada1.config(font=("consolas", 10), state=tk.DISABLED)
```
- eliminarTablita(): Elimina la tabla.
- eliminarSegundaEntrada(): Elimina el segundo cuadro de texto y su scrollbar.
```python
def eliminarTablita():
    global tabla
    if tabla is not None:
        for widget in tabla.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.destroy()
        tabla.destroy()
        tabla = None

def eliminarSegundaEntrada():
    global entrada1, scroll1
    if entrada1!=None:
        entrada1.destroy()
        entrada1=None
    if scroll1!=None:
        scroll1.destroy()
        scroll1=None
    
    for widget in fram33.winfo_children():
        if isinstance(widget, ttk.Scrollbar):
            widget.destroy()
```
#### Funciones de carga masiva

- cargarRutas(): Carga rutas desde un archivo, crea el grafo, genera la imagen y la muestra.
```python
def cargarRutas():
    global rutas,rutaGrafica
    info.config(text="Cargando rutas...", foreground="black", font=("Arial", 9, "italic"))
    ruta=filedialog.askopenfilename(title="Cargar Rutas", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if ruta!="":
        try:
            with open(ruta, "r", encoding="utf-8") as archivo: #Abro el archivo
                rutongas=archivo.read() #Leo el archivo y lo paso a string
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no se encontró o no se pudo abrir.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
        #                Origen      Destino       100
        patroRutas = r'\s*(.+)\s*/\s*(.+)\s*/\s*(\d+)\s*' #Patrón para las rutas

        #Ciclo para ir separando las rutas
        rutitas=rutongas.split('%')
        print("Se hizo split------------------------------------")
        for ruta in rutitas:
            datos=re.search(patroRutas, ruta)
            if datos:
                #Ingreso los valores del grupo dentro de variables
                origen=(datos.group(1)).rstrip()
                destino=datos.group(2).rstrip()
                tiempo=float(datos.group(3))
                if origen==None or destino==None or tiempo==None:
                    #Solo es para trabajar con el último
                    print("No se pudo ingresar la ruta") 
                else:
                    rutas.insertarRuta(origen, destino, tiempo)
                    print(origen, destino, tiempo)

        rutas.generarGrafo()
        rutaGrafica="Rutas.png"

        graficaImg=Image.open(rutaGrafica) #Actualizo la gráfica
        redimencionada=graficaImg.resize((680, 500), Image.Resampling.LANCZOS)
        grafiquita=ImageTk.PhotoImage(redimencionada)
        gra.config(image=grafiquita)
        gra.image=grafiquita
        gra.pack(anchor="e")

        #Aquí destruyo el botón para cargar rutas porque ya no lo voy a volver a usar
        botonRutas.destroy()
        
        #Aquí solo confirmo que se hizo bien
        info.config(text="Rutas cargadas correctamente", foreground="green", font=("Arial", 9, "italic"))
        messagebox.showinfo("Carga de rutas", "Rutas cargadas correctamente.")
    else:
        print("No se pudo abrir el archivo")
        messagebox.showerror("Error", "No se pudo abrir el archivo.")
        info.config(text="Error al cargar rutas", foreground="red", font=("Arial", 9, "italic"))
```

- cargaMasivaClientes(): Carga clientes desde un archivo.
- cargaMasivaVehículos(): Carga vehículos desde un archivo.
```python
#Funciones de carga masiva de datos-----------------------------------------------------------------------------------------------------------
#Función para la carga masiva de clientes
def cargaMasivaClientes():
    global clientes
    info.config(text="Cargando clientes...", foreground="black", font=("Arial", 9, "italic"))
    ruta=filedialog.askopenfilename(title="Cargar Clientes", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if ruta!="":
        try:
            with open(ruta, "r", encoding="utf-8") as archivo: #Abro el archivo
                usuarios=archivo.read() #Leo el archivo y lo paso a string

        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no se encontró o no se pudo abrir.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
        #                1234567879012,  Nombre1,    Nombre2       Apellido1   Apellido2      Genero     44456654   2da calle 25-50 zona 1;
        patronUsuario=r'\s*(\d*),\s*([A-Za-z]+\s*[A-Za-z]*),\s*([A-Za-z]+\s*[A-Za-z]*),\s*([A-Za-z]+),\s*(\d*),\s*(.+)'

        #Ciclo para ir separando los clientes
        print(usuarios)
        
        clientesitos=usuarios.split(";")
        print("Se hizo split------------------------------------")
        for cliente in clientesitos:
            print(cliente)
            datos=re.search(patronUsuario, cliente)
            if datos:
                print(f"Usuario: {datos.group(1)} {datos.group(2)} {datos.group(3)} {datos.group(4)} {datos.group(5)} {datos.group(6)}")
                #Instancio al cliente y lo inserto en la lista circular
                clintete:clases.Cliente=clases.Cliente(datos.group(1), datos.group(2), datos.group(3), datos.group(4), datos.group(5), datos.group(6))
                clientes.insertar(clintete)
        info.config(text="Clientes cargados correctamente", foreground="green", font=("Arial", 9, "italic"))
    else:
        print("No se pudo abrir el archivo")
        messagebox.showerror("Error", "No se pudo abrir el archivo.")
        info.config(text="Error al cargar clientes", foreground="red", font=("Arial", 9, "italic"))

#Función para la carga masiva de vehículos
def cargaMasivaVehículos():
    global vehículos
    info.config(text="Cargando vehículos...", foreground="black", font=("Arial", 9, "italic"))
    ruta=filedialog.askopenfilename(title="Cargar Vehículos", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if ruta!="":
        try:
            with open(ruta, "r", encoding="utf-8") as archivo: #Abro el archivo
                vehiculos=archivo.read() #Leo el archivo y lo paso a string

        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no se encontró o no se pudo abrir.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
        #                  651CVD:    Marca:    Modelo:  precio   
        patronVehiculo=r'\s*(.*):\s*([A-Za-z]+):\s*(.+):\s*(.+)'

        #Ciclo para ir separando los clientes
        print(vehiculos)
        
        vehiculitos=vehiculos.split(";")
        print("Se hizo split------------------------------------")
        for vehiculo in vehiculitos:
            #print(vehiculo)
            data=re.search(patronVehiculo, vehiculo)
            if data:
                print(f"Vehiculo: {data.group(1)} {data.group(2)} {data.group(3)} {data.group(4)}")
                #Instancio al cliente y lo inserto en la lista circular
                vehiculete:clases.Vehiculo=clases.Vehiculo(data.group(1), data.group(2), data.group(3), data.group(4))
                vehículos.insertarValor(vehiculete)
        info.config(text="Vehículos cargados correctamente", foreground="green", font=("Arial", 9, "italic"))
    else:
        print("No se pudo abrir el archivo")
        messagebox.showerror("Error", "No se pudo abrir el archivo.")
        info.config(text="Error al cargar vehículos", foreground="red", font=("Arial", 9, "italic"))
#Fin de funciones para carga masiva de datos------------------------------------------------
```
#### Funciones de creación
- crearCliente(): Crea un cliente.
- crearVehículo(): Crea un vehículo.
- crearViaje(): Crea un viaje.
```python
#Funciónes para crear----------------------------------------------------------------
def crearCliente():
    global clientes
    info.config(text="Creando cliente...", foreground="black", font=("Arial", 9, "italic"))
    #Solicito los datos para crear el cliente
    nombres=simpledialog.askstring("Creación de usuario", "Ingrese los NOMBRES del Cliente:",parent=ventana)
    dpi=simpledialog.askstring("Creación de usuario", "Ingrese el DPI del Cliente:",parent=ventana)
    apellidos=simpledialog.askstring("Creación de usuario", "Ingrese los APELLIDOS del Cliente:",parent=ventana)
    genero=simpledialog.askstring("Creación de usuario", "Ingrese el GÉNERO del Cliente:",parent=ventana)
    telefono=simpledialog.askstring("Creación de usuario", "Ingrese el TELÉFONO del Cliente:",parent=ventana)
    direccion=simpledialog.askstring("Creación de usuario", "Ingrese la DIRECCIÓN del Cliente:",parent=ventana)
    
    if nombres==None or dpi==None or apellidos==None or genero==None or telefono==None or direccion==None:
        messagebox.showerror("Error", "No se pudo crear el Cliente.")
        info.config(text="Error al crear el cliente", foreground="red", font=("Arial", 9, "italic"))
        return
    else:
        #Creo el cliente
        donElian:clases.Cliente=clases.Cliente(dpi, nombres, apellidos, genero, telefono, direccion)
        #Lo inserto en la lista circular
        clientes.insertar(donElian)
        info.config(text="Cliente creado correctamente", foreground="green", font=("Arial", 9, "italic"))
    
def crearVehículo():
    global vehículos
    info.config(text="Creando vehículo...", foreground="black", font=("Arial", 9, "italic"))
    #Solicito los datos para crear el vehículo
    placa=simpledialog.askstring("Creación de vehículo", "Ingrese la PLACA del vehículo:",parent=ventana)
    marca=simpledialog.askstring("Creación de vehículo", "Ingrese la MARCA del vehículo:",parent=ventana)
    modelo=simpledialog.askstring("Creación de vehículo", "Ingrese el MODELO del vehículo:",parent=ventana)
    pps=simpledialog.askstring("Creación de vehículo", "Ingrese el PRECIO del vehículo:",parent=ventana)

    if placa==None or marca==None or modelo==None or pps==None:
        messagebox.showerror("Error", "No se pudo crear el vehículo.")
        info.config(text="Error al crear el vehículo", foreground="red", font=("Arial", 9, "italic"))
        return
    else:
        #Creo el vehículo
        carriñoso:clases.Vehiculo=clases.Vehiculo(placa, marca, modelo, pps)
        #Lo inserto en el arbol B
        vehículos.insertarValor(carriñoso)
        info.config(text="Vehículo creado correctamente", foreground="green", font=("Arial", 9, "italic"))
        messagebox.showinfo("Creación de vehículo", "Vehículo creado correctamente.")

def crearViaje():
    global viajes,vehículos,clientes
    info.config(text="Creando viaje...", foreground="black", font=("Arial", 9, "italic"))
    #Muestro los clientes y los vehículos
    mostrarClientes()
    mostrarVehículos()


    #Solicito los datos para crear el viaje
    dpi=simpledialog.askstring("Creación de viaje", "Ingrese el DPI del cliente:",parent=ventana)
    placa=simpledialog.askstring("Creación de viaje", "Ingrese la PLACA del vehículo:",parent=ventana)
    origen=simpledialog.askstring("Creación de viaje", "Ingrese el ORIGEN del viaje:",parent=ventana)
    destino=simpledialog.askstring("Creación de viaje", "Ingrese el DESTINO del viaje:",parent=ventana)


    if dpi==None or placa==None or origen==None or destino==None:
        messagebox.showerror("Error", "No se pudo crear el viaje.")
        info.config(text="Error al crear el viaje", foreground="red", font=("Arial", 9, "italic"))
        return
    else:
        #Creo el viaje

        #Aumento el contador de los viajes de cada auto y de cada cliente
        clientecito=clientes.encontrarCliente(dpi)
        clientecito.getValor().setViajes(clientecito.getValor().getViajes()+1)
        vehiculito=vehículos.buscarValor(placa)
        vehiculito.setViajes(vehiculito.getViajes()+1)

        #Busco la ruta más corta
        pasos,tiempoRuta=rutas.encontrarRutaCorta(origen, destino)
        fechaActual=datetime.now()
        fechaFormateada=fechaActual.strftime("%d/%m/%Y %H:%M")
        
        #Creo el viaje
        viajecito:clases.Viaje=clases.Viaje(origen, destino,fechaFormateada, clientecito.getValor(), vehiculito, pasos, tiempoRuta)
        viajes.insertar(viajecito)

        info.config(text="Viaje creado correctamente", foreground="green", font=("Arial", 9, "italic"))
        messagebox.showinfo("Creación de viaje", "Viaje creado correctamente.")
    #Creo la instancia del viaje
    
#Fin de funciones para crear--------------------------------------------------------------

```
#### Funciones de eliminación
- eliminarCliente(): Elimina un cliente.
- eliminarVehículo(): Elimina un vehículo.
```python
#Funciones para eliminar----------------------------------------------------------------
def eliminarCliente():
    global clientes
    mostrarClientes()
    if clientes.getTamano==0:
        messagebox.showerror("Error", "No hay clientes para eliminar.")
        info.config(text="Error al eliminar el cliente", foreground="red", font=("Arial", 9, "italic"))
        return
    dpi=simpledialog.askstring("Eliminación de cliente", "Ingrese el DPI del cliente a eliminar:",parent=ventana)
    if dpi==None:
        messagebox.showerror("Error", "No se pudo eliminar el cliente.")
        info.config(text="Error al eliminar el cliente", foreground="red", font=("Arial", 9, "italic"))
        return
    else:
        clientes.eliminarCliente(dpi)
        lucas:nodoListaCircularDoble=clientes.encontrarCliente(dpi)
        if lucas==None:
            messagebox.showerror("Error", "No se encontró el cliente.")
            info.config(text="Cliente no encontrado", foreground="red", font=("Arial", 9, "italic"))
            return
        info.config(text="Cliente eliminado correctamente", foreground="green", font=("Arial", 9, "italic"))
        messagebox.showinfo("Eliminación de cliente", "Cliente eliminado correctamente.")

def eliminarVehículo():
    global vehículos
    mostrarVehículos()
    if vehículos.raiz==None:
        messagebox.showerror("Error", "No hay vehículos para eliminar.")
        info.config(text="Error al eliminar el vehículo", foreground="red", font=("Arial", 9, "italic"))
        return
    

#Fin de funciones para eliminar------------------------------------------------------------
```
#### Funciones de Modificación
- modificarCliente(): Modifica un cliente.
- modificarVehículo(): Modifica un vehículo.
```python
#Funciones para modificar----------------------------------------------------------------
def modificarCliente():
    global clientes
    mostrarClientes()
    #Si es que no tiene nada
    if clientes.getTamano==0:
        messagebox.showerror("Error", "No hay clientes para modificar.")
        info.config(text="Error al modificar el cliente", foreground="red", font=("Arial", 9, "italic"))
        return
    #Si sí entonces sigo :)
    dpi=simpledialog.askstring("Modificación de cliente", "Ingrese el DPI del cliente a modificar:")
    if dpi==None:
        messagebox.showerror("Error", "No se pudo modificar el cliente.")
        info.config(text="Error al modificar el cliente", foreground="red", font=("Arial", 9, "italic"))
        return
    else:
        lucas:nodoListaCircularDoble=clientes.encontrarCliente(dpi)
        if lucas==None:
            messagebox.showerror("Error", "No se encontró el cliente.")
            info.config(text="Cliente no encontrado", foreground="red", font=("Arial", 9, "italic"))
            return
        nombres=simpledialog.askstring("Modificación de cliente", "Ingrese los NOMBRES del Cliente:",parent=ventana)
        apellidos=simpledialog.askstring("Modificación de cliente", "Ingrese los APELLIDOS del Cliente:",parent=ventana)
        genero=simpledialog.askstring("Modificación de cliente", "Ingrese el GÉNERO del Cliente:",parent=ventana)
        telefono=simpledialog.askstring("Modificación de cliente", "Ingrese el TELÉFONO del Cliente:",parent=ventana)
        direccion=simpledialog.askstring("Modificación de cliente", "Ingrese la DIRECCIÓN del Cliente:",parent=ventana)
        if nombres==None or apellidos==None or genero==None or telefono==None or direccion==None:
            messagebox.showerror("Error", "No se pudo modificar el Cliente.")
            info.config(text="Error al modificar el cliente", foreground="red", font=("Arial", 9, "italic"))
            return
        else:
            #Modifico el cliente
            clientes.modificarCliente(dpi, nombres, apellidos, genero, telefono, direccion)
            info.config(text="Cliente modificado correctamente", foreground="green", font=("Arial", 9, "italic"))
            messagebox.showinfo("Modificación de cliente", "Cliente modificado correctamente.")

def modificarVehículo():
    global vehículos
    mostrarVehículos()
    if vehículos.raiz==None:
        messagebox.showerror("Error", "No hay vehículos para modificar.")
        info.config(text="Error al modificar el vehículo", foreground="red", font=("Arial", 9, "italic"))
        return
    placa=simpledialog.askstring("Modificación de vehículo", "Ingrese la PLACA del vehículo a modificar:")
    if placa==None:
        messagebox.showerror("Error", "No se pudo modificar el vehículo.")
        info.config(text="Vehículo no encontrado", foreground="red", font=("Arial", 9, "italic"))
        return
    marca=simpledialog.askstring("Modificación de vehículo", "Ingrese la MARCA del vehículo:",parent=ventana)
    modelo=simpledialog.askstring("Modificación de vehículo", "Ingrese el MODELO del vehículo:",parent=ventana)
    pps=simpledialog.askstring("Modificación de vehículo", "Ingrese el PRECIO del vehículo:",parent=ventana)
    if marca==None or modelo==None or pps==None:
        messagebox.showerror("Error", "No se pudo modificar el vehículo.")
        info.config(text="Error al modificar el vehículo", foreground="red", font=("Arial", 9, "italic"))
        return
    else:
        #Modifico el vehículo
        vehículos.modificarValor(placa, marca, modelo, pps)
        info.config(text="Vehículo modificado correctamente", foreground="green", font=("Arial", 9, "italic"))
        messagebox.showinfo("Modificación de vehículo", "Vehículo modificado correctamente.")

#Fin de funciones para modificar------------------------------------------------------------
```
#### Funciones para mostrar Información
- mostrarClientes(): Muestra clientes en entrada.
- mostrarVehículos(): Muestra vehículos en entrada1.
- mostrarViajes(): Muestra viajes en entrada.
```python
#Funciones para mostrar información-------------------------------------------------------
def mostrarClientes():
    global clientes
    info.config(text="Mostrando clientes...", foreground="black", font=("Arial", 9, "italic"))
    mostrar:str=""
    mostrar=clientes.stringClientes()
    entrada.config(state=tk.NORMAL)
    entrada.delete(1.0, tk.END)
    entrada.insert(tk.END, mostrar)
    print(mostrar)
    entrada.config(state=tk.DISABLED)

def mostrarVehículos():
    global vehículos, entrada1, scroll1
    regenerarEntrada1()
    info.config(text="Mostrando vehículos...", foreground="black", font=("Arial", 9, "italic"))
    mostrar:str=""
    mostrar=vehículos.stringVehiculos()
    entrada1.config(state=tk.NORMAL)
    entrada1.delete(1.0, tk.END)
    entrada1.insert(tk.END, mostrar)
    print(mostrar)
    entrada1.config(state=tk.DISABLED)

def mostrarViajes():
    global viajes
    info.config(text="Mostrando viajes...", foreground="black", font=("Arial", 9, "italic"))
    mostrar:str=""

    #Ordeno los viajes por ID por si se desordenaron
    viajes.ordenarPorID()
    #Ante de todo limpio ambos para no confudirme
    limpiar()
    mostrar=viajes.stringViajes()
    entrada.config(state=tk.NORMAL)
    entrada.delete(1.0, tk.END)
    entrada.insert(tk.END, mostrar)
    print(mostrar)
    entrada.config(state=tk.DISABLED)
#Fin de funciones para mostrar información------------------------------------------------
```
- mostrarInfoPorID(): Muestra información detallada de un viaje por su ID.
```python
#Función para mostrar información por id de los viajes
def mostrarInfoPorID():
    global viajes
    mostrarViajes()
    info.config(text="Solicitando id", foreground="black", font=("Arial", 9, "italic"))
    id=simpledialog.askstring("Información de viaje por Id", "Ingrese el ID del viaje:",parent=ventana)
    if id==None:
        messagebox.showerror("Error", "No se pudo mostrar la información del viaje.")
        info.config(text="Error al mostrar la información del viaje", foreground="red", font=("Arial", 9, "italic"))
        return
    else:
        #Busco el viaje
        viaje:clases.Viaje=viajes.encontrar(int(id))
        if viaje==None:
            messagebox.showerror("Error", "No se encontró el viaje.")
            info.config(text="Viaje no encontrado", foreground="red", font=("Arial", 9, "italic"))
            return
        else:
            #Muestro la información del viaje
            messagebox.showinfo("Información de viaje "+str(viaje.getId()), f"ID: {str(viaje.getId())}\nOrigen: {viaje.getOrigen()}\nDestino: {viaje.getDestino()}\nFecha: {viaje.getFechaHoraInicio()}\nCliente: {viaje.getCliente().getNombre()} {viaje.getCliente().getApellido()}\nVehículo: {viaje.getVehiculo().getPlaca()}\nTiempo: {str(viaje.getTiempoRuta())}")
```

#### Funciones para reportes
- actualizarTabla(columnas, valores_func): Actualiza la tabla con datos.
```python
#Generación de tabla :)---------------------------------------------------------------------

def actualizarTabla(columnas, valores_func):
    global tabla, fram33, entrada1, scroll1

    #Primero elimino la tabla y la entrada si es que existen
    eliminarTablita()
    eliminarSegundaEntrada()
    
    #Creo la nueva tabla
    tabla = ttk.Treeview(fram33, columns=columnas, show="headings")
    #tabla.column(col, width=100)

    #nueva scrollbar
    scrollbar = ttk.Scrollbar(fram33, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)

    #Configuro cabeceras
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=88)
    
    #Inserto los valores
    aux = viajes.getInicio()
    contador = 0
    auxi = None
    prevalores=None
    valores=None
    while aux and contador < 5:
        if auxi == aux:
            contador -= 1
        else:
            valores = valores_func(aux)
            if valores != prevalores:
                tabla.insert("", tk.END, values=valores)
            else:
                contador -= 1
        auxi = aux
        aux = aux.getSiguiente()
        prevalores = valores
        contador += 1

    
    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
```
- topVehiculos(): Reporte de vehículos con más viajes.
- topClientes(): Reporte de clientes con más viajes.
- topGanancias(): Reporte de viajes por ganancias.
- topViajesLargos(): Reporte de viajes más largos.
```python
def topVehiculos():
    global viajes
    viajes.ordenarPorVehiculos()
    
    columnas = ("Viajes", "Placa", "Marca", "Modelo", "Precio")
    def obtener_valores(aux):
        vehiculo = aux.getValor().getVehiculo()
        return (str(vehiculo.getViajes()), vehiculo.getPlaca(), 
                vehiculo.getMarca(), vehiculo.getModelo(), vehiculo.getPPS())
    
    actualizarTabla(columnas, obtener_valores)

def topClientes():
    global viajes
    viajes.ordenarPorClientes()
    
    columnas = ("Viajes", "DPI", "nombreCliente", "Genero")
    def obtener_valores(aux):
        cliente = aux.getValor().getCliente()




        return (cliente.getViajes(), cliente.getDPI(),
                f"{cliente.getNombre()} {cliente.getApellido()}", 
                cliente.getGenero())
    
    actualizarTabla(columnas, obtener_valores)

def topGanancias():
    global viajes
    viajes.ordenarPorGanancias()
    
    columnas = ("Ganancias","Precio Vehiculo", "tiempo", "id", "origen", "destino", "vehículo")
    def obtener_valores(aux):
        valor = aux.getValor()
        return (str(float(valor.getTiempoRuta()) * float(valor.getVehiculo().getPPS())),str(valor.getVehiculo().getPPS()),
                valor.getTiempoRuta(),valor.getId(), valor.getOrigen(), valor.getDestino(), 
                valor.getVehiculo().getPlaca())
    
    actualizarTabla(columnas, obtener_valores)

def topViajesLargos():
    global viajes
    viajes.ordenarPorLargo()
    
    columnas = ("Destinos", "id", "origen", "destino", "tiempo", "cliente", "vehículo")
    def obtener_valores(aux):
        valor = aux.getValor()
        return (str(valor.getPasos().tamano), valor.getId(), 
                valor.getOrigen(), valor.getDestino(), valor.getTiempoRuta(),
                valor.getCliente().getNombre(), valor.getVehiculo().getPlaca())
    
    actualizarTabla(columnas, obtener_valores)
#Fin de funcinoes para reportes----------------------------------------------------------------
```
- rutaDeUnViaje(): Visualiza la ruta de un viaje específico.
```python
def rutaDeUnViaje():
    global viajes
    info.config(text="Mostrando ruta de un viaje...", foreground="black", font=("Arial", 9, "italic"))
    mostrarViajes()
    #Solicito el id del viaje
    id=simpledialog.askstring("Ruta de un viaje", "Ingrese el ID del viaje:",parent=ventana)
    if id==None:
        messagebox.showerror("Error", "No se pudo mostrar la ruta del viaje.")
        info.config(text="Error al mostrar la ruta del viaje", foreground="red", font=("Arial", 9, "italic"))
        return
    else:
        #Busco el viaje
        viaje:clases.Viaje=viajes.encontrar(int(id))
        if viaje==None:
            messagebox.showerror("Error", "No se encontró el viaje.")
            info.config(text="Viaje no encontrado", foreground="red", font=("Arial", 9, "italic"))
            return
        else:
            #Muestro la ruta del viaje
            origen=viaje.origen
            destino=viaje.destino
            rutas.visualizar_recorrido_lista(origen, destino)
            info.config(text="Ruta del viaje mostrada correctamente", foreground="green", font=("Arial", 9, "italic"))
```

#### Funciones para mostrar estructuras de clientes
- estructuraClientes(): Genera gráfica de la estructura de clientes.
- estructuraVehículos(): Genera gráfica de la - estructura de vehículos.
- estructuraViajes(): Genera gráfica de la estructura de viajes.
```python
#Funciones para mostrar estructura de datos------------------------------------------------
def estructuraClientes():
    global clientes
    info.config(text="Mostrando estructura de datos de clientes...", foreground="black", font=("Arial", 9, "italic"))
    clientes.generarEstructura()

def estructuraVehículos():
    global vehículos
    info.config(text="Mostrando estructura de datos de vehículos...", foreground="black", font=("Arial", 9, "italic"))
    vehículos.generarEstructura()

def estructuraViajes():
    global viajes
    info.config(text="Mostrando estructura de datos de viajes...", foreground="black", font=("Arial", 9, "italic"))
    viajes.generarEstructura()

#Fin de funciones para mostrar estructura de datos------------------------------------------
```
#### Interfaz gráfica con tkinter
La interfaz gráfica se creó con tkinet y se colocó todo dentro de una ventana principal llamada *ventana*.
##### Frames
Se usaron frames para organizar de mejor manera el contenido dentro de la ventana
- frame10: Título principal.
- frame11: Contenedor inferior para los menús de Clientes, Vehículos, Viajes y Reportes.
- frame1: Visualización del grafo de rutas (lado izquierdo).
- frame2: Áreas de texto y tabla (lado derecho).
- frame3, frame4, frame5, frame6: Contenedores para los botones de Clientes, Vehículos, Viajes y Reportes, respectivamente.
##### Widgets
En la ventana se colcoaron los siguientes widgets:
- Label: Títulos, mensajes, imagen del grafo.
- Button: Para las acciones.
- Text: Para mostrar información.
- Scrollbar: Para los cuadros de texto.
- Treeview: Para los reportes en forma de tabla.

Esto es todo por parte del programa, alguna lógica, funcionalidad o estética de este podría cambiar en la versión final, pero lo descrito en este manual es la escencia y la base toda la aplicación.






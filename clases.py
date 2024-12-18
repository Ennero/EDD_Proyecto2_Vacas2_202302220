
#Tengo pensado colocar aquí todas las clases que se necesiten para el proyecto que tendrán carga masiva


#Estos se almacenarán dentro de una lista circular doblmente enlazada que se auto-ordenará por el DPI
class Cliente:
    def __init__(self,dpi:int, nombre:str, apellido:str,genero:str,telefono:int,direccion:str):
        self.dpi=dpi
        self.nombre = nombre
        self.apellido=apellido
        self.genero=genero
        self.telefono=telefono
        self.direccion=direccion

        
#Estos se guardarán dentro de un arbol B de orden 5 usando como id la placa del vehículo
class Vehiculo:
    def __init__(self, placa:str,marca:str,modelo:str,pps:float):
        self.placa=placa
        self.marca=marca
        self.modelo=modelo
        self.pps=pps



#se guardará en un grafo
class Ruta:
    def __init__(self, origen:str, destino:str, tiempoRuta:float):
        self.origen=origen
        self.destino=destino
        self.tiempoRuta=tiempoRuta





#va a estar almacenado en una lista circular simple
class Viaje:
    def __init__(self, origen:str,destino:str, fechaHoraInicio:str, cliente:Cliente, vehiculo:Vehiculo, ruta:Ruta):
        self.origen=origen
        self.destino=destino
        self.fechaHoraInicio=fechaHoraInicio
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.ruta=ruta #En realidad debe ser la lista de las rutas cortas que tengo que hacer (es simple)



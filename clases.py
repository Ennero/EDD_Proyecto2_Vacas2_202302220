import ListaAdyacente

#Tengo pensado colocar aquí todas las clases que se necesiten para el proyecto que tendrán carga masiva------------------------------------


#Estos se almacenarán dentro de una lista circular doblmente enlazada que se auto-ordenará por el DPI
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
#------------------------------------------------------------------------------------------

        
#Estos se guardarán dentro de un arbol B de orden 5 usando como id la placa del vehículo
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
#------------------------------------------------------------------------------------------

#va a estar almacenado en una lista circular simple
class Viaje:
    def __init__(self,origen:str,destino:str, fechaHoraInicio:str, cliente:Cliente, vehiculo:Vehiculo, pasos:ListaAdyacente.ListaResultado, tiempoRuta):
        self.id=9999 #Este id se generará automáticamente
        self.origen=origen
        self.destino=destino
        self.fechaHoraInicio=fechaHoraInicio
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.pasos: ListaAdyacente.ListaResultado=pasos
        self.tiempoRuta=tiempoRuta
        #self.ruta=ruta #En realidad debe ser la lista de las rutas cortas que tengo que hacer (es simple)
    #getters y setters
    def getPasos(self):
        return self.pasos
    
    def setPasos(self,pasos):
        self.pasos=pasos

    def getTiempoRuta(self):
        return self.tiempoRuta
    
    def setTiempoRuta(self,tiempoRuta):
        self.tiempoRuta=tiempoRuta

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
    
    def getTiempoRuta(self):
        return self.tiempoRuta
    
    def setTiempoRuta(self,tiempoRuta:float):
        self.tiempoRuta=tiempoRuta
    
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

    

    '''def setRuta(self,ruta:Ruta):
        self.ruta=ruta'''
#------------------------------------------------------------------------------------------


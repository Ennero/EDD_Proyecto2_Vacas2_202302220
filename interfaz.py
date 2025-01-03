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
    clientelo=clientes.encontrarCliente(dpi)
    if clientelo==None:
        messagebox.showerror("Error", "No se encontró el cliente.")
        info.config(text="Cliente no encontrado", foreground="red", font=("Arial", 9, "italic"))
        return
    placa=simpledialog.askstring("Creación de viaje", "Ingrese la PLACA del vehículo:",parent=ventana)

    plaquela=vehículos.buscarValor(placa)
    if plaquela==None:
        messagebox.showerror("Error", "No se encontró el vehículo.")
        info.config(text="Vehículo no encontrado", foreground="red", font=("Arial", 9, "italic"))
        return
    
    #Por fe se ponen bien los viajes xd
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

#Funciones para reportes----------------------------------------------------------------

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
        tabla.column(col, width=82)
    
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

#----------------------------------------------------------------------------------
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

#Fin de generación de tabla------------------------------------------------------------------
    
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


#INTEFAZ GRÁFICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#----------------------------------------------------------------------------

#Creo la ventana principal
ventana = tk.Tk()
ventana.title("Llega Rapidito")
ventana.geometry("1280x800")


# Creación de los frames para la interfaz
frame10=tk.Frame(ventana)
frame10.pack(side=tk.TOP)
frame11=tk.Frame(ventana)
frame11.pack(side=tk.BOTTOM)
frame1 = tk.Frame(ventana)
frame1.pack(side=tk.LEFT) #Lado izquierdo
frame1.config(border=2, relief="groove", borderwidth=5)
frame2 = tk.Frame(ventana)
frame2.pack(side=tk.RIGHT) #Lado derecho
frame2.config(border=2, relief="groove",borderwidth=5)


#Estos frames son para organizar los:
frame5= tk.Frame(frame11)#Viajes
frame5.config(border=2, relief="groove", borderwidth=5)
frame5.pack(side=tk.RIGHT)
frame3= tk.Frame(frame11)#clientes
frame3.config(border=2, relief="groove", borderwidth=5)
frame3.pack(side=tk.RIGHT)
frame4= tk.Frame(frame11)#Vehículos
frame4.config(border=2, relief="groove", borderwidth=5)
frame4.pack(side=tk.RIGHT)
frame6= tk.Frame(frame11)#Reportes
frame6.config(border=2, relief="groove", borderwidth=5)
frame6.pack(side=tk.RIGHT)

#ARRIBA---------------------------------------------------------------------------------------------------------------------------
#Título global de la ventana
titulo=tk.Label(frame10, text="LLEGA RAPIDITO")
titulo.pack()
titulo.config(foreground="black", font=("Arial", 20, "bold"))
#FIN DE LA PARTE DE ARRIBA--------------------------------------------------------------------------------------------------------------------------

#IZQUIERDA---------------------------------------------------------------------------------------------------------------------------
#Título de la sección izquierda de la ventana 
edittxt=tk.Label(frame1, text="RUTAS")
edittxt.pack()
edittxt.config(foreground="black", font=("Arial", 14, "bold"))

#Imagen de la grafica
#Le coloco un path a la grafica
imagen_original = Image.open(rutaGrafica)
imagen_redimensionada = imagen_original.resize((550, 400), Image.Resampling.LANCZOS)  # Redimensionar a 600x400
graficaImg = ImageTk.PhotoImage(imagen_redimensionada)

# Mostrar la imagen en un Label
gra = Label(frame1, image=graficaImg)
gra.pack(anchor="e")



#Creo el botón para enviar la información
frameIngresoRutas = tk.Frame(frame1)
frameIngresoRutas.pack(anchor=tk.CENTER)
botonRutas=tk.Button(frameIngresoRutas, text="Cargar Rutas",height="1", width="10", command=cargarRutas)
botonRutas.pack()
botonRutas.config(background="white", foreground="blue", font=("Arial", 14, "bold"))
#FIN DE LA PARTE IZQUIERDA--------------------------------------------------------------------------------------------------------------------------


#DERECHA---------------------------------------------------------------------------------------------------------------------------
#Creo el editor de texto para los clientes

#Creo otro frame para organizar las entradas
fram32 = tk.Frame(frame2)
fram32.pack(side="top")
fram32.config(border=2, relief="groove", borderwidth=5)

fram33 = tk.Frame(frame2)
fram33.pack(side="bottom")
fram33.config(border=2, relief="groove", borderwidth=5)


info = tk.Label(frame2, text=" ")  # Aquí se mostrará la información de los clientes, vehículos y viajes
info.pack(side="bottom")
info.config(foreground="red", font=("Arial", 9, "italic"))

# Primera entrada con scroll
scroll = tk.Scrollbar(fram32, orient="vertical")
scroll.pack(side="right", fill="y")

entrada = tk.Text(fram32, height=11, width=75, yscrollcommand=scroll.set)
entrada.pack(side="bottom", fill="both", expand=True)
scroll.config(command=entrada.yview)
entrada.config(font=("consolas", 10), state=tk.DISABLED)

# Segunda entrada con scroll
scroll1 = tk.Scrollbar(fram33, orient="vertical")
scroll1.pack(side="right", fill="y")

entrada1 = tk.Text(fram33, height=11, width=75, yscrollcommand=scroll1.set)
entrada1.pack(side="bottom", fill="both", expand=True)
scroll1.config(command=entrada1.yview)
entrada1.config(font=("consolas", 10), state=tk.DISABLED)

#**************************************************************
tabla= ttk.Treeview(fram33)
#**************************************************************




#FIN DE LA PARTE DERECHA--------------------------------------------------------------------------------------------------------------------------




#ABAJO--------------------------------------------------------------------------------------------------------------------------
#Sección de botones para las operaciones--------------------------------------------------------------------------------------------------------------------------
#Menu para los CLIENTES---------------------------------------------------------------------------------------------------------------------------
contenedorClientes=tk.Frame(frame3)
contenedorClientes.pack(ipady=5,ipadx=5, padx=5, pady=5)
tituloClientes = tk.Label(contenedorClientes, text="CLIENTES", font=("Arial", 15, "bold"))
tituloClientes.pack(side="top")

#frames organizadores
frameizquierdo2=tk.Frame(frame3)
frameizquierdo2.pack(side="left")
framederecho2=tk.Frame(frame3)
framederecho2.pack(side="right")

#Creación del botón para Crear
nuevo = tk.Button(frameizquierdo2, text="Crear", height="1", width="11", command=crearCliente)
nuevo.pack()
nuevo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Eliminar
abrir = tk.Button(frameizquierdo2, text="Eliminar", height="1", width="11", command=eliminarCliente)
abrir.pack()
abrir.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Información
guardo = tk.Button(framederecho2, text="Mostrar Información", height="1", width="22", command=mostrarClientes)
guardo.pack()
guardo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para modificar
guardoComo = tk.Button(frameizquierdo2, text="Modificar", height="1", width="11", command=modificarCliente)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Estructura de Datos
guardoComo = tk.Button(framederecho2, text="Mostrar Estructura de Datos", height="1", width="22", command=estructuraClientes)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Menu para los VEHÍCULOS---------------------------------------------------------------------------------------------------------------------------
contenedorVehiculos=tk.Frame(frame4)
contenedorVehiculos.pack(ipady=5,ipadx=5, padx=5, pady=5)
tituloVehiculo = tk.Label(contenedorVehiculos, text="VEHÍCULOS", font=("Arial", 15, "bold"))
tituloVehiculo.pack(side="top")

#frames organizadores
frameizquierdo1=tk.Frame(frame4)
frameizquierdo1.pack(side="left")
framederecho1=tk.Frame(frame4)
framederecho1.pack(side="right")

#Creación del botón para Crear
nuevo = tk.Button(frameizquierdo1, text="Crear", height="1", width="11", command=crearVehículo)
nuevo.pack()
nuevo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Eliminar
abrir = tk.Button(frameizquierdo1, text="Eliminar", height="1", width="11", command=eliminarVehículo)
abrir.pack()
abrir.config(background="white", foreground="black", font=("Arial", 10, "bold"),state=tk.DISABLED) #Desactivado por ahora

#Creación del botón para Mostrar Información
guardo = tk.Button(framederecho1, text="Mostrar Información", height="1", width="22", command=mostrarVehículos)
guardo.pack()
guardo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para modificar
guardoComo = tk.Button(frameizquierdo1, text="Modificar", height="1", width="11", command=modificarVehículo)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Estructura de Datos
guardoComo = tk.Button(framederecho1, text="Mostrar Estructura de Datos", height="1", width="22", command=estructuraVehículos)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))


#Menu para los VIAJES---------------------------------------------------------------------------------------------------------------------------
contenedorViajes=tk.Frame(frame5)
contenedorViajes.pack(ipady=5,ipadx=5, padx=5, pady=5)
tituloViajes = tk.Label(contenedorViajes, text="VIAJES", font=("Arial", 15, "bold"))
tituloViajes.pack(side="top")

#Creación del botón para Crear
nuevo = tk.Button(contenedorViajes, text="Crear", height="1", width="22", command=crearViaje)
nuevo.pack()
nuevo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para mostrar información
mostrarInformacion=tk.Button(contenedorViajes, text="Mostrar Información", height="1", width="22", command=mostrarViajes)
mostrarInformacion.pack()
mostrarInformacion.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Estructura de Datos
guardoComo = tk.Button(contenedorViajes, text="Mostrar Estructura de Datos", height="1", width="22", command=estructuraViajes)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación de botón para mostrar información por id
mostrarInfoIndividual=tk.Button(contenedorViajes, text="Mostrar Información por ID", height="1", width="22", command=mostrarInfoPorID)
mostrarInfoIndividual.pack()
mostrarInfoIndividual.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Menu para REPORTES---------------------------------------------------------------------------------------------------------------------------
contenedorReportes=tk.Frame(frame6)
contenedorReportes.pack(ipady=5,ipadx=5, padx=5, pady=5)
tituloReportes = tk.Label(contenedorReportes, text="REPORTES", font=("Arial", 15, "bold"))
tituloReportes.pack(side="top")

#Creación de los botones de los reportes
#TopViajes en destino
topViajes = tk.Button(contenedorReportes, text="Top 5 Viajes Largos", height="1", width="22", command=topViajesLargos)
topViajes.pack()
topViajes.config(background="white", foreground="black", font=("Arial", 10, "bold"))
#TopGanacias en tiempo
topoGanancias = tk.Button(contenedorReportes, text="Top 5 Ganancias", height="1", width="22", command=topGanancias)
topoGanancias.pack()
topoGanancias.config(background="white", foreground="black", font=("Arial", 10, "bold"))
#TopClientes
topoClientes = tk.Button(contenedorReportes, text="Top 5 Clientes", height="1", width="22", command=topClientes)
topoClientes.pack()
topoClientes.config(background="white", foreground="black", font=("Arial", 10, "bold"))
#TopVehículos
topoVehiculos = tk.Button(contenedorReportes, text="Top 5 Vehículos", height="1", width="22", command=topVehiculos)
topoVehiculos.pack()
topoVehiculos.config(background="white", foreground="black", font=("Arial", 10, "bold"))
#Ruta de un viaje específico
viajeEspecifico = tk.Button(contenedorReportes, text="Ruta de un Viaje", height="1", width="22", command=rutaDeUnViaje)
viajeEspecifico.pack()
viajeEspecifico.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#----------------------------------------------------------------------------
#FIN DE LA PARTE DE ABAJO--------------------------------------------------------------------------------------------------------------------------

#Creo la barra
barra=tk.Menu(ventana)
carga=tk.Menu(barra, tearoff=0)
carga.add_command(label="Cargar Clientes", command=cargaMasivaClientes)
carga.add_command(label="Cargar Vehículos", command=cargaMasivaVehículos)


# Agregar acerca de y salir
barra.add_cascade(label="Carga Masiva", menu=carga)
barra.add_command(label="Acerca de", command=acerca_de)
barra.add_command(label="Limpiar", command=limpiar)
barra.add_command(label="Salir", command=ventana.quit)

# Asignar la barra de menús a la ventana principal
ventana.config(menu=barra)
#----------------------------------------------------------------------------

#Ejecuta la ventana
ventana.mainloop()
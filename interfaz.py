import tkinter as tk
from tkinter import messagebox,simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
import re
from arbolito import ArbolB
from listas import listaCircularDoble, listaSimple
import clases


#Inicializo las estructuras
vehículos: ArbolB=ArbolB(5)
clientes: listaCircularDoble =listaCircularDoble()
viajes: listaSimple = listaSimple()



#Declarando mis variables globales
rutaGrafica:str="C:/banderas/nono.png"
usuarios:str=""

def acerca_de(): #Función para mostrar la información del autor (la mia)
    messagebox.showinfo("Acerca de","Nombre: Enner Esaí Mendizabal Castro\nCarné: 202302220\nCurso: Estructura de Datos\nSección: A")



def limpiar():
    pass

    


def cargarRutas():
    pass

#Funciones de carga masiva de datos-----------------------------------------------------------------------------------------------------------
#Función para la carga masiva de clientes
def cargaMasivaClientes():
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
        patronUsuario=r'\s*(\d{12}),\s*([A-Za-z]+\s*[A-Za-z]*),\s*([A-Za-z]+\s*[A-Za-z]*),\s*([A-Za-z]+),\s*(\d*),\s*(.+)'

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
    else:
        print("No se pudo abrir el archivo")
        messagebox.showerror("Error", "No se pudo abrir el archivo.")

#Función para la carga masiva de vehículos
def cargaMasivaVehículos():
    ruta=filedialog.askopenfilename(title="Cargar Vehículos", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if ruta!="":
        try:
            with open(ruta, "r", encoding="utf-8") as archivo: #Abro el archivo
                vehiculos=archivo.read() #Leo el archivo y lo paso a string

        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no se encontró o no se pudo abrir.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
        #                   651CVD:      Marca:       Modelo:    precio   
        patronVehiculo=r'\s*(.{6}):\s*([A-Za-z]+):\s*(.+):\s*(\d+)'

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
    else:
        print("No se pudo abrir el archivo")
        messagebox.showerror("Error", "No se pudo abrir el archivo.")
#Fin de funciones para carga masiva de datos------------------------------------------------

#Funciónes para crear----------------------------------------------------------------
def crearCliente():
    info.config(text="Creando cliente...", foreground="black", font=("Arial", 9, "italic"))
    #Solicito los datos para crear el cliente
    nombres=simpledialog.askstring("Creación de usuario", "Ingrese los NOMBRES del Cliente:")
    dpi=simpledialog.askstring("Creación de usuario", "Ingrese el DPI del Cliente:")
    apellidos=simpledialog.askstring("Creación de usuario", "Ingrese los APELLIDOS del Cliente:")
    genero=simpledialog.askstring("Creación de usuario", "Ingrese el GÉNERO del Cliente:")
    telefono=simpledialog.askstring("Creación de usuario", "Ingrese el TELÉFONO del Cliente:")
    direccion=simpledialog.askstring("Creación de usuario", "Ingrese la DIRECCIÓN del Cliente:")

    #Creo el cliente
    donElian:clases.Cliente=clases.Cliente(dpi, nombres, apellidos, genero, telefono, direccion)
    #Lo inserto en la lista circular
    clientes.insertar(donElian)

def crearVehículo():
    info.config(text="Creando vehículo...", foreground="black", font=("Arial", 9, "italic"))
    #Solicito los datos para crear el vehículo
    placa=simpledialog.askstring("Creación de vehículo", "Ingrese la PLACA del vehículo:")
    marca=simpledialog.askstring("Creación de vehículo", "Ingrese la MARCA del vehículo:")
    modelo=simpledialog.askstring("Creación de vehículo", "Ingrese el MODELO del vehículo:")
    pps=simpledialog.askstring("Creación de vehículo", "Ingrese el PRECIO POR SEGUNDO del vehículo:")

    #Creo el vehículo
    carriñoso:clases.Vehiculo=clases.Vehiculo(placa, marca, modelo, pps)
    #Lo inserto en el arbol B
    vehículos.insertarValor(carriñoso)

def crearViaje():
    pass

#Fin de funciones para crear--------------------------------------------------------------

#Funciones para eliminar----------------------------------------------------------------
def eliminarCliente():
    
    pass

def eliminarVehículo():
    pass

#Fin de funciones para eliminar------------------------------------------------------------

#Funciones para modificar----------------------------------------------------------------
def modificarCliente():
    pass

def modificarVehículo():
    pass

#Fin de funciones para modificar------------------------------------------------------------


#Funciones para mostrar información-------------------------------------------------------
def mostrarClientes():
    pass

def mostrarVehículos():
    pass

#Fin de funciones para mostrar información------------------------------------------------

#Funciones para mostrar estructura de datos------------------------------------------------
def estructuraClientes():
    pass

def estructuraVehículos():
    pass

def estructuraViajes():
    pass


#Fin de funciones para mostrar estructura de datos------------------------------------------

    
#INTEFAZ GRÁFICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#----------------------------------------------------------------------------

#Creo la ventana principal
ventana = tk.Tk()
ventana.title("Llega Rapidito")
ventana.geometry("1200x700")


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
frame3= tk.Frame(frame11)#clientes
frame3.config(border=2, relief="groove", borderwidth=5)
frame3.pack(side=tk.RIGHT)
frame4= tk.Frame(frame11)#Vehículos
frame4.config(border=2, relief="groove", borderwidth=5)
frame4.pack(side=tk.RIGHT)
frame5= tk.Frame(frame11)#Viajes
frame5.config(border=2, relief="groove", borderwidth=5)
frame5.pack(side=tk.RIGHT)

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




#Creo el botón para enviar la información
frameIngresoRutas = tk.Frame(frame1)
frameIngresoRutas.pack(anchor=tk.CENTER)
botonRutas=tk.Button(frameIngresoRutas, text="Cargar Rutas",height="1", width="10", command=cargarRutas)
botonRutas.pack()
botonRutas.config(background="white", foreground="blue", font=("Arial", 14, "bold"))
#FIN DE LA PARTE IZQUIERDA--------------------------------------------------------------------------------------------------------------------------


#DERECHA---------------------------------------------------------------------------------------------------------------------------
#Creo el editor de texto
info=tk.Label(frame2,text=" ") #Aquí se mostrará la información de los clientes, vehículos y viajes
info.pack()
info.config(foreground="red", font=("Arial", 9, "italic"))
edittxt=tk.Label(frame2, text="Visualice la información aquí")
edittxt.pack()
edittxt.config(foreground="black", font=("Arial", 14, "bold"))

scroll=tk.Scrollbar(frame2, orient="vertical")
scroll.pack(side="right", fill="y")

entrada = tk.Text(frame2, height=26, width=75, yscrollcommand=scroll.set)
entrada.pack(side="left", fill="both", expand=True)
scroll.config(command=entrada.yview)

entrada.config(font=("consolas", 11))
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
abrir = tk.Button(frameizquierdo2, text="Eliminar", height="1", width="11", command=limpiar)
abrir.pack()
abrir.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Información
guardo = tk.Button(framederecho2, text="Mostrar Información", height="1", width="22", command=limpiar)
guardo.pack()
guardo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para modificar
guardoComo = tk.Button(frameizquierdo2, text="Modificar", height="1", width="11", command=limpiar)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Estructura de Datos
guardoComo = tk.Button(framederecho2, text="Mostrar Estructura de Datos", height="1", width="22", command=limpiar)
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
nuevo = tk.Button(frameizquierdo1, text="Crear", height="1", width="11", command=limpiar)
nuevo.pack()
nuevo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Eliminar
abrir = tk.Button(frameizquierdo1, text="Eliminar", height="1", width="11", command=limpiar)
abrir.pack()
abrir.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Información
guardo = tk.Button(framederecho1, text="Mostrar Información", height="1", width="22", command=limpiar)
guardo.pack()
guardo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para modificar
guardoComo = tk.Button(frameizquierdo1, text="Modificar", height="1", width="11", command=limpiar)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Estructura de Datos
guardoComo = tk.Button(framederecho1, text="Mostrar Estructura de Datos", height="1", width="22", command=limpiar)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))
#FIN DE LA PARTE DE ABAJO--------------------------------------------------------------------------------------------------------------------------


#Menu para los VIAJES---------------------------------------------------------------------------------------------------------------------------
contenedorViajes=tk.Frame(frame5)
contenedorViajes.pack(ipady=5,ipadx=5, padx=5, pady=5)
tituloViajes = tk.Label(contenedorViajes, text="VIAJES", font=("Arial", 15, "bold"))
tituloViajes.pack(side="top")

#Creación del botón para Crear
nuevo = tk.Button(contenedorViajes, text="Crear", height="1", width="22", command=limpiar)
nuevo.pack()
nuevo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Estructura de Datos
guardoComo = tk.Button(contenedorViajes, text="Mostrar Estructura de Datos", height="1", width="22", command=limpiar)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#----------------------------------------------------------------------------
#Creo la barra
barra=tk.Menu(ventana)
carga=tk.Menu(barra, tearoff=0)
carga.add_command(label="Cargar Clientes", command=cargaMasivaClientes)
carga.add_command(label="Cargar Vehículos", command=cargaMasivaVehículos)


# Agregar acerca de y salir
barra.add_cascade(label="Carga Masiva", menu=carga)
barra.add_command(label="Acerca de", command=acerca_de)
barra.add_command(label="Salir", command=ventana.quit)

# Asignar la barra de menús a la ventana principal
ventana.config(menu=barra)
#----------------------------------------------------------------------------


#Ejecuta la ventana
ventana.mainloop()
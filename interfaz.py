import tkinter as tk
from tkinter import messagebox
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

    
def actualizarInfo(): #Solo actualizo los datos de los labels y las rutas de las imagenes
    pass

def analizar(): #Función para analizar el texto del editor
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
        #                  651CVD:     Marca:     Modelo:    precio   
        patronUsuario=r'\s*(.{6}):\s*([A-Za-z]+):\s*(.+):\s*([A-Za-z]+)'

        #Ciclo para ir separando los clientes
        print(vehiculos)
        
        vehiculitos=vehiculos.split(";")
        print("Se hizo split------------------------------------")
        for vehiculo in vehiculitos:
            print(vehiculo)
            datos=re.search(patronUsuario, vehiculo)
            if datos:
                print(f"Usuario: {datos.group(1)} {datos.group(2)} {datos.group(3)} {datos.group(4)}")
                #Instancio al cliente y lo inserto en la lista circular
                vehiculete:clases.Cliente=clases.Cliente(datos.group(1), datos.group(2), datos.group(3), datos.group(4))
                vehículos.insertarValor(vehiculete)
    else:
        print("No se pudo abrir el archivo")
        messagebox.showerror("Error", "No se pudo abrir el archivo.")





    pass








    
#INTEFAZ GRÁFICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#----------------------------------------------------------------------------

#Creo la ventana principal
ventana = tk.Tk()
ventana.title("Llega Rapidito")
ventana.geometry("1200x700")


# Creación de los frames para la interfaz
frame1 = tk.Frame(ventana)
frame1.pack(side=tk.LEFT)
frame1.config(border=2, relief="groove", borderwidth=30)
frame2 = tk.Frame(ventana)
frame2.pack(side=tk.RIGHT)
frame2.config(border=2, relief="groove",borderwidth=30)

#Estos frames son para organizar los:
frame3= tk.Frame(frame2)#clientes
frame3.pack(side=tk.BOTTOM)
frame4= tk.Frame(frame3)#Vehículos
frame4.pack(side=tk.BOTTOM)
frame5= tk.Frame(frame3)#Viajes
frame5.pack(side=tk.BOTTOM)


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

#Menu para los CLIENTES---------------------------------------------------------------------------------------------------------------------------
contenedorClientes=tk.Frame(frame3)
contenedorClientes.pack(ipady=5,ipadx=5, padx=5, pady=5)
contenedorClientes.config(border=2, relief="groove")
tituloClientes = tk.Label(contenedorClientes, text="CLIENTES", font=("Arial", 15, "bold"))
tituloClientes.pack(side="top")

#Creación del botón para Crear
nuevo = tk.Button(contenedorClientes, text="Crear", height="1", width="11", command=limpiar)
nuevo.pack(side="left")
nuevo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Eliminar
abrir = tk.Button(contenedorClientes, text="Eliminar", height="1", width="11", command=limpiar)
abrir.pack(side="right")
abrir.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Información
guardo = tk.Button(contenedorClientes, text="Mostrar Información", height="1", width="16", command=limpiar)
guardo.pack()
guardo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para modificar
guardoComo = tk.Button(contenedorClientes, text="Modificar", height="1", width="11", command=limpiar)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Estructura de Datos
guardoComo = tk.Button(contenedorClientes, text="Mostrar Estructura de Datos", height="1", width="22", command=limpiar)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Menu para los VEHÍCULOS---------------------------------------------------------------------------------------------------------------------------
contenedorVehiculos=tk.Frame(frame4)
contenedorVehiculos.pack(ipady=5,ipadx=5, padx=5, pady=5)
contenedorVehiculos.config(border=2, relief="groove")
tituloVehiculo = tk.Label(contenedorVehiculos, text="VEHÍCULOS", font=("Arial", 15, "bold"))
tituloVehiculo.pack(side="top")

#Creación del botón para Crear
nuevo = tk.Button(contenedorVehiculos, text="Crear", height="1", width="11", command=limpiar)
nuevo.pack(side="left")
nuevo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Eliminar
abrir = tk.Button(contenedorVehiculos, text="Eliminar", height="1", width="11", command=limpiar)
abrir.pack(side="right")
abrir.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Información
guardo = tk.Button(contenedorVehiculos, text="Mostrar Información", height="1", width="16", command=limpiar)
guardo.pack()
guardo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para modificar
guardoComo = tk.Button(contenedorVehiculos, text="Modificar", height="1", width="11", command=limpiar)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Creación del botón para Mostrar Estructura de Datos
guardoComo = tk.Button(contenedorVehiculos, text="Mostrar Estructura de Datos", height="1", width="22", command=limpiar)
guardoComo.pack()
guardoComo.config(background="white", foreground="black", font=("Arial", 10, "bold"))

#Menu para los VIAJES---------------------------------------------------------------------------------------------------------------------------
contenedorViajes=tk.Frame(frame5)
contenedorViajes.pack(ipady=5,ipadx=5, padx=5, pady=5)
contenedorViajes.config(border=2, relief="groove")
tituloViajes = tk.Label(contenedorViajes, text="VIAJES", font=("Arial", 15, "bold"))
tituloViajes.pack(side="top")

#Creación del botón para Crear
nuevo = tk.Button(contenedorViajes, text="Crear", height="1", width="11", command=limpiar)
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
carga.add_command(label="Cargar Vehículos", command=cargarRutas)


# Agregar acerca de y salir
barra.add_cascade(label="Carga Masiva", menu=carga)
barra.add_command(label="Acerca de", command=acerca_de)
barra.add_command(label="Salir", command=ventana.quit)

# Asignar la barra de menús a la ventana principal
ventana.config(menu=barra)
#----------------------------------------------------------------------------


#Ejecuta la ventana
ventana.mainloop()
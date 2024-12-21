import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess

#Declarando mis variables globales
rutaGrafica="C:/banderas/nono.png"


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
try:
    imagenRutas = Image.open("C:/banderas/nono.png")

    anchoImagen, altoImagen = imagenRutas.size
    anchoCanvas, altoCanvas = 700, 500
    imagen_tk = ImageTk.PhotoImage(imagenRutas)

    #Cálculo para para redimensionar la imagen
    proporcionImagen=anchoImagen/altoImagen
    proporcionCanvas=anchoCanvas/altoCanvas

    if proporcionImagen>proporcionCanvas:
        nuevoAncho=anchoCanvas
        nuevoAlto=int(anchoCanvas/proporcionImagen)
    else:
        nuevoAlto=altoCanvas
        nuevoAncho=int(altoCanvas*proporcionImagen)

    imagenRutas=imagenRutas.resize((nuevoAncho,nuevoAlto), Image.LANCZOS)
    imgencita=imagen_tk.PhototImage(imagenRutas)

    canvas = tk.Canvas(frame1, width=anchoCanvas, height=altoCanvas)
    canvas.pack()

    x=(anchoCanvas-nuevoAncho)//2
    y=(altoCanvas-nuevoAlto)//2

    #Coloco la imagen en el canvas
    canvas.create_image(x, y, anchor=tk.CENTER, image=imagen_tk)

except FileNotFoundError:
    print("Error: La imagen no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
    exit()



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

# Agregar acerca de y salir
barra.add_command(label="Acerca de", command=acerca_de)
barra.add_command(label="Salir", command=ventana.quit)

# Asignar la barra de menús a la ventana principal
ventana.config(menu=barra)
#----------------------------------------------------------------------------


#Ejecuta la ventana
ventana.mainloop()
# Gestión de viajes con árbol B, listas y grafos en Python

Aplicación de escritorio para clientes, vehículos, rutas y viajes. Implementa árbol B para vehículos, listas enlazadas/circulares y listas de adyacencia para rutas, con reportes Graphviz e interfaz Tkinter.

## Requisitos

Python 3 con Tkinter, paquetes de requirements.txt y Graphviz instalado como programa del sistema (dot en PATH).

## Ejecución

Los comandos parten de la raíz del repositorio, salvo donde se indica otra terminal.

```bash
python -m pip install -r requirements.txt
python interfaz.py
```

## Recorrido de demostración

Cargar los archivos de pruebas/ desde la interfaz: Clientes.txt, Vehiculos.txt y Rutas.txt. Consultar los manuales para generar viajes y reportes. main.py contiene demostraciones de estructuras; interfaz.py es la aplicación gráfica.

## Organización

Carpetas de la entrega: [`docs/`](docs/), [`pruebas/`](pruebas/).

## Documentación

- [manualTecnico](docs/manualTecnico.md)
- [manualUsuario](docs/manualUsuario.md)

## Alcance y límites

Las colecciones se mantienen en memoria. Este proyecto no implementa blockchain, árboles Merkle ni una base de datos persistente. Las ventanas necesitan una sesión gráfica.

## Contexto y licencia

Trabajo académico o de aprendizaje conservado en el portafolio de [Enner Mendizabal](https://github.com/Ennero). Los créditos de los trabajos en grupo se conservan en sus entregas y manuales.

Consultar [LICENSE](LICENSE) para la licencia de la raíz. Las dependencias y los componentes con avisos o licencias propios conservan sus condiciones.

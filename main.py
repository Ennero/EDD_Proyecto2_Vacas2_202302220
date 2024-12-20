from arbolito import ArbolB
import clases


cliente=clases.Cliente(3,"jksjkd","sfksjdf","sdkjfkls",2,"ksdjfsklf")

print(cliente.getNombre())

'''arbolB: ArbolB=ArbolB(5)
arbolB.insertarClavecita(5)
arbolB.insertarClavecita(6)
arbolB.insertarClavecita(4)
arbolB.insertarClavecita(2)
arbolB.insertarClavecita(7)
arbolB.insertarClavecita(9)
arbolB.insertarClavecita(10)
arbolB.insertarClavecita(3)
arbolB.insertarClavecita(1)
arbolB.insertarClavecita(12)
arbolB.insertarClavecita(0)

print(arbolB.imprimirUsuario())

arbolB.insertarClavecita(-1)
arbolB.insertarClavecita(13)
arbolB.insertarClavecita(20)
'''
'''
# Crear el árbol B de orden 5
arbol = ArbolB(5)

# Insertar valores para probar
valores = [30, 20, 40, 10, 50, 60, 70, 35]
print("Insertando valores:", valores)

for valor in valores:
    arbol.insertarClavecita(valor)

# Generar y mostrar el código DOT
dot_code = arbol.imprimirUsuario()
print("\nCódigo DOT generado:")
print(dot_code)'''
from arbolito import ArbolB
import clases
import graphviz


cliente=clases.Cliente(3,"jksjkd","sfksjdf","sdkjfkls",2,"ksdjfsklf")

print(cliente.getNombre())


arbolB: ArbolB=ArbolB(5)
arbolB.insertarValor(5)
arbolB.insertarValor(6)
arbolB.insertarValor(4)
arbolB.insertarValor(2)
arbolB.insertarValor(45)
arbolB.insertarValor(45)
arbolB.insertarValor(34)
arbolB.insertarValor(3)
arbolB.insertarValor(1)
arbolB.insertarValor(12)
arbolB.insertarValor(0)
arbolB.insertarValor(7)
arbolB.insertarValor(8)
arbolB.insertarValor(9)
arbolB.insertarValor(10)
arbolB.insertarValor(11)
arbolB.insertarValor(13)
arbolB.insertarValor(14)

arbolB.generarGrafica("ArbolB")

'''grafiquita: str = arbolB.imprimirUsuario()
graph = graphviz.Source(grafiquita)
graph.render('ArbolB', format='pdf', view=True)'''









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
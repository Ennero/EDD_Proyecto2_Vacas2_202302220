from arbolito import ArbolB
import clases


cliente=clases.Cliente(3,"jksjkd","sfksjdf","sdkjfkls",2,"ksdjfsklf")

print(cliente.getNombre())

arbolB: ArbolB=ArbolB(5)
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
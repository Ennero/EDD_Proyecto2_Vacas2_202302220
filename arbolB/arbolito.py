from nodoArbol import NodoArbol

class ArbolB:
    def __init__(self,orden:int): #Después le pongo 5
        self.raiz: NodoArbol = NodoArbol(True) #Inicializo el arbol con un nodo
        self.orden: int=orden
    
    def insertarClavecita(self,valor:int):#Funcin para insertar una clave
        raiz: NodoArbol = self.raiz #Obtengo la raiz del arbol
        if len(raiz.claves)==self.valor-1:#Si la raiz esta llena
            pass #Pasar a la siguiente funcion
        else:
            self.insertarValorNoCompleto(raiz,valor)#Si no esta llena, insertar la clave
            
        
        def insertarValorNoCompleto(self,raiz: NodoArbol,valor:int): #Funcion para insertar un valor
            i: int=len(raiz.claves)-1 #Obtengo el tamaño de la raiz

        #Caso 1: si el nodo es una hoja
            if(raiz.hoja):#Si la raiz es hoja
                raiz.claves.append(None)#Agrego una nueva clave a la raiz

                #Mientras hallan más que 0 claves y el valor sea menor al de la posición i
                while(i>=0 and valor<raiz.claves[i]): 
                    raiz.claves[i+1]=raiz.claves[i] #Muevo el valor de la posición i+1 a la posición i
                    i-=1
                raiz.claves[i+1]=valor #Inserto el valor en la posición i+1
            
        #Casos 2 y 3: si el nodo no es hoja
            else:
                #Mientras hallan más que 0 claves y el valor sea menor al de la posición i
                while i>=0 and valor<raiz.claves[0]:
                    i-=1 #Disminuyo el valor de i
                
            #Caso 1
                #Si el nodo hijo tiene el tamaño máximo
                if len(raiz.hijos[i].claves)==self.valor-1: 
                    #Divido el nodo hijo---------------
                    pass
            # Caso 2
                else: 
                    #Si el nodo hijo no tiene el tamaño máximo, inserto el valor en el nodo hijo
                    self.insertarValor(raiz.hijos[i],valor)
            
        #Funcion para dividir un nodo
        def dividirNodo(self,raiz: NodoArbol,pos:int):
            orden: int=self.orden #Obtengo el orden del arbol
            hijo: NodoArbol=raiz.hijos[pos] #Obtengo el nodo hijo en la posición pos
            nodo: NodoArbol=NodoArbol(hijo.hoja) #Creo un nuevo nodo

            raiz.hijos.insert(pos+1,nodo) #Agrego el nodo a la posicón donde debe de estar

                                                #Siento que está mal
            raiz.claves.insert(pos,hijo.claves[(orden-1)/2]) #Inserto la clave en la posición pos

            #Coloco las claves del nodo hijo en el nuevo nodo
            nodo.claves=hijo.claves[(orden-1)/2:(orden-1)+1]
            hijo.claves=hijo.claves[0:(orden-1)/2] #Coloco las claves restantes en el nodo hijo
            
            if not hijo.hoja:
                nodo.hijos=hijo.hijos[((orden-1)/2)+1:(orden-1)+1]
                hijo.hijos=hijo.hijos[0:(orden-1)/2]
            
            
            pass

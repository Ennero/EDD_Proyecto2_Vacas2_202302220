class Node:
    def __init__(self):
        self.keys=[]
        self.children=[]

    def __repr__(self):
        pass

class BTree:
    def __init__(self):
        self.minKeys=t-1
        self.maxKeys=2*t-1

        self.root=Node()

    def splitChild(self,parent:Node, childIndex:int):
        newRightChild=Node()
        halfMax=self.macKeys//2
        child=parent.children[childIndex]
        middleKey=child.keys[halfMax]
        newRightChild.keys=child.keys[halfMax+1:]
        child.keys=child.keys[:halfMax]

        if not child.isLeaf:
            newRightChild.children=child.children[halfMax+1:]
            child.children=child.children[:halfMax+1]
        
        parent.keys.insert(childIndex,middleKey)
        parent.children.insert(childIndex+1,newRightChild)


    def insertKeys(self,key):
        if len(self.root.keys)>=self.maxKeys:
            newRoot=Node()
            newRoot.children.append(self.root)
            self.root=newRoot
            self.splitChild(newRoot,0)
            self.insertNonFull(self.root,key)
        else:
            self.insertNonFull(self.root,key)

    def insertNonFull(self,node:Node,key):
        i=len(node.keys)-1
        while i>=0 and node.keys[i]>key:
            i-=1
        
        if node.isLeaf:
            node.keys.insert(i+1,key)
        else:
            if len(node.children[i+1].keys)>=self.maxKeys:
                self.splitChild(node,i+1)
                if node.keys[i+1]<key:
                    i+=1

        self.insertNonFull(node.children[i+1],key)

    def find(self, key)->bool:
        nodoActual=self.root
        while True:
            i=len(nodoActual.keys)-1
            while i>=0 and nodoActual.keys[i]>key:
                i-=1

            if i>=0 and nodoActual.keys[i]==key:
                return True
            elif nodoActual.isLeaf:
                return False
            else:
                nodoActual=nodoActual.children[i+1]

    def removeKey(self, key):
        self.removeKeyFromNode(self.root,key)

    def _removeKey(self, node:Node, key)->bool:
        try:
            index=node.keys.index(key)
            if node.isLeaf:
                node.keys.pop(index)
                return True
            else:
                self.removfromNonLeaf(node,index)
            return True
        except:
            if node.isLeaf:
                print("Llave no encontrada")
                return False
            else:
                i=0
                KeysNumber=len(node.keys)
                while i<KeysNumber and node.keys[i]<key:
                    i+=1
                actionPerformed=self._repairTree(node, i)
                if actionPerformed:
                    return self._removeKey(node, key)
                else:
                    return self._removeKey(node.children[i], key)
                

    def _repairTree(self, node:Node, index:int)->bool:
        child=node.children[index]
        if self.minKeys<=len(child.keys)<=self.maxKeys:
            return False
        
        if index>0 and len(node.children[index-1].keys)>self.minKeys:
            self._rotateRight(node,index)
            return True
        
        if (index<len(node.keys) and len(node.children[index+1].keys)>self.minKeys and len(node.children[index+1].keys)>self.minKeys):
            return True
        
        if (index>0):
            self._merge(node,index-1,index)
        else:
            self._merge(node,index,index+1)

        return True

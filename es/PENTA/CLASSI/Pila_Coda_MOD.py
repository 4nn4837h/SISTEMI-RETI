""" Modulo di: Pila e Coda
    Modulo in Py == libreria C"""

from xml.etree.ElementTree import PI


class Pila(): # classe dotata di due metodi: push e pop
    def __init__(self):
        self.pila = []
        
    def push(self, elemento): # i metodi devo sempre passare self == this. un metodo che non ha parametri, nella sua definizione ha anche self
        self.pila.append(elemento)
        
    def pop(self):
        if len(self.pila) > 0: return self.pila.pop()
        else: return None
    
    def funzione(x, y, z):
        pass
    
    def print(self):
        print(self.pila)
        
class Coda(object):
    def __init__(self) -> None:
        self.coda = []
        
    def enqueue(self, elemento): # i metodi devo sempre passare self == this. un metodo che non ha parametri, nella sua definizione ha anche self
        self.coda.append(elemento)
        
    def dequeue(self):
        if len(self.coda) > 0: return self.coda.pop(0)
        else: return None
        
    def print(self):
        print(self.coda)
        
def main():
    p = Pila()
    q = Coda()
    
    p.push(1)
    p.push(3)
    x = p.pop()
    p.print()
    
    q.enqueue(5)
    q.enqueue(4)
    y = q.dequeue()
    q.print()
    
if __name__ == "__main__":
    main()
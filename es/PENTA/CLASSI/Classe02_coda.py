""" Classe_03: Coda
Libreria esterna: modulo
"""
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
        
c1 = Coda()
c1.enqueue("something")
c1.enqueue("Something Again")
c1.print()
c1.dequeue()
c1.print()
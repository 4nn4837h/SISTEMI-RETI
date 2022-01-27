"""Classe Pila: con le sue funzioni predefinite e una funzione(metodo) con pass"""

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
    
p1 = Pila() # istanza della classe Pila == chiamare + eseguire il costruttore (che si chiama __init__, sempre)
print("Viene inserito l'elemento 'ciao'")
p1.push("ciao") # non devo chiamare la pila stessa nella chiamata
print("Stampo la pila:")
p1.print()
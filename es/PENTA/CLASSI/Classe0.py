"""CLASSI:
    lettera maiuscola per il nome della classe:
    costruttore
    attributi -> si possono definire o internamente al costruttore o appena "invocata" la classe
"""
class Pila(): # classe dotata di due metodi: push e pop
    def __init__(self, lista): # costruttore della classe, di ogni classe 
        self.pila = lista # self = this in Java

# p1 istanza di Pila
p1 = Pila([1, 2, 3]) # quando chiamo la classe così invoca direttamente il costruttore
print(p1.pila)
      
# class Pila(object):  == class Pila():
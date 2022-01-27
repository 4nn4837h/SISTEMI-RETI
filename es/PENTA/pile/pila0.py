""" Esercizio 13/01/2022
Risolvere il bug della pop che si chiama su una pila vuota"""

def push(pila, elemento):
    pila.append(elemento)
    
def pop(pila):
    if len(pila) > 0: return pila.pop()
    return None # pila = []

pila = [1, 2, 3, 4]
push(pila, 9999)
print(pila)
pop(pila)
print(pila)

pila2 = []
pop(pila2)

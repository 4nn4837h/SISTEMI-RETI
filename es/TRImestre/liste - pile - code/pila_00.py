"""esercizio pile in py:
                  ^
                  |
                HEAD
"""
pila = [1, 2, 3, 4, 5]
pila.append(6) # push
print(pila)
elemento = pila.pop() # tolgo elemento
print(elemento)
print(pila)
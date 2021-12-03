""" ESERCIZIO: 18 (4)
"""
lista = [] # lista vuota
print(f"Inserisci due numeri qualsiasi:")
n1 = int(input("I numero"))
n2 = int(input("II numero"))

lista.append((n1**2) + (n2**2))
lista.append((n1 + n2)**2)
lista.append((n1**2) - (n2**2))
lista.append((n1-n2)**2)
# oppure creare la lista da capo
print(lista)
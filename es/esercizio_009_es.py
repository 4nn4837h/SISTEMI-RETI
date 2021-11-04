"""
Crea un programma in Python in cui:
inizializzi la lista x=[0, 1, 2, 3, 4, 5, 6, 7, 8] e poi:
- crea due nuove liste  contenenti ciascuna una delle due metà della lista;
- aggiungi il valore 5 alla lista conenente la prima metà.
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
x1 = x[:5]
x2 = x[5:]
x1.append(5)
print(x1)
print(x2)

""" in Python ci sono tutti gli operatori matematici:
a**b --> elevamento a potenza
a/b --> divisione tra float
a//b -->DIV: divisione intera (5/2 = 2)
a&b --> MOD: modulo: resto della divisione intera """


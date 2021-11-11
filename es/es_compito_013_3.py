"""     ESERCIZIO 3:
Scrivi un programma in Python che permetta all’utente di inserire le coordinate di due punti del piano cartesiano.
I punti devono essere salvati all’interno di tuple. Stampa la distanza euclidea tra i due punti.
"""
import math # inserisco la libreria nel codice per effettuare l'operazione della radice quadrata

c1a = float(input("Inserisci la latitudine (N > 0 o S < 0):"))
c1b = float(input("Inserisci la longiitudine (E > 0 o W < 0):"))
c2a = float(input("Inserisci la latitudine (N > 0 o S < 0):"))
c2b = float(input("Inserisci la longitudine (E > 0 o W < 0):"))
tupla1 = (c1a, c1b)
tupla2 = (c2a, c2b)
#print(tupla1, tupla2)
distanza = math.sqrt((tupla1[0] - tupla2[0])**2 + (tupla1[1] - tupla2[1])**2)
print(f"La distanza tra i due punti vale: ", distanza)

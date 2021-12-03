""" ESERCIZIO: 6
Utilizza le list comprehension per generare la tavola pitagorica.
"""
tavola = [(x * y) for x in range(11) for y in range(11)]
indice = 0
indice2 = 0

"""for k in range(11): # qui la variabile (in Py un oggetto) non serve e il k utilizza memoria
    print(tavola[indice][indice2]):
    indice += 1
    indice2 += 1 """

for _ in range(11): # qui l'underscore non occupa memoria
    print(tavolaPitagorica[indice][indice2])
    indice += 1
    indice2 += 1

# oppure si può usare una lista di liste
tavolapitagorica = [[x * y for x in range(11)] for y in range(11)]
# prima quadra: la x aumenta sempre di 1
# seconda quadra: la y, dopo che la x ha fatto il suo giro, aumenta anche lei di 1 alla volta

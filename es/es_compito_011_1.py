""" ESERCIZIO: 1
Crea un programma in Python in cui inizializzi un dizionario che funga da rubrica telefonica.
Scegli alcuni dei tuoi amici e usa il loro nome come chiave del dizionario, il loro numero di telefono come valore.
Stampa il numero di telefono di un amico a tua scelta.
Aggiungi un nuovo amico alla rubrica e stampa l’intero dizionario.
"""
rubrica = {"Ciro":"1111111111", "Gabry":"2222222222", "Willy":"3333333333"}
print(rubrica["Gabry"]) # dizionari: indicizzati dalle loro chiavi
rubrica["Bestie"] = "4444444444" # aggiungo un elemento al dizionario
print(rubrica)

"""     ESERCIZIO: 2:   Crea una funzione Python che data una lista di numeri, ritorni il suo valore massimo e il suo valore minimo.    """
listaDiNumeri = [2, 5, 7, 10, 43, 76, 83, 24, 76, 43, 90, 21, 12, 54, 67]
numeroPiuPiccolo = listaDiNumeri[0]
numeroPiuGrande = listaDiNumeri[0]

for numero in listaDiNumeri:
    if numeroPiuGrande < numero:
        numeroPiuGrande = numero
    if numeroPiuPiccolo > numero:
        numeroPiuPiccolo = numero
        
print(f"Il numero minore della lista è: {numeroPiuPiccolo}, mentre il numero maggiore è: {numeroPiuGrande}")            
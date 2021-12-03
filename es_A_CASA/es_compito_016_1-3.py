"""     ESERCIZIO:
Crea un programma in Python che permetta all'utente di inserire un numero qualunque di interi all'interno di una lista.
Stampa la lista al termine dell'inserimento.
"""
conta = 0
serieDiNumeriInteri = [] # per inizializzare la lista, in modo che non la consideri una tupla o un dizionario dato che l'indicizzazione è uguale per tutte e 
                         # tre le "strutture"
risposta = int(input("Vuoi inserire dei numeri?\n0 = no, 1 = sì: "))

while risposta == 1:
    serieDiNumeriInteri.append(int(input("Inserisci il numero: ")))
    conta = conta + 1
    risposta = int(input("Vuoi inserire dei numeri?\n0 = no, 1 = sì: "))

print(f"Ora la lista contiene i seguenti valori interi:")
for valore in serieDiNumeriInteri:
    print(valore)
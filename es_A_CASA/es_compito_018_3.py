"""     ESERCIZIO: 3
Scrivi un programma in Python in cui chiedi all’utente un numero e comunichi se esso è primo oppure no. 
Per stabilire se il numero è primo crea una funzione apposita che ritorni True se il numero è primo, False altrimenti. 
"""
def isPrimo(numero): # brute force
    conta = 2
    primo = True
    while ((conta < numero) & (primo == True)): # deve partire da due altrimenti ogni numero sarebbe divisibile per uno e il risultato sarebbe sbagliato
        if( numero % conta) == 0: 
            primo = False
        conta = conta + 1    
    return primo

numero = int(input("Inserisci un numero a tua scelta, intero: ")) # ricordatisempre la conversione perché questa funzione ritorna sempre stringhe
if isPrimo(numero):print(f"Il numero è primo!")
else: print(f"Il numero NON è primo!")    
""" ESERCIZIO: 3
Scrivi un programma in Python in cui chiedi all’utente un numero e comunichi se esso è divisibile per
2, oppure per 3, oppure per 5,oppure per nessuno di essi. 
"""
numero = int(input("Inserisci un numero a tua scelta: "))

if numero % 2 == 0:
    print(f"Il numero {numero} è divisibile per 2!")
elif numero % 3 == 0:
    print(f"Il numero {numero} è divisibile per 3!")
elif numero % 5 == 0:
    print(f"Il numero {numero} è divisibile per 5!")
else:
    print("Il numero {numero} non è divisibile per alcun numero tra 2, 3 e 5")
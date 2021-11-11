"""     ESERCIZIO: 5
Scrivi un programma in Python che permetta all’utente di inserire un numero intero e una stringa:
concatena la stringa con sé stessa tante volte quante il numero e stampa il risultato.
"""
numero = int(input("inserisci un numero intero: "))
stringa = input("inserisci una parola o una frase: ")
stringa = numero * stringa
print(stringa)
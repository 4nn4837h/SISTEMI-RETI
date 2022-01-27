"""ESERCIZIO: 1
Utilizzando le list comprehension scrivi un programma che crei una lista con tutte le potenze di due
minori o uguali a un valore inserito dall’utente. Stampa la lista. 
""" 
valore = int(input("Inserisci un numero a tua scelta: "))
potenzeDue = [2**k for k in range(valore) if(2**k <= valore)] # il k parte da 0
print(potenzeDue)
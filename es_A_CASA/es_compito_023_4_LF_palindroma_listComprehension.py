""" ESERCIZIO: 4
4 Data una lista di stringhe estrai da essa la lista di stringhe che sono palindrome e la lista di stringhe che hanno iniziale maiuscola. 
ricordati che in python tutto è un oggetto: sia funzioni che variabili
"""
lista, listaM, listaP = ["ciao", "poveri"], [], [] # ricorda di inizializzarle vuote, altrimnti l'append non funge
for elemento in lista:
    if(palindroma(parola)):
        listaP.append(elemento)
        if(maggiore(elemento)):
            listaM.append(elemento)

palindroma = lambda stringa : (stringa == stringa[::-1])
maggiore = lambda parola : parola[0] == parola[0].upper

parole = ["ciao", "Anna", "Alice"]
palindrome = [parola for parola in parole if parola == parola[::-1]]
maiuscole = [parola for parola in parole if(parola[0] >= 'A' & parola[0] <= 'Z')] # list cpmprehension

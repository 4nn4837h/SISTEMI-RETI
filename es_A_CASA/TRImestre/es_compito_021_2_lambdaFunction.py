"""ESERCIZI: 2
Creare una lambda function che ritorni True se una stringa inizia con lettera maiuscola, False altrimenti.

nome della funzione = lambda parametri : (codice di uscita)

"""
def maiuscolaF2(parola):
    return parola[0] >= 'A' & parola[0] <= 'Z'

def maiuscolaF(parola):
    return parola[0] == parola[0].upper
print(maiuscolaF("ciao"))

maiuscola = lambda frase : frase.isLower() # true o folase
frase = input("Inserisci una frase: ")
maiuscola(frase[0])

maggiore = lambda parola : parola[0] == parola[0].upper
maggiore(frase)
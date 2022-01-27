"""     ESERCIZIO: 2
Scrivi un programma in Python che permetta all’utente di inserire il suo nome (tramite input)
e stampi il nome in cui tutti i caratteri tranne il primo sono sostituiti da un *.
"""
nome = [input("inserisci il tuo nome: ")]
#print(lista[0], lista[1:]) # stampa tutta la stringa
#nome[1:] = '*'
print(nome[0] + (len(nome)-1)*'*')

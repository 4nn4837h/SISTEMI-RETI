""" ESERCIZIO: 4
Calcola, mediante un opportuno programma in Python, inserisca in una lista i numeri primi minori di 1000. 
Per stabilire se il numero è primo crea una funzione apposita che ritorni True se il numero è primo, False altrimenti.
"""
def isPrimo(numero):
    conta = 2
    primo = True
    while ((conta < numero) & (primo == True)): # deve partire da due altrimenti ogni numero sarebbe divisibile per uno e il risultato sarebbe sbagliato
        if( numero % conta) == 0: 
            primo = False
        conta = conta + 1    
    return primo

# "MAIN"
n = 2 # n parte da 2 perché 2 è effettivamente il primo numero primo, se lo facessi partire da 0 ovviamente mi darebbe 170, 
      # perché 0 e 1 verrebbero considerati dal programma primi
listaNumeriPrimi = [k for k in range(n, 1003) if isPrimo(k)]
for n in listaNumeriPrimi:
    print(n)
"""list comprehension:
per creare e modificare liste:



"""
""" le liste sono mutabili """
lista = [3, 3.1415, "ciao"] # lista eterogenea
lista2 = ["ciao", "non", "sono", "bella"] # lista omogenea
print(lista[-1])
print(lista[1:-1]) # indicizzazione come gli array
lista[1] = 2.716
print(lista)

numeriPrimi = [2, 3, 5, 7, 11, 13]
numeriPrimi.append(17) # ma poteva anche essere "mario" --> mario
print(numeriPrimi)
print(f"La lunghezza della lista: {len(numeriPrimi)}") # dupla, stringa, funziona su tutto

altriNumeriPrimi = [19, 23, 29]
# concatenazione liste:
moltiNumeriPrimi = numeriPrimi + altriNumeriPrimi # che putensaaaaa
print(moltiNumeriPrimi)
# moltiplicare la lista per un numero intero di volte
print(5 * altriNumeriPrimi)

# se in C si cicla su indice: su Python si cicla sugli elementi:
for numeriPrimo in numeriPrimi: # mette subito indentazione,
    # se non fosse indentata non la leggerebbe: perché in python non ci sono le graffe
    print(numeriPrimo, end=" FINE RIGA ") # stampa uno per uno, riga per riga, ma se metto end="..." stamperà qualcosa al posto della backslash n (\n)
def somma_moltiplicazione(x, y):
    somma = x + y
    moltiplicazione = x * y
    return {"somma":somma, "moltiplicazione":moltiplicazione}

"""
LAMBDA FUNCTION:
FUNZIONE MOLTO SEMPLICE:
le variabili che mando: come le chiamo nella funzione
:
primo valore ritornato, secondo valore ritornato
"""
somma_moltiplicazione2 = lambda x, y : (x + y, x * y) 

a = 10
b = 2
print(somma_moltiplicazione2(a, b))

""" SE TUTTE LE COSE SONO OGGETTI:
allora le funzioni sono oggetti
allora posso avere delle liste di oggetti, un dizionario di oggetti
"""
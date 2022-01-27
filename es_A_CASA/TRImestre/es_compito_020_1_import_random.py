"""     ESERCIZIO: 
Simula una partita a dadi TRA DUE GIOCATORI: Alice e Bob.
Il dado è a 6 facce.
Vince col*i che ottiene il punteggio più alto.
Stampa il nome del vincitore.

MODULO: le librerie qui si chiamano moduli:
quindi sono librerie di funzioni, classi già fatte e permettono quindi di realizzare delle funzioni più complesse senza sforzo
sono di 2 tipi:
nativi: se sono moduli già resenti con l'installazione di Python
non nativi: sono quelli esterni
-> import moduli
la chiamata in python deve sempre precedere la libreria
"""
import random
"""lancioDado1.random.int();
lancioDado2.random.int();
battaglia = ("Alice" : lancioDado1, "Bob" : lancioDado2) #dizionario
if(lancioDado1 > lancioDado2): winner = battaglia["Alice"]
else: winner = battaglia["Bob"]"""
Alice = random.randint(1, 6)
Bob = random.randint(1, 6)
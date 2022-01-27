import Pila_Coda_MOD as pc #ALIAS
# Py si va a cercare un file che si chiama Pila_Coda: questo file che importiamo deve essere nella stessa cartella
""" Spazio dei nomi di un progaramma:
in es_moduli.py habbiamo delle funzioni che c'entrano nel programma: e quindi hanno un certo spazio dei nomi
se importo la classe così: lo spazio dei nomi si chiama col punto -->
in C: i nomi delle librerie diventano nomi del programma ==> MA SI PUò DEFINIRE UN ALIAS ==> ovvero: import libreria as ALIAS
"""
p = pc.Pila()
p.push(3) # solo per il costruttore ci va l'alias
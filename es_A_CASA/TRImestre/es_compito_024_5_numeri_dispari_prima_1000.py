""" ESERCIZIO 5
Genera una lista contenente i quadrati perfetti dispari minori di 1000.
"""
import math
quadratiPerfetti = [k for k in range(1001) if math.sqrt(k) % 1 == 0] # non c'è stato bisogno di inizializzare la lista
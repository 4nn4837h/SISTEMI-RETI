"""x = 123
y = x
x = "ciao"
avviene la garbage collection: pulizia della cella di memoria che ha cambiato il tipo e cambiato il valore della variabile = ORFANA
un po' come la free in c, qui lo fa in aurtomatico"""
"""SLICING"""
stringa = "Classe quarta A robotica"
print(f"Il primo carattere della stringa è: {stringa[0]}")
print(f"Il primo carattere della stringa è: {stringa[-1]}")
print(stringa[3:9])     # sottostringa: prende i caratteri dal primo indice al secondo -1
print(stringa[0:6])     # prende "Classe"
print(stringa[6:])      # dal carattere 6 alla fine
print(stringa[:-2])     # dall'inizio fino al carattere -3
print(stringa[2:14:2])  #step or gap: prende tutto dal 2 al 13 (14-1), saltando di 2 {utile sugli array}
print(stringa[::-1])    # prende tutta la stringa a salti di -1 -> la stampa al contrario

# se volessimo cambiare la stringa -> il terminale ci dice: ERRORE, perché le STRINGHE SONO IMMUTABILE
# -> TypeError: 'str' object does not support item assignement
# per cui se la voglio cambiare faccio una sorta di taglia e cuci:
stringa_nuova = stringa[:14] + "B" + stringa[15:]
print(stringa_nuova)
print(f"LA STRINGA CAMBIATA E': {stringa_nuova}")

print(print)    # <built-in> function -> ti da informazioni su ciò che stampi: e quindi sarebbe quaso in grado di
                # stampare una funzione, la print: SUPERPOWER

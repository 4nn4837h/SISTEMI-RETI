x = 3.1415 # un float: che bisgona scrivere necessariamnete col punto
tupla = 3, 1415 # questa variabile è di tipo tupla: ha due valori al suo interno: 3 e 1415
a = 4 #commento di una riga sola, un intero
""" un commento
su più righe """

y = x * a # anche qui calcola tutto per scontato calcolando lui le cose che gli servono

# utile epr stampare le variabili: f-string
print(f"Il valore di y è {y}") # unicode -> evoluzione dell'ASCII
print(f"{x} moltiplicato per {a} vale {y}")
# senza la f dentro la parentesi non si possono stapare i valori delle variabili:
print("{x} moltiplicato per {a} vale {y}")

###################################################################################################################################################
a = float(input("Inserisci un numero")) # la funzione input da come valore di ritorno una stringa, per cui faccio un casting 

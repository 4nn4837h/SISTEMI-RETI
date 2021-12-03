"""
SIMONDI FRANCESCA IV A ROB
Crea un programma in Python in cui assegni una parola di almeno 8 lettere a una variabile stringa e poi stampi tutta la parola con un carattere
? al posto della terza lettera.
"""
parola = "HoOttoCaratteri"
if parola[-1] == parola[7]: # se metto meno di 8 caratteri dice che c'è un errore
    print(f"La stringa ha 8 caratteri:")
    print(parola[:2] + "?" + parola[3:])
elif parola[7] == None:
    print(f"La parola non ha sufficienti caratteri: 8.")
else:
    print(parola[:2] + "?" + parola[3:])

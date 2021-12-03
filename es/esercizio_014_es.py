"""Esercizio:
Crea una funzione in py che data una lista di stringhe ristorni la stringa più lunga della lista
"""
parole = ["ciao", "sono", "Rebecca", "Simondi", "la", "sorella", "di Francesca", "Simondi"] #lista
parolaPiuLunga = parole[0]

for parola in parole:
    if len(parolaPiuLunga) < len(parola):
        parolaPiuLunga = parola

print(f"La stringa più lunga della lista è: {parolaPiuLunga}")
print(f"La stringa più lunga della lista è: " + parolaPiuLunga)
# se hai problemi con gli esercizi, prima falli SU CARTA, a cumputer spento
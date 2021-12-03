"""
Scrivi un programma che permetta all'utente di effettuare le quattro opeazioni aritmetiche fondamentali
"""
operazione = int(input("0:somma\n1:Sottrazione\n2:Moltiplicazione\n3:Divisione"))
n1 = float(input("inserisci il I numero: "))
n2 = float(input("inserisci il II numero: "))
if operazione == 0:
    print(n1+n2)
elif operazione == 2:
    print(n1-n2)
elif operazione == 3:
    print(n1*n2)
else:    
    print(n1/n2) # divisione tra float
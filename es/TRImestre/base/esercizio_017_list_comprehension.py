"""     ESERCIZIO: 
Stampa tutti i numeri dispari da 0 a 1000.
e poi stampa la lista
"""
def isDispari(numero):
    conta = 2
    return (numero % conta) != 0

dispari = [k for k in range(0, 1000) if isDispari(k)] # oppure per l'if: k % 2 != 0
print(dispari) # va a capo di natura
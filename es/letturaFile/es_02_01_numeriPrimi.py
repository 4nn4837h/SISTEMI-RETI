""" ESERCIZIO: 1
Scrivi un programma Python che salvi su un file i primi 100 numeri primi, uno per ogni riga del file. 
"""
f = open("./numeriprimi.txt", "w")
def isPrimo(numero):
    conta = 2
    primo = True
    while ((conta < numero) & (primo == True)):
        if( numero % conta) == 0: 
            primo = False
        conta = conta + 1    
    return primo

# "MAIN"
n = 2 
nNum = 0;
while nNum < 100: # i primi 100 numeri, oppure da nNum = 1 --> nNum <= 100
    if isPrimo(n):
        f.write(str(n) + "\n")
        nNum += 1
    n += 1

f.close()    

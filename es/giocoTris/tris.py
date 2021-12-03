griglia = {0:' ', 1:' ', 2:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '} #chiave : valore
partitaFinita = False
Alice, Bob = "O", "X"; # nelle celle stampo direttamente i sibìmboli che usano
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

def disegnaGriglia(): # simboli: o maiuscola, e X maiuscola
    print(" {griglia[0]} | {griglia[1]} | {griglia[2]}")
    print("-----------")
    print(" {griglia[3]} | {griglia[4]} | {griglia[5]}")
    print("-----------")
    print(" {griglia[6]} | {griglia[7]} | {griglia[8]}")
    
def controlloCella(cella):
    if( griglia[cella] == ' '):
        libera = True
    else:
        libera = False  
    return libera 

def reinserimentoCella(libera):
    while (libera != True):
        cella = int(input("Inserisci di nuovo il numero della cella (0-8)"))
        libera = controlloCella(cella)
        
def chiediMossa(g):
    cella = int(input("Cella (0-8)")) # definisco la cella 
    # controllo cella libera
    libera = controlloCella(cella)
    # while se !cellaLibera
    if libera != False:
        reinserimentoCella(libera)
    else:
        griglia[cella] = g # nel valore della chiave cella ci metto il simbolo che hanno
    return cella

def vittoria():
    if(((griglia[0] != ' ') & (griglia[1] != ' ') & (griglia[2] != ' ')) or
       ((griglia[0] != ' ') & (griglia[3] != ' ') & (griglia[6] != ' ')) or
       ((griglia[3] != ' ') & (griglia[4] != ' ') & (griglia[5] != ' ')) or
       ((griglia[6] != ' ') & (griglia[7] != ' ') & (griglia[8] != ' ')) or
       ((griglia[1] != ' ') & (griglia[4] != ' ') & (griglia[7] != ' ')) or
       ((griglia[2] != ' ') & (griglia[5] != ' ') & (griglia[8] != ' ')) or
       ((griglia[0] != ' ') & (griglia[4] != ' ') & (griglia[7] != ' ')) or
       ((griglia[2] != ' ') & (griglia[4] != ' ') & (griglia[6] != ' '))):

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

#stampare la griglia
disegnaGriglia()
while (True): #!partitaFinita: -> questo lo fai solo quando la vittoria arriva
    # chiedere mossa a g1
    numCella = chiediMossa(Alice)
    
    # dopo ogni mossa diseganre la griglia --> griglia aggiornata
    disegnaGriglia()
    # controllo vittoria -> a ogni mossa
    vittoria()
    
    # chiedere mossa a g2 == chiedere i numeri
    numCella = chiediMossa(Bob)
    # controllo cella libera
    libera = controlloCella()
    # while !cellaLibera
    if libera != True:
        reinserimentoCella(libera)
        
    # dopo ogni mossa diseganre la griglia
    disegnaCella(griglia)
    # controllo vittoria -> a ogni mossa
    vittoria()
    
#LISTA DI CONFIGURAZIONI VINCENTRI, DATO CHE SONO POCHE
#AL MASSIMO TROVI ALTRE STRATEGIE
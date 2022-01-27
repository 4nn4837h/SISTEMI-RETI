""" This is my code, do not tuch it, if you'll copy it your father will hear about this!
    Simondi Francesca IV A ROB - Sistemi & Reti
WARNINGS: se clicco 0 per mettere l'indirizzo di una cella si pianta    """

def disegnaGriglia(griglia): # simboli: o maiuscola, e X maiuscola
    """Stamoa la griglia aggiornata"""
    print(f"    {griglia[0]} | {griglia[1]} | {griglia[2]}")
    print("   -----------")
    print(f"    {griglia[3]} | {griglia[4]} | {griglia[5]}")
    print("   -----------")
    print(f"    {griglia[6]} | {griglia[7]} | {griglia[8]}")
    
def reinserimentoCella(griglia, cella):
    """ permette all'utente di reinserire la cella se già occupata o se non presente"""
    while ( cella < 0 or cella > 8 ) or ( griglia[cella] != ' ' ):
        cella = int(input("Inserisci di nuovo il numero della cella (0-8)"))
    return cella
            
def controlloCella(cella, griglia):
    """ DOC STRING: controlla se la cella è già occupata da u'altra mossa"""
    libera = False
    if((cella <= 8 and cella >= 0) and griglia[cella] == ' '):
        libera = True
    while((cella < 0 or cella > 8) and libera == False):
        print("Cella non disposnibile!")
        cella = reinserimentoCella(griglia)
        if (cella <= 8 and cella >= 0) and griglia[cella] == ' ':
            libera = True
    return libera
        
def chiediMossa(g, griglia): # g = char
    """Chiede il numero della cella, controlla se la cella esiste o è libera, e la fa reinserire se necessario"""
    cella = int(input("\nCella (0-8): ")) # definisco la cella 
    # controllo cella libera
    libera = controlloCella(cella, griglia)
    # while se !cellaLibera
    if (libera != True) :
        cella = reinserimentoCella(griglia, cella)
    griglia[cella] = g # nel valore della chiave cella ci metto il simbolo che hanno: in ogni caso lo faccio

def vittoria(griglia, nomeg1, nomeg2):
    """ Trova il/la vittorios* o il pareggio, e ne stampa il risultato"""
    vitt = False
    listaCombinazioni = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    k = 0 # inizializzo l'indice per il ciclo
    while ( vitt == False and k < 8):
        tris = listaCombinazioni[k] # a tris assegno una combinazione
        if (griglia[tris[0]] == griglia[tris[1]] and griglia[tris[1]] == griglia[tris[2]] and griglia[tris[2]] != ' '): # controllo se c'è la combinazione
            vitt = True
            if griglia[tris[0]] == 'X':
                print(f"\nHa vinto il giorcatore 1: {nomeg1}!")
            else:
                print(f"\nHa vinto il giocatore 2: {nomeg2}!")
        k += 1
    return vitt 

def controlloPareggio(griglia):
    """ controlla se hanno pareggiato"""
    pieno = True
    k = 0
    while (k < 9 and pieno == True):
        if( griglia[k] == ' '): # vuoto = nessun pareggio
            pieno = False
    return pieno # che in questo caso significa: pieno = pareggio, !pieno = nessun pareggio

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

griglia = {0:' ', 1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' '} #chiave : valore
victory, pareggio = False, False
disegnaGriglia(griglia)
n1 = input("Giocatore 1: ")
n2 = input("Giocatore 2: ") # due stringhe per i nomi
giocatori = {n1:'X', n2:'O'}

while (victory == False and pareggio == False): #!partitaFinita: -> questo lo fai solo quando la vittoria arriva, se lo vuoi in loop metti while(True):
    # chiedere mossa a g1 == chiedere i numeri, fare il controllo della cella libera, reinserimento cella
    chiediMossa(giocatori[n1], griglia)
    # dopo ogni mossa diseganre la griglia --> griglia aggiornata
    disegnaGriglia(griglia)
    # controllo vittoria -> a ogni mossa
    victory = vittoria(griglia, n1, n2)
    if (victory == False): # vuol dire che non ha vinto nessuno, ma non vuol dire che non ci sia pareggio --> controllo
        if(controlloPareggio(griglia)):
            print("Nessuno ha vinto: schiappon*!")
    
    # chiedere mossa a g2 == chiedere i numeri, fare il controllo della cella libera, reinserimento cella
    chiediMossa(giocatori[n2], griglia)
    # dopo ogni mossa diseganre la griglia
    disegnaGriglia(griglia)
    # controllo vittoria -> a ogni mossa
    victory = vittoria(griglia, n1, n2)
    if (victory == False):
        pareggio = controlloPareggio(griglia)
        if(pareggio == True):
            print("Nessuno ha vinto: schiappon*!")
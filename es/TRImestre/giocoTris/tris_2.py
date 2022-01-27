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

def prendiMossa(simbolo, gr):
    cella = int(input("Numero (0 - 8): "))
    gr[cella] = simbolo
    return cella
    
def isLibera(cella, gr):
    libera = False
    if( cella >= 0 or cella <= 8):
        if ( gr[cella] == ' '):
            libera = True
    return libera

def reinserisciMossa(nome, gr):
    libera = False
    cella = int(input("Inserisci di nuovo (0 - 8):"))
    if( (cella > -1 and cella < 9) and (gr[cella] == ' ')):
        libera = True
    return libera
    
def vittoria(griglia, c1, c2):
    listaCombinazioni =[[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [2,4,6], [0,4,8]]
    vit = False
    k = 0
    while ( k < 9 and vit != True):
        tris = listaCombinazioni[k]
        if( griglia[tris[0]] == c1 and griglia[tris[1]] == c1 and griglia[tris[2]] == c1):
            vit = True
        k += 1
    return vit
def isPareggio(griglia):
    cellaPiena = True
    k = 0
    while ( k < 9 and cellaPiena):
        if(griglia[k] == ' '):
            cellaPiena = False
        k += 1
    return cellaPiena # se vera = pareggio

griglia = {0:' ', 1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' '} #chiave : valore
victory, pareggio = False, False

n1 = input("Giocatore 1: ")
n2 = input("Giocatore 2: ") # due stringhe per i nomi
giocatori = {n1:'X', n2:'O'}
disegnaGriglia(griglia)
while( victory == False and pareggio == False):
    # giocatore 1
    cella = prendiMossa(giocatori[n1], griglia)
    libera = isLibera(cella, griglia)
    while (libera == False):
       libera = reinserisciMossa(n1, griglia)
    victory = vittoria(griglia, giocatori[n1], giocatori[n2])
    if (victory == False):
        pareggio = isPareggio(griglia)
        
    # giocatore 2
    cella = prendiMossa(n2, griglia)
    libera = isLibera(cella, griglia)
    if libera == False:
        reinserisciMossa(n2, griglia)
    victory = vittoria(griglia, n1, n2)
    if victory == False:
        pareggio = isPareggio(griglia)
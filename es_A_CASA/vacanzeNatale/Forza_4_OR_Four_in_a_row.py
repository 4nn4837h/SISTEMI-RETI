def selezioneGiocatori(num_G):
    """ assegna segni e nomi ai giocatori con rispettivamente un dizionario e una lista"""
    segni_G = {}
    nomi_G = []
    while num_G > 0:
        name = input("Inserisci il nome di uno dei 2 G: ")
        if name in segni_G:
            input("Scusa, questo nome esiste già! Riprova: ")
            continue
        
        sign = input(f"Inserisci il segno di {name}: ")
        if sign in segni_G.values():
            input("Questo simbolo è già stato utilizzato! Reinseriscilo: ")
            continue
        elif len(list(sign)) != 1:
            input("Questo simbolo non può essere usato. Clicca invio, per ripartire dal tuo nome: ")
            continue
        
        segni_G[f"{name}"] = f"{sign}"
        nomi_G.append(name)
        num_G +=-1
    return segni_G, nomi_G

def board(board, NUM_COL, NUM_RIG):
    """ stampa la board / mappa / tavola / campo"""
    NUM_LIN_X_COL = 3
    SPAZI_TRA_COL = NUM_COL - 1

    cols = [cols for cols in range(1, NUM_COL + 1)] # list comprehension per le colonne a cui si appoggeranno le righe
    #print dei numeri delle colonne
    print("  ", end = "")
    for col in cols:
        print(f"{col}   ", end = "" )
    #print delle linee di divisione del campo, o mappa
    print(f"\n " + "-" * NUM_COL * NUM_LIN_X_COL + "-" * SPAZI_TRA_COL)
    
    #print del resto della board, o campo
    for rig in range(NUM_RIG):
        #print una riga di quadrati separati dalla Pipe
        for col in range(NUM_COL):
            print(f"| {board[col][rig]} ", end = "")
        print(f"|\n " + "-" * NUM_COL * NUM_LIN_X_COL + "-" * SPAZI_TRA_COL)


def isWin(board):
    """ controlla se c'è una vittoria: return bool"""
    combo = 4
    # loop for check if there is 4 signs in row, col or bevels next to each other
    for rig in range(len(board)):
        for col in range(len(board[0])):
            if rig <= len(board) - combo:
                if (board[rig][col] == board[rig+1][col] == board[rig+2][col] == board[rig+3][col]) and board[rig][col] != ' ':
                    return True

            if col <= len(board[0]) - combo:
                if (board[rig][col] == board[rig][col+1] == board[rig][col+2] == board[rig][col+3]) and board[rig][col] != ' ':
                    return True

            if col <= len(board[0]) - combo and rig <= len(board) - combo:
                if (board[rig][col] == board[rig+1][col+1] == board[rig+2][col+2] == board[rig+3][col+3]) and board[rig][col] != ' ':
                    return True

            if col >= 3 and rig <= len(board) - combo:
                if (board[rig][col] == board[rig+1][col-1] == board[rig+2][col-2] == board[rig+3][col-3]) and board[rig][col] != ' ':
                    return True
    return False

def emptySquare(board, numColonne, numRighe):
    """ controlla se la cella è vuota: return bool"""
    quadrato = board[numColonne-1][numRighe]
    return quadrato == ' '

def main():
    NUM_COL, NUM_RIG, NUM_G = 7, 6, 2
    segni, nomi = selezioneGiocatori(NUM_G)
    NUM_QUADRATI = NUM_COL * NUM_RIG
    campo = [[' '] * NUM_RIG for colonna in range(NUM_COL)]
    
    board(campo, NUM_COL, NUM_RIG)
    turno = 1

    while turno <= NUM_QUADRATI:
        # I parte: nome, segno, colonna, riga    
        giocatore = nomi[turno % nomi] # prelevo il nome del giocatore dalla lista
        segno_G = segni[giocatore] # e gli assegno il suo segno
        print(f"E' il turno di {giocatore}: ")
        nColonna = int(input("Scegli una colonna: "))
        while (nColonna >= NUM_COL) or (nColonna < 1) : # all'utente faccio inserire il numero come lo vedrebbe un bambino, non come un programmatore: parte daa 1
            colonna = campo[nColonna - 1] # parte ovviamente da 0
        while (nRiga >= NUM_COL) or (nRiga < 1):
            nRiga = int(input("Scegli una riga: "))
            riga = campo[nRiga - 1]
                
        if emptySquare(campo, nColonna, nRiga) == False: # !emptySquare(campo, nColonna, nRiga):
            input("Questa cella è piena! Ritenta: ") # se schiaccia invio lo fa continuare, in teoria
            continue
        else:
            colonna[nRiga] = segno_G
            contenutoQuadrato = segno_G
            nRiga -= 1
        
        if isWin(campo):
            print(f"{giocatore} vince!!!")
            
        turno += 1
        board(campo, NUM_COL, NUM_RIG)
    print("GAME OVER SCHIAPPE!")

if __name__ == "__main__":
    main()
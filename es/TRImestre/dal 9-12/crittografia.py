"""     ESERCIZIO: CRITTOGRAFIA
Inserire un numero per cui slittare le lettere per inserire al loro posto un altro simbolo dell'alfabeto + lo spazio
e che poi a richiesta dell'utente lo decodifichi
ARITMETICA MODULARE:
27 caratteri:a = carattere 0;
spazio == carattere 27 -> (27 + numero) % numero

queste fuori dal main sono variabili o strutture globali:
quindi tutte le funzioni vedono alfabeto, chiaviAlfabeto, MA NESSUNO PUO' MODIFICARE NULLA"""

alfabeto = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
            'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
            'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25, ' ':26}
#chiaviAlfabeto = alfabeto.keys() # lista delle chiavi -> lista di char -> dict_keys[(...)]
chiaviAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ " #print(f"{chiaviAlfabeto}") la stringa è corretta

def modifica(numero, stringa, alfabeto):
    volte = 0
    stringaModificata = "" # per inizializzarla
    for lettera in stringa:
        numeroModificato = alfabeto[lettera] # alla variabile assegno il numero che è il valore nel dizionario
        if numeroModificato <= (len(alfabeto) - numero) and volte == 0: # devo prendere anche l'ultimo carattere
            numeroModificato += numero # (de)crittografia della lettera
        else:
            indice = alfabeto[lettera]
            numeroModificato = indice + numero # faccio la somma
            if( 27 < numeroModificato): # se la somma è maggiore
                numeroModificato -= 27 # gli sottraggo la lunghezza dell'alfabeto così riparto da 0
        stringaModificata += chiaviAlfabeto[numeroModificato]
        volte += 1
    return stringaModificata

def main():
    stringa = input("Inserisci la stringa che vuoi modificare: ")
    stringa = stringa.upper() # la metto maiuscola
    stringaModificata = stringa # per inizializzarla

    cosaFare = input("Inserisci il comando che vuoi eseguire (crittografia - decodifica): ")
    while( cosaFare != "crittografia" and cosaFare != "decodifica"):
        cosaFare = input("Reinserisci il comando: ")
    
    formula = int(input("Inserire il numero che vuoi che cripti o de-cripti la tua frase: "))
    stringaModificata = modifica(formula, stringa, alfabeto)
    print(stringaModificata)

    rifare = input("Vuoi fare l'operazione inversa (s o n)?")
    if (rifare == 's' or rifare == 'S'):
        formula = formula * (-1)
        #print(formula)
        stringaRiModificata = modifica(formula, stringaModificata, alfabeto)
        print(stringaRiModificata)
    
if __name__ == "__main__":
    main()
    
""" potremmo pure fare import main"""
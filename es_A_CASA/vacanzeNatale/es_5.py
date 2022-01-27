""" 5.	
Scrivere un programma in Python che prenda in input il nome file di un programma scritto in C. 
Il programma deve leggere il file e:
    1.	Contare il numero di righe totali
    2.	Contare il numero di chiamate alla funzione “printf”
    3.	Contare il numero di linee di commento.
"""
def main():
    nomeFile = input("Inserisci il nome del file in linguaggio C: ")
    f = open("./nomeFile", "r") # lo apro in read così lo leggo
    numeroRighe, file, contaCommenti, contaPrintf = 0, f.readlines(), 0, 0

    for righe in file:  # ognicarattere nel file 
        if "printf(" in righe:
            contaPrintf += 1
        if "//" in righe:
            contaCommenti += 1
    #print(file)
    print(f"Numero di righe: " + str(numeroRighe))
    print(f"Numero di righe di commento: " + str(contaCommenti))
    print(f"Numero di chiamate della funzione printf(): " + str(contaPrintf))
    
if __name__ == "__main__":
    main()
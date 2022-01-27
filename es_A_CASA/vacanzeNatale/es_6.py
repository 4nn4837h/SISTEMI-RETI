"""6.	Il file covid-19_gen1.txt contiene la sequenza genomica RNA di un virus SARS-COV-2. 
L'RNA è una sequenza in cui si alternano 4 simboli (detti nucleotidi): A, T, C, G. L'RNA del virus SARS-COV-2 contiene 29903 nucleotidi. 
Leggi covid-19_gen1.txt il file e crea un dizionario Python avente come chiavi i nucleotidi A, T, C, G e come valori i rispettivi conteggi.
"""
f = open("./covid-19_gen1.txt", "r")
nA, nT, nC, nG = 0, 0, 0, 0
nucleotidi = {"A" : nA, "T" : nT, "C" : nC, "G" : nG}
numeroRighe, file, numeroCaratteri = 0, f.readlines(), 0

for righe in file:  # ognicarattere nel file 
    for carattere in righe:
        if carattere in nucleotidi:
            nucleotidi[carattere] += 1
        
f.close()
print(nucleotidi)
""" 7.	Il file prezzi.csv (separatore ;) contiene le serie storiche mensili dei prezzi di alcuni generi
alimentari dal Settembre 2011 a Dicembre 2016. Immagina una spesa costituita da 5 generi alimentari 
a tua scelta e crea una lista contenente la serie storica del prezzo della tua spesa ottenuta sommando i
prezzi dei generi alimentari scelti. 
Calcola mese / anno in cui la tua spesa ha costi minimi e massimi.
"""
import sys # modulo nativo con funzioni di sistema

def main():
    f = open("./prezzi.csv", "r")
    prezzo_spesa, lista_mesi = [], []
    righe = f.readlines()
    righe.pop(0) # tolgo la prima riga
    
    prodotti = []
    for i in range(5):
        prodotti.append(int(input(f"Inserire:")))
    
    for riga in righe: # riga = mese (nome - anno)
        somma = 0
        campi = riga.split(';') # prende la stringa, la spezza e ritorna una lista
        lista_mesi.append(campi[0] + ' ' + campi[1]) # stringa dell'anno e poi del mese: dal csv:anno/mese --> english cheeeck
        for prodotto in prodotti:
            somma += float(campi[prodotto]) # sono str quindi li devo castare in float
            prezzo_spesa.append(somma) # lista di tutti i prezzi, dal primo mese all'ultimo
    print(prezzo_spesa)
    print(lista_mesi)
    
    prezzoMin = 1000000
    prezzoMax= 0
    iMin, iMax = None, None # l'oggetto che non è niente -> null in C    
    
    for i, prezzo in enumerate(prezzo_spesa): # ci servono gli indici: cicliamo sugli indici di prezzo_spesa
        if prezzo < prezzoMin:
            prezzoMin = prezzo
            iMin = i
    for i, prezzo in enumerate(prezzo_spesa):
        if prezzo > prezzoMax:
            prezzoMax = prezzo
            iMax = i
    print(f"La spesa ha un prezzo minimo di €{prezzoMin:.2f} nel mese di {prezzo_spesa[iMin]}")
        
    f.close()

if __name__ == "__main__":
    main()

# Vittoria's one
""" ESERCIZIO: 2
    Scrivi un programma Python che chieda all’utente i suoi dati anagrafici (nome, cognome, data di nascita), 
    li salvi all’interno di un dizionario e infine salvi il dizionario su un file, elemento per elemento.
"""

nome = input("Inserisci il tuo nome: ")
cognome = input("Il tuo cognome: ")
gg = int(input("Giorno di nascita: "))
mm = int(input("Mese: "))
aa = int(input("Anno: "))
anagrafico = {"Nome: ": nome,  "Cognome: ": cognome, "Giorno: ": gg, "Mese: ": mm, "Anno: ": aa}

f = open("./anagrafico.txt", "w")
for chiave in anagrafico:
    #f.write(el + str(anagrafico[el]) + "\n")
    f.write(f"{anagrafico[chiave]}\n")
f.close()    
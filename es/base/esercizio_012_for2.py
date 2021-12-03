classi = ["4 A ROB", "3 A ROB", "5 B ROB", "4 A CHI", "3 A INF"]
indirizzi = {"ROB":"Smart-Robot", "CHI":"Chimica", "INF":"Informatica"}
#indice = 0
for indice, classe in enumerate(classi): # ci sono due variabili: non servono i puntatori: ogni tanti ci servirà sia l'elemento che la posizione
    #indice = indice +1
    indirizzo = indirizzi[classe[-3:]]
    print(f"posizion {indirizzo + 1} nella lista: ")
    print(f"La classe {classe} è dell'indirizzo {indirizzo}", end="\n---\n")

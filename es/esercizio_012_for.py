classi = ["4 A ROB", "3 A ROB", "5 B ROB", "4 A CHI", "3 A INF"]
indirizzi = {"ROB":"Smart-Robot", "CHI":"Chimica", "INF":"Informatica"}
for classe in classi: # scorre sugli elementi, non sugli indici, è più furbo, diciamo di C
    #print(f"La classe {classe} è dell'indirizzo {classe[-3:]}")# la variabile classe contiene il contatore
    # cosa soi riesce a fare in pyrhon? limitRE L'USO DELLE IF:
    indirizzo = indirizzi[classe[-3:]] # indicizzazione del dizionario e poi della lista
    print(f"La classe {classe} è dell'indirizzo {indirizzo}")

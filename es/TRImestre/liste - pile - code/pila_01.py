""" 
1. chiedere la stinga all'utente -> parentesi([{}])
2. ciclo sulla stringa in cui snobbate tutti i carateri tranne le parentesi
3. se ne tovo una aperta la metto nella pila -> push, chiusa -> pop dell'aperta DELLO STESSO TIPOS
"""
stringa, pilaParentesi, chiavi = input("Inserisci la frase che vuoi: "), [], [0]*3 # pilaParentesi == lista --> indici al contrario -> ultimo indice == -1
parentesiChiuse = { 0:')', 1:']', 2:'}'} # nominate per il tipo: primo "tipo", secondo e terzo "tipo" di parentesi
parentesiAperte = { 0:'(', 1:'[', 2:'{'}
count =  -1 # parte dalla prima parentesi: chiave == 1; fosse zero: KeyError: 0 -> chiave ionesistente del dizionario

for carattere in stringa:
    for k in range(0,3): # (0-2) -> estremo dx esclusi
        if carattere == parentesiAperte[k]: # così se parte dalla parentesi graffa / quadra funge
            pilaParentesi.append(carattere) # in pos -1 ci metto la parentesi
            print(pilaParentesi)
            count += 1
            chiavi[count] = k # alla chiave assegno il tipo di parentesi per poi trovare l'altra del suo stesso tipo: chiusa
            
        elif carattere == parentesiChiuse[k] and k == chiavi[count]: # se la paretesi è dello stesso tipo dell'ultima
            pilaParentesi.pop(-1) # tolgo ovviamente l'ultima, ovvero carattere
            count -= 1
            print(f"Rimossa la simmetrica di: " + str(carattere)) # e la stampo        
        
        #else: print("!!!Errore con le parentesi!!!")  

# {ciao s(ono Fr[ancesca] Simondi)}
# {h(e[i])}
# {(hello} --> errore
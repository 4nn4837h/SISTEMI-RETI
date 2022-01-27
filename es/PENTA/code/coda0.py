""" sulle code si opera sia dalla testa che dalla coda:
coda: inserimento
head: expires

head -> [1, 2, 3, 4] <- tail

pass ==> comando che non fa nulla: utile per un codice complesso:
mentre scrivi il tuo coice in maniera incrementale tu ci metti pass, così quando vuoi eseguire funge
"""

def enqueue(coda, elemento):
    coda.append(elemento)
    
def dequeue(coda):
    if len(coda) > 0: return coda.pop(0)
    else: return None

def main():
    coda, coda2, risp = [], [], ''
    while risp == 's' or risp == 'S':
        num = int(input("Inserisci il numero che vuoi inserire: "))
        enqueue(coda, num)
        risp = input(" Inserisci il carattere s se vuoi inserire altri elementi: ")
    print(coda)

"""     elemento = dequeue(coda)
while elemento != None:
    print(elemento)
    elemento = dequeue(coda)    """

if __name__ == "__main__":
    main()

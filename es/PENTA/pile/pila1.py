""" Scrivere un programma che legga una sequenza di caratteri e li stampi in ordine inverso, usa una pila"""

def push(pila, elemento):
    pila.append(elemento)
    
def pop(pila):
    return pila.pop()

pilaDaNonUsare = ["ciao", "sono", "Arataki", "Itto"]
pila, pila2, risp = [], [], ''

while risp == 's' or risp == 'S':
    num = int(input("Inserisci il numero che vuoi inserire: "))
    push(pila, num)
    risp = input(" Inserisci il carattere s se vuoi inserire altri elementi: ")

for _ in range(len(pila)):
    push(pila2, pop(pila)) # quello che tolgo dalla pila arriva alla pila2
print(pila2)

elemento = pop(pila)
while elemento != None:
    print(elemento)
    elemento = pop(pila)



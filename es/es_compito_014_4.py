"""     ESERCIZIO 4: 
Scrivi un programma in Python che permetta all’utente di inserire due numeri qualsiasi. 
Crea una lista contenente:
1. la somma dei quadrati dei due numeri;
2. il quadrato della somma dei numeri;
3. la differenza tra i quadrati dei due numeri;
4. la differenza tra i numeri al quadrato.
Stampa la lista ottenuta.
"""
int1 = int(input("Inserisci il I numero: "))
int2 = int(input("Inserisci il II numero: "))
lista = [int1**2 + int2**2]
lista.append((int1 + int2)**2)
lista.append(int1**2 - int2**2)
lista.append((int1 - int2)**2)
print(f"{lista[0]} - {lista[1]} - {lista[2]} - {lista[3]}")
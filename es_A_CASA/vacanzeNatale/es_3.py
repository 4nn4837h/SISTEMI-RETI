"""3.	Scrivere un programma che data una lista ne stampi una sua permutazione casuale."""
import random, itertools

def main():
    lista = ["Venti", "Xiangling", "Arataki Itto", 394, 42]
    casuale, lista2 = [], list(itertools.permutations(lista)) # list = costruttore della lista
    
    while len(lista) != len(casuale):
        num = random.choice(lista)
        if num not in casuale:
            casuale.append(num)
            
if __name__ == "__main__":
    main()

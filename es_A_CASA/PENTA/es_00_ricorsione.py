"""1)Scrivere una funzione Python ricorsiva che permetta di calcolare il fattoriale di un numero intero. """

def fattoriale(n): 
    if(n == 0): return 1
    else: return n* fattoriale(n - 1)

def main():
    n = int(input("inserisci il numero di cui vuoi che si calcoli il fattoriale: "))
    print(f"Il fattoriale di {n} vale: {fattoriale(n)}")
    
if __name__ == "__main__":
    main()
"""2)Scrivere una funzione Python ricorsiva che permetta di stampare i numeri di Fibonacci minori di un valore scelto dall'utente. 

The First 10 Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
sommo il primo e il precedente"""

sequenza = [] # globale: man mano cresce con la serie di Fibonacci
# se fosse nella funzione: sarebbe sbagliato, perché lo ri-inizializzerebbe ogni volta che si richiama
def fibonacci(num, ultimo, penultimo): # numero dato, poi come altro attributo: quello che viene dopo
    fibo = ultimo + penultimo  # quello della funzione
    if fibo < num:
        sequenza.append(fibo)
        fibonacci(num, fibo, ultimo)
    else: return sequenza[-2] # devo stampare il penultimo perché l'ultimo è già maggiore del numero dato dall'utente

def fibonacci2(n):
        if n <= 1:
            return 1
        else: return fibonacci2(n - 1) + fibonacci2(n - 2) # richiama nella stessa funzione 2 volte se stessa

def main():
    numeroDato = int(input("Inserire il numero che non di vuole superare con la sequenza di Fibonacci: "))
     # passo il numero da non superare, si parte dall'1
    print(f"L'ultimo numero della serie di Fibonacci minore di {numeroDato} è questa: {fibonacci(numeroDato, 1, 1)}")
    numeroDiVolteFibonacci = int(input("Inserire il numero di volte che calcoli la sequenza di Fibonacci: "))
    fibonacci2(numeroDiVolteFibonacci)
    
if __name__ == "__main__":
    main()

# C:\Users\paola\Documents\SCUOLA\FRANCY\IV\SISTEMI E RETI\Python\es_A_CASA\PENTA
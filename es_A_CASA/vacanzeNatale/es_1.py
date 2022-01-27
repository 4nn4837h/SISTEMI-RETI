"""
1. Scrivere un programma che data una lista qualsiasi ne elimini i
duplicati.
"""
import antigravity

def main():
    listaQualsiasi = [1, 6, 3, 5, 7, 3, 5, 6]
    lista2 = []
    for k in listaQualsiasi:
        if k not in lista2: # ecco il booleano: ci dice se k è o no in lista2
            lista2.append(k)
    print(lista2)
    
if __name__ == "__main__":
    main()

def main():
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    dizionario = {x : elemento for x, elemento in enumerate(lista)}
    print(dizionario) # dictionnary comprehension

if __name__ == "__main__":
    main()
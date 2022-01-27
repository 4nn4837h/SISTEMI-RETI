"""     Chiedi all'alunno nome e voto di condotta
poi crea un file csv e salva per ogni riga: nome - voto di condotta
per motivi di privacy il nome deve essere la prima lettera e gli altri tutti asterischi
"""
continua = True
f = open("file.csv", "w")

def main():
    while(continua):
        nome = input("Inserisci il tuo nome: ")
        iniziale = nome[0]
        numeroAsterischi = len(nome) - 1
        voto = float(input("Inserisci il voto in condotta: "))

        f.write("Nome: " + iniziale + numeroAsterischi*"*" + " - Voto di condotta: " + str(voto) + "\n")
        #f.write(f"Nome: {iniziale} {numeroAsterischi* "*"} - Voto di condotta: {str(voto)} \n")
        lettera = str(input("Vuoi inserire il tuo nome? (S - N): ")) # vuole continuare con l'inserimento dei nomi?
        if(lettera == "S" or lettera == "s" ):
            continua = True # vuole continuare -> continua il ciclo
        else: 
            continua = False # non vuole continuare -> esce dal ciclo
f.close()

if __name__ == "__main__":
    main()
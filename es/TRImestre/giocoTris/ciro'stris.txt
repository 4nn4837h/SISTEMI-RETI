#made by Coppola
def stampaGriglia(g):
    k=0
    for k in range(3):
        print(f"{griglia[k*3]}|{griglia[k*3+1]}|{griglia[k*3+2]}")
        print("-----")

def controlloVittoria(g, car):
    comb=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    trov=False
    k=0
    while(trov==False and k < 8):
        tris=comb[k]
        if(g[tris[0]]==car and g[tris[1]]==car and g[tris[2]]==car):
            trov=True
        k+=1
    return trov

def controlloPareggio(g):
    pareggio=True
    k=0
    while(pareggio ==True and k <9):
        if(g[k]== " "):
            pareggio=False
        k+=1
    return pareggio

def isLibera(cella, g):
    ok=False
    if(cella >= 0 and cella <= 8):
        if(g[cella]==" "):
            ok = True
    return ok

griglia={0:" ", 1:" ", 2 :" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",}
partitaFinita=False
car1="X"
car2="0"
stampaGriglia(griglia)
while(partitaFinita==False):
    mossag1=int(input("Giocatore 1 dammi la mossa(0-8): ")) #chiedere mossa g1
    while(isLibera(mossag1, griglia)==False):  #verifica cella libera
        print("Cella già occupata!!\n")
        mossag1=int(input("Giocatore 1 dammi la mossa(0-8): "))
    griglia[mossag1]=car1
    stampaGriglia(griglia)#stampa griglia
    if(controlloVittoria(griglia, car1)):    #controlla Vittoria
        print("Complinti, il g1 ha vinto!!!")
        partitaFinita=True
    elif(controlloPareggio(griglia)):
            print("Pareggio!!!")
            partitaFinita=True
    else:
        mossag2=int(input("Giocatore 2 dammi la mossa(0-8): ")) #chiedere mossa g2
        while(isLibera(mossag2, griglia)==False):  #verifica cella libera
            print("Cella già occupata!!\n")
            mossag2=int(input("Giocatore 1 dammi la mossa(0-8): "))
        griglia[mossag2]=car2
        stampaGriglia(griglia)#stampa griglia
        if(controlloVittoria(griglia, car2)):    #controlla Vittoria
            print("Complinti, il g2 ha vinto!!!")
            partitaFinita=True
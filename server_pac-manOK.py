#------------------------------------------------------------------------------------------------------------------------- server del gioco Microbit
import socket, random, sys, queue, time, serial
from threading import Thread
import pygame as pg
from pygame.locals import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # lo metto come variabile globale in modo che tutti lo possano vedere
q = queue.Queue()
q2=queue.Queue() # non serve metterle nel pacman perché globale

black = 0, 0, 0
dt, gamma = 3, 0.05
#pg configuration
width = 800
height = 800
pg.init()                                        # parte subito la schermata di gioco
screen = pg.display.set_mode((width, height))
pg.display.set_caption("PAC-MAN!!!")
clock = pg.time.Clock()
pacman = pg.image.load("pacmanChiuso-pacman.png")
ghost = pg.image.load("ghost1-pacman.png")
#pacmanRect = pg.transform.scale(pacman,(50, 50))
floor = pg.image.load("pavimento-pacman.png")
wall = pg.image.load("muro-pacman.png") # immagini del pavimento e del muro
button_a1=False
button_b1=False
button_a2=False
button_b2=False

class Receiver(Thread):
    def __init__(self):
        # costruttore del thread
        Thread.__init__(self)
        self.s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # inizializzazione del socket: in ipv4 e in protocllo TCP
        self.s.bind(("172.20.10.2", 8000))                        # la bind del socket, per cercare il seconod nodo
        self.s.listen()                                              # ricerca II nodo
        self.connection, self.address = self.s.accept()                # accettazione del nodo
        self.running = True

    def run(self):
        """Funzione usata per la lettura dei dati"""
        while self.running:
            dati = ""
            dati = self.connection.recv(4096)                          # ricezione dati dopo l'inizializzazine della variabile str
            dati = dati.decode()
            global button_a2
            global button_b2                                           # rendo globali i bottoni del secondo microbit
            if "aT" in dati:
                button_a2=True
            else:
                button_a2=False
            if "bT" in dati:
                button_b2=True
            else:
                button_b2=False                                        # prendo i "comandi" di microbit e li butto nelle globali
            time.sleep(0.1)  

    def terminate(self):
        """Funzione per la terminazione del Lavoro del Thread"""
        self.running = False

#---------------------------------------------------------------------------------------------------------------------------
def setSpawn(matrice,dim):
    """ lo spawn delle figure nella matrice"""
    x, y = 0, 0
    while matrice[y][x] != 0 and y < dim:                # dentro la matrice in senso verticale
        while matrice[y][x] != 0 and x < dim:            # dentro la matrice in senso orizzontale
            x += 1
        x = 0
        y += 1
    return x, y

def getAdiacenze(mappa,dim):
    """ la funzione che ovviamente crea il dizionario delle adiacenze: tutte le celle che la cella ha vicino"""
    Movimenti={}
    for i,k in enumerate(mappa):
        for i2, j in enumerate(k):
            if j == 1:
                Movimenti[i,i2] = "Muro"                              # come dati ho messo delle str: muro == movimento non possibile
            else:
                Movimenti[i,i2] = ""                                  # se il movimento è possibile: bisogna capire quale
                if i > 0:
                    if mappa[i-1][i2] == 0:
                        Movimenti[i,i2] = Movimenti[i,i2] + "sopra "  # movimenti possibili
                if i < dim-1:
                    if mappa[i+1][i2] == 0:
                        Movimenti[i,i2]=Movimenti[i,i2] + "sotto "
                if i2 > 0:
                    if mappa[i][i2-1] == 0:
                        Movimenti[i,i2]=Movimenti[i,i2] + "sinistra "
                if i2 < dim-1:
                    if mappa[i][i2+1] == 0:
                        Movimenti[i,i2]=Movimenti[i,i2] + "destra "
    return Movimenti

def creaMappa(dim):
    """ crea la mappa appunto con le immagini al posto degli zero e degli 1"""
    floorRect = pg.transform.scale(floor,(width/dim, height/dim))
    wallRect = pg.transform.scale(wall,(width/dim, height/dim))
    mat, matImg = [[0]*dim for _ in range(dim)], [[wallRect]*dim for _ in range(dim)] 
    for k in range(dim):
        for j in range(dim):
            x = random.choice([0,0,0,0,0,0,0,1,1])
            mat[k][j] = x
            if mat[k][j] == 1: 
                matImg[k][j] = wallRect
            else: 
                matImg[k][j] = floorRect
    return matImg,mat # mappa sottoforma di matrice di adiacenze pg.Surface e di mappa con 0 e 1

def disegnaCampo(mat, dim):
    """ disegna effettivamente la mappa sullo schermo di pygame"""
    x, y = 0, 0
    for y,riga in enumerate(mat):
        for x,cella in enumerate(riga):
            screen.blit(cella, (x*(width/dim), y*(height/dim)))    # stampa la cella: muro o pavimento che sia
        pg.display.update()

def generaFrutti(mat, dim):
    """ generatore di frutta nel campo """
    frutto = pg.image.load("frutto.png").convert_alpha()
    frutto = pg.transform.scale(frutto, (width/dim/2, height/dim/2))
    frutto_rect = frutto.get_rect()                                    # effettiva immagine del frutto
    for _ in range(dim * 2):                                           # i frutti devono essere molti: ecco perché dim * 2 (dim == 20)
        x, y = random.randint(0, dim-1),random.randint(0, dim-1)
        while mat[y][x] != 0:                                          # se non è muro
            x, y = random.randint(0, dim-1),random.randint(0, dim-1)
        frutto_rect.center = (x*width/dim + (width/dim)/2, y*height/dim + (height/dim)/2)
        screen.blit(frutto,frutto_rect)
#------------------------------------------------------------

class Read_Microbit(Thread):
    """ classe che legge i dati di microbit"""
    def __init__(self):
        Thread.__init__(self)
        self._running = True
      
    def terminate(self):
        self._running = False
        
    def run(self):                                          # qui letteralmente prende i dati e li mette nella queue
        #serial config
        port = "COM13"
        s = serial.Serial(port)
        s.baudrate = 115200                                 # inizializza porta e socket
        while self._running:
            dati = ""
            dati =  s.readline().decode() 
            global button_a1
            global button_b1                                           # rendo globali i bottoni del secondo microbit
            if "aT" in dati:
                button_a1=True
            else:
                button_a1=False
            if "bT" in dati:
                button_b1=True
            else:
                button_b1=False
            time.sleep(0.1)  
            """try: 
                data = s.readline().decode() 
                print(data)
                acc = [float(x) for x in data[1:3].split(" ")] # aT
                q.put(acc)
            except:
                print("errore di ricezione")
            time.sleep(0.01)"""
        
#------------------------------------------------------------

class Ghost(object):
    """ classe dei fantasmi """
    def __init__(self,dim,adiacenze,matrice):
        self.ghost = pg.transform.scale(ghost,(width/dim-2, height/dim-2)).convert_alpha()
        self.ghost_rect = ghost.get_rect()                                                 # immagine reale dei fantasmi
        self.speed = (1,0)
        self.dizMovSin = {(1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1), (0,1):(1,0)}
        self.dizMovDes = {(1,0):(0,1), (0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0)}             # come pacman hanno una rotazione di 90 gradi
        self.x,self.y = setSpawn(matrice, dim)                                              # utilizzo la funzione che mi la spawnare correttamente
        self.adiacenze = adiacenze                                                         # dove si può effettivamente spostare
        self.ghost_rect.center = (self.x*(width/dim), self.y*(height/dim))
        self.dim = dim

    def move(self):
        """ il movimento che vado a a fargli fare"""
        floorRect = pg.transform.scale(floor,(width/self.dim, height/self.dim))
        dizScelte = {1 : self.dizMovSin[self.speed], 2 : self.dizMovDes[self.speed], 3 : self.speed, 4 : (-self.speed[0],-self.speed[1])}
        self.speed = dizScelte[random.randint(1,3)]
        mosso = True                                                              # essendo un movimento di un ghost lo faccio random
        while mosso:
            if self.speed == (1,0) and "destra" in self.adiacenze[self.y, self.x]: # controllo di come si può muovere e di come muoversi eventualmente
                self.x += self.speed[0]
                self.y += self.speed[1]                                           # grazie al dizionario posso farlo muovere automaticamente
                mosso = False                                                     # senzasommare cose srane qui negli if
                screen.blit(floorRect,self.ghost_rect.center)                     # ristampo il floor: non vedo più il ghost precedente
                self.ghost_rect = self.ghost_rect.move((self.speed[0] * (width/self.dim)), (self.speed[1] * (height/self.dim))) # ricorsione
            elif self.speed == (0,-1) and "sopra" in self.adiacenze[self.y, self.x]:
                self.x += self.speed[0]
                self.y += self.speed[1]
                mosso = False
                screen.blit(floorRect, self.ghost_rect.center)
                self.ghost_rect = self.ghost_rect.move((self.speed[0] * (width/self.dim)), (self.speed[1] * (height/self.dim)))
            elif self.speed == (-1,0) and "sinistra" in self.adiacenze[self.y,self.x]:
                self.x += self.speed[0]
                self.y += self.speed[1]
                mosso = False
                screen.blit(floorRect, self.ghost_rect.center)
                self.ghost_rect = self.ghost_rect.move((self.speed[0] * (width/self.dim)), (self.speed[1] * (height/self.dim)))
            elif self.speed == (0,1) and "sotto" in self.adiacenze[self.y, self.x]:
                self.x += self.speed[0]
                self.y += self.speed[1]
                mosso = False
                screen.blit(floorRect, self.ghost_rect.center)
                self.ghost_rect = self.ghost_rect.move((self.speed[0] * (width/self.dim)), (self.speed[1] * (height/self.dim)))
            else:
                self.speed = dizScelte[random.randint(1, 4)]
        screen.blit(self.ghost, self.ghost_rect.center)

#--------------------------------------------------------------------------------------------------------------------

class PacMan(object):
    """ l'agognata classe per il pac-man"""
    def __init__(self,dim,adiacenze,matrice,coda):
        self.pacman = pg.transform.scale(pacman,(width/dim-2,height/dim-2)).convert_alpha()
        self.pacmanDefault = pg.transform.scale(pacman,(width/dim-2,height/dim-2)).convert_alpha()
        self.pacmanRect = pacman.get_rect()
        self.speed =(1,0)
        self.dizMovSin = {(1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1), (0,1):(1,0)}  # faccio sempre dei dizionari per evitare tutte le if dopo
        self.dizMovDes = {(1,0):(0,1), (0,1):(-1,0), (-1,0):(0,-1), (0,-1):(1,0)}
        self.angolo = {(1,0):180, (0,-1):-90, (0,1):90, (-1,0):0}                  # angolo di rotazione
        self.x,self.y = setSpawn(matrice,dim)
        self.adiacenze = adiacenze
        self.pacmanRect.center = (self.x*(width/dim) + (width/dim)/2, self.y*(height/dim) + (height/dim)/2)
        self.dim = dim
        self.q = coda

    def move(self):
        """ il movimento che io passo al microbit selezionando i tasti opportuni """
        floorRect = pg.transform.scale(floor,(width/self.dim, height/self.dim))
        data = ""
        if not(self.q.empty()):
            data = self.q.get()
        dizScelte = {"a":self.dizMovSin[self.speed], "b":self.dizMovDes[self.speed],"":self.speed}
        self.speed = dizScelte[data]
        if self.speed == (1,0) and "destra" in self.adiacenze[self.y,self.x]:
            self.x += self.speed[0]
            self.y += self.speed[1]
            screen.blit(floorRect,self.pacmanRect)            # al passaggio del pacman ovviamente si rimette il pavimento per non vedere i pacman "del passatp" == delle celle precedenti
            self.pacmanRect = self.pacmanRect.move((self.speed[0] * width/self.dim), (self.speed[1] * height/self.dim))
        elif self.speed == (0,-1) and "sopra" in self.adiacenze[self.y, self.x]:
            self.x += self.speed[0]
            self.y += self.speed[1]
            screen.blit(floorRect,self.pacmanRect)
            self.pacmanRect = self.pacmanRect.move((self.speed[0]*width/self.dim), (self.speed[1]*height/self.dim))
        elif self.speed == (-1,0) and "sinistra" in self.adiacenze[self.y, self.x]:
            self.x += self.speed[0]
            self.y += self.speed[1]
            screen.blit(floorRect, self.pacmanRect)
            self.pacmanRect = self.pacmanRect.move((self.speed[0] * width/self.dim), (self.speed[1] * height/self.dim))
        elif self.speed == (0,1) and "sotto" in self.adiacenze[self.y, self.x]:
            self.x += self.speed[0]
            self.y += self.speed[1]
            screen.blit(floorRect,self.pacmanRect)
            self.pacmanRect = self.pacmanRect.move((self.speed[0] * width/self.dim), (self.speed[1] * height/self.dim))
        self.pacman  =pg.transform.rotate(self.pacmanDefault, self.angolo[self.speed])
        screen.blit(self.pacman, self.pacmanRect)

def main():
    running = True
    rm = Read_Microbit()
    rm.start()            # il thread per leggere il microbit
    rc = Receiver()
    rc.start()            # l socket client che riceve praticamente i dati dal server
    dim = 30
    mappa, matrice = creaMappa(dim) # creiamo la mappa del gioco, che ogni volta è casuale
    global pacman
    pacman = pg.transform.scale(pacman,(width/dim-2, height/dim-2)).convert_alpha()
    screen.fill(black)
    disegnaCampo(mappa, dim)
    generaFrutti(matrice,dim)
    adiacenze = (getAdiacenze(matrice,dim))                      # mi salvo il dizionario delle adiacenze
    nGhost = 8
    ghost = [Ghost(dim,adiacenze, matrice) for _ in range(nGhost)]
    player1 = PacMan(dim, adiacenze, matrice, q)
    player2 = PacMan(dim, adiacenze, matrice, q2)                # ovviamente ogni pacman è un thread
    pg.display.flip()                                            # aggiorno lo schermo
    time.sleep(0.02)
    global button_a1
    global button_b1
    global button_a2
    global button_b2
    while running:                                               # l'attributo della classe
        for g in ghost:
            g.move()                                             # faccio muovere i fantasmi per sempre
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
            """if event.type == pg.KEYDOWN:
                if event.__dict__["unicode"]=="a":
                    q.put("a")
                    q2.put("d")
                if event.__dict__["unicode"]=="d" :
                    q.put("d")
                    q2.put("a")"""
        if button_a1:
            q.put("a")
        if button_b1:
            q.put("b")
        if button_a2:
            q2.put("a")
        if button_b2:
            q2.put("b")  
        player1.move()                                           # dopo aver preso i comandi in inout da microbit
        player2.move()                                           # posso farli spostare
        pg.display.flip()
        clock.tick(10)
        time.sleep(0.2)
    rm.join()
    rc.join()
    rm.terminate()
    rc.terminate()
    
    
if __name__ == "__main__":
    main()
    
#   C:\Users\paola\Documents\SCUOLA\FRANCY\IV\SISTEMI E RETI\Python\es\PENTA\MICROBIT\pac_man

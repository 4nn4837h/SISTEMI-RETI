import turtle
snowFlake = turtle.Turtle()
finestra = turtle.Screen()
snowFlake.color("white")
finestra.bgcolor("RoyalBlue1")
snowFlake.speed(500)

f = open("./snowFlake.txt", "w") # apro in scrittura

def avantiIndietro():
    f.write("forward:" + str(30) + "\n")
    snowFlake.forward(30)
    f.write("backward:" + str(30) + "\n")
    snowFlake.backward(30)

def rametto():
    f.write("forward:" + str(120) + "\n")
    snowFlake.forward(120) # punta centrale
    f.write("backward:" + str(30) + "\n")
    snowFlake.backward(30)
    for _ in range(3):
        f.write("right:" + str(45) + "\n")
        snowFlake.right(45) # punta a dx
        avantiIndietro()
        f.write("left:" + str(90) + "\n")
        snowFlake.left(90) # punta a sx
        avantiIndietro()
        f.write("right: " + str(45) + "\n")
        snowFlake.right(45) # torna dritto
        f.write("backward:" + str(30) + "\n")
        snowFlake.backward(30)

for _ in range(8): # da 0 a 7
    rametto() # disegna il rametto dello snowFlake
    f.write("right: " + str(45) + "\n")
    snowFlake.right(45) # gira di 45 gradi

f.close() # chiudo == salvo

f = open("./snowFlake.txt", "r") # lo riapro in lettura

#righe = []
righe = f.readlines() # lista di stringhe
#rigaSplittata = []
for riga in righe:
    rigaSplittata = riga.split(":")
    print(rigaSplittata)

f.close()    

finestra.exitonclick() # azione bloccante (click del mouse sblocca)
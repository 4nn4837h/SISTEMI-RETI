""" Classe stella per disegnarle in turtle: 
3 attributi: che non istanziamo ma li usiamo quando ci servono
x, y, dimensione
metodi:
inzit, disegna stella"""

import random, turtle
penna = turtle.Turtle() # globali
cielo = turtle.Screen()
cielo.bgcolor("Blue")

class Stella(object):
    def __init__(self, x, y, dim):
        self.x = x
        self.y = y
        self.dim = dim
        
    def disegna(self):
        penna.penup()
        penna.goto(self.x, self.y)
        penna.pendown()
        for _ in range(0, 5):
            penna.forward(self.dim)
            penna.right(144)
    
def main():
    for _ in range(0, 50):
        star = Stella(random.randint(-300, 300), random.randint(-300, 300), random.randint(10, 60))
        star.disegna()    
    
if __name__ == "__main__":
    main()
""" 3)Scrivere un programma in Python nel quale utilizzando il modulo turtle: 
- sia presente una funzione che disegni una stella nelle coordinate x e y (passate come parametri alla funzione) 
- disegni 50 stelle sullo screen posizionate in posizioni casuali."""

import turtle, random

penna = turtle.Turtle()
schermo = turtle.Screen()

def stella(x, y, dim):
    penna.penup()
    penna.goto(x, y)
    penna.pendown()
    for _ in range(0, 5):
        penna.forward(dim)
        penna.right(144)

def main():
    for _ in range(0, 50):
        stella(random.randint(-480, 480), random.randint(-480, 480), random.randint(10, 60))
    schermo.exitonclick()
    
    
if __name__ == "__main__":
    main()


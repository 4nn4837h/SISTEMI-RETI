"""ESERCIZIO: 5
Scrivi un programma in Python che chieda all'utente un numero intero n. 
Il programma deve creare una lista contente due diverse turtle, orientate in direzioni opposte. 
Ciascuna turtle disegna poi il poligono regolare a n lati.
"""
import turtle
figura = turtle.Turtle()
figura2 = turtle.Turtle()
schermo = turtle.Screen()

def disegnaFigura (n, figura, volta):
    """ Disegna la figura che vuole l'utente, con n lati"""
    while n <= 0:
        n = int(input("RE-inserisci il numero: "))
        
    k = 0
    if volta == 1:
        figura.goto(10, 10)
        while k < n:
            figura.forward(50)
            figura.right(360 / n)
    else:
        while k < n:
            figura.goto(50, 50)
            figura.forward(50)
            figura.left(360 / n)
    
numero = int(input("Inserisci un numero a tua scelta: "))
listaTurtle = [disegnaFigura(numero, figura, 1), disegnaFigura(numero, figura2, 2)]
schermo.exitonclick()


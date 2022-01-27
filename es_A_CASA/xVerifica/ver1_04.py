"""ESERCIZIO: 4
Scrivi un programma in Python che chieda all'utente un numero intero n e disegni, tramite turtle, il poligono regolare a n lati. 
"""
import turtle
figura = turtle.Turtle()
schermo = turtle.Screen()

n = int(input("Inserisci un numero a tua scelta: "))
while n <= 0:
    n = int(input("RE-inserisci il numero: "))

k = 0
while k < n:
    figura.forward(50)
    figura.right(360 / n)

schermo.exitonclick()
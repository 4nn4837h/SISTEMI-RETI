""" esercizio: prendi comandi del file turtle e poi riscrivili splittati"""
import turtle
snowFlake = turtle.Turtle()
finestra = turtle.Screen()
f = open("./snowFlake.txt", "w") # apro in scrittura
righe = f.readline() # lista di righe
f.close()

file = open("./snowFlake.txt", "r") # apro in scrittura
for riga in righe:
    comando = riga.split(":")
    valore = comando[1]
    if(comando[0] == ""):
        go = comando[1].split(",")
        

file.close()
""" ESERCIZIO: 3
Creare una lambda function che ritorni True se una stringa è palindroma, False altrimenti. 
"""
palindroma = lambda stringa : (stringa == stringa[::-1]) # come s'inverte una stringa si inverte anche una lista
print(palindroma("anna"))
print(palindroma("anno"))
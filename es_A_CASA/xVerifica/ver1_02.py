"""ESERCIZIO: 2 
Utilizzando il modulo random (https://docs.python.org/3/library/random.html),
simula dieci lanci di un dado per Alice e dieci lanci di un dado per Bob, mediante list comprehension.
Il dado è a sei facce. Salva i lanci all’interno di un file, su dieci righe,
in cui la prima colonna corrisponde ai lanci di Alice e la seconda a quelli di Bob.
Utilizza la virgole come separatore all’interno delle righe.    
"""
#Random seed
#from random import randint, seed
import random

random.seed(1)
Alice = [ random.randint(1, 6) for _ in range(1, 10)] # estremi inclusi
random.seed(2)
Bob = [ random.randint(1, 6) for _ in range(1, 10)]

f = open("./ver1_02.txt", "w")
for i in range(9):
    print(f"Alice: " + str(Alice[i]) + ",Bob: " + str(Bob[i]))
    f.write("Alice: " + str(Alice[i]) + ",Bob: " + str(Bob[i]) + "\n")
f.close()
# dato che non vediamo i tipi delle variabili chiamarle in modo specifico e chiaro, anche con nomi lunghi#
nome = input("Dimmi il tuo nome: ")
#anni = int(input("Dimmi quanti anni hai: "))
#print(f"Tu ti chiami {nome}, e hai {anni} anni!")
""" i caratteri di una stringa si possono indicizzare in due modi:
C    I    A   O
0    1    2   3
-4  -3   -2  -1"""

print(f"Il tuo nome inizia con la lettera {nome[0]}! E finisce con la lettera {nome[-1]}")
print(f"La penultima lettera del tuo nome è {nome[-2]}")
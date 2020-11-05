#Exercice 29 : Faire un programme python indiquant si le nombre d’éléments égaux à un d’une séquence d’entiers binaires est pair ou non.

a = [0,1,0,1,1,0,0,1]
compteur = 0

import random

liste = [random.randint(0, 1)for i in range (0,50)] # liste en compréhension

nombreDeUn = liste.count(1)

if nombreDeUn % 2 == 0:
    print("pair")
else:
    print("impair")
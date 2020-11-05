#Exercice 28 : Faire un programme python retournant le nombre d’éléments égaux à 0 d’une séquence d’entiers binaires donnée.

a = [0,1,0,1,1,0,0]

compteur = 0

for i in a:
    if i == 0:
        compteur += 1

def count(liste, element):
    for valeur in liste :
        if valeur == element:
            compteur += 1
    return compteur

print(compteur, a.count(0))
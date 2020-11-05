#Exercice 23 : Faire un programme python qui demande à un utilisateur un entier. Le programme fait la somme des carrées des entiers compris en 1 et la valeur donnée.

a = float( input("Tapez un nombre réel :"))

print("le carré du nombre réel :", a , "est", a**2 )

a = int(input("entier :"))
somme = 0

for nombre in range(0, a+1):
    somme += (nombre ** 2)



print(somme)

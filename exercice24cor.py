#Exercice 24 : Faire la somme et la multiplication des 100 premiers entier positifs. Affichez les résultats.

somme = 0
somme2 = 1

for i in range(1,101): # le nombre 101 n'est pas compris
    somme += i
    somme2 *= i

print(somme)








nombre = 1
somme += nombre # += > somme = nombre + somme

nombre = 2
somme += nombre

nombre = 3
somme += nombre
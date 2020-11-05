#Exercice 19 : Faire un programme python qui demande un nombre réel à un utilisateur. A partir de ce nombre en faire la racine carrée.


from math import sqrt
a = float( input("Tapez un nombre réel :"))

print("la racine carrée du nombre réel :" , a , "est:", sqrt(a))



a = int(input("tapez un nombre réel :"))

a = a ** (1 /2)

print(a)
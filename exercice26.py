#Exercice 26 : Faire un programme python avec un affichage formaté. Pour cela vous utilisez la fonction .format(). Avec .format() faire afficher 30 étoiles sur une ligne et 2 chiffre après virgule du nombre 34.30480.

etoiles = "{0}".format("*" * 30)
chiffres = 34.30480


formaté = "{0: .2f}".format(chiffres)

print(etoiles,formaté)
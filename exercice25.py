#Exercice 25 : Faire un programme python qui demande à un utilisateur d’entrer un entier positif. Le programme indique ensuite si l’entier positif est pair ou impair ? Le programme vérifie et redemande l’entier si ce n’est pas un entier positif.

txt = int(input("veuillez entrer un entier positif :"))
while txt < 0 :
    txt2 = int(input("Cette entier est négatif,veuillez entrer un entier positif :"))
    if txt2 % 2 == 0 :
        print("pair")
    else :
        print("impair")
else :
    if txt % 2 == 0 :
        print("pair")
    else :
        print("impair")



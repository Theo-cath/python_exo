#Exercice 20 : Faire un programme python qui fait le tri de 3 entiers donnés.

a = [8,6,9]

print(a)

aa = sorted(a)

print(aa)


a = int(input("a"))
b = int(input("b"))
c = int(input("c"))

d = [a, b, c]

d.sort() #Possibilité de passer reverse = True en paramètre

print(d)
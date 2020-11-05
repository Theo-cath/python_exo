# Exercice 6: Faire la saisie d’un entier qui sera une durée en secondes. Faire les instructions pour convertit cette valeur en heures, minutes, secondes. 


a = int(input(r"entrer une valeur en secondes :"))

h = a//3600
minutes = (a % 3600)//60 
s = (a % 3600) % 60

print(h,"heures",minutes,"minutes et",s,"secondes")
 
 



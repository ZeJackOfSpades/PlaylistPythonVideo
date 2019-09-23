#coding:utf-8

"""
Opérateur en Python : +   (addition)
									-   (soustraction)
									*   (multiplication)
									/   (division)
									% (modulo) -> reste d'une division Euclidienne
									
									
variable = variable +X
variable += X

variable = variable - X
variable -= X

variable = variable * X 
variable *= X
"""

niveauPersonnage = int(input("Niveau de départ ") )
print("Niveau de personnage", niveauPersonnage)

niveauPersonnage += 1
print("Niveau de personnage", niveauPersonnage)


calcul = 5 / 2
calcul = int(calcul)
calculDeux = int(5 % 2)

print("Résultat =", calcul, "reste :", calculDeux)

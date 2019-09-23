#coding:utf-8

"""
(!) Tuple	:	conteneur imuable (dont on ne peut modifier les valeurs)

Création de tuple	:	monTuple	=	()			#vide
									monTuple	=	17,		#une seule valeur
									monTuple	=	(17,)	#une seule valeur
									monTuple	=	(4, 6)	#Plusieurs valeurs

Accès aux valeurs	:	monTuple[X]				#valeur d'indice X

Z raisons d'utiliser les tuples	:	affectation multiple de variable
														retour multiple de fonction
"""

def getPlayerPosition():
	posX	=	148
	posY	=	86
	
	return (posX, posY)

#Programme principal

(nombre1, nombre2)	=	(14, 72)

liste	=	[1, 2, 3, 4, 5, 6, 7]
coordX	=	0
coordY	=	0

print("Position du joueur : ({}/{})".format(coordX, coordY))
(coordX, coordY)	=	getPlayerPosition()
print("Position du joueur : ({}/{})".format(coordX, coordY))

for chose in enumerate(liste):
	print(chose)

monTuple	=	(45, 56)						#tuple avec une virgule apres l'€ ou 45, sans les parenthèses
print(monTuple)

print(monTuple[1])




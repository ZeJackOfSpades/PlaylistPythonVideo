#coding:utf-8
import os
import copy
"""
	inventaire[:2]					#affichage des 2 premier €
	inventaire[2:]					#affichage des 2 dernier €
	inventaire[-3]					#affichage du dernier - 3 €
	inventaire[1]					#affichage du n ième €
	inventaire[:]						#affichage de tous les €
	inventaire[2:4]					#affichage de l'€ 2 au 4 ième € (fourchette de valeur)
	inventaire.index("aze")	#renvoi l'indice de "aze"
	
	len(<list>) 						#retourne le nombre d'€
	Attention :
	si liste1	=	liste2	on fait un clone et qui sont relié sinon on import copy pour cloner et mettre
	a 2 endroit différent dans la mémoire donc indépendante l'une de l'autre
"""
#Créaton d'une liste
inventaire					=	[0]*10	#	ou list()
inventaireObjet			=	["arc"]*10
inventaireCroissant	=	range(20) # insertion de 0 à 19
inventaireJeu				=	["arc", "epée", "bouclier", "potion", "flèches", "pagne"]
inventaire2					=	[]
inventaireJeuCopie	=	copy.deepcopy(inventaireJeu)


os.system("clear")

inventaireObjet.extend(inventaireJeuCopie)	#ou inventaireObjet	+=	inventaireJeuCopie  pas de référence entres elles

chaine			=	"Bonjour à tous"
chaineListe	=		["Bonjour", "à", "tous"]
phrase	=	"_".join(chaineListe)
print(phrase)

i	=	0
#inventaireJeu[2:3]	=	["BOUCLIERRRRR"]	*	3
if "Bouclier" in inventaireJeu:
	print("Bouclier")
else:
	print("No shield")


inventaire2.append("Arc")
inventaire2.insert(2,"Potion de mana")
print(inventaire2)
inventaire2.remove("Potion de mana")		#ou del inventaire2[1]
print(inventaire2)

inventaireJeu.sort()										#ATTENTION accents ! ordre Alphabetique
print(inventaireJeu[:])
inventaireJeu.reverse()									#ATTENTION accents ! ordre inverse Alphabétique
print(inventaireJeu[:])

print("Nombre d'arc :", inventaireJeu.count("arc"))

inventaireObjet.clear()									#vide la liste ou inventaire[:]	=	[]

chaine	=	chaine.split(" ")
print(chaine)


"""
while i < len(inventaireCroissant):	#première méthode de parcours de liste
	print(inventaireCroissant[i])
	i	+=	1

for	valeur	in	inventaireCroissant:	#Deuxième méthode de parcours de liste, on pourra rajouter enumerateavant inventaire pour créer un tuple
	print(valeur)
	
#Affichage Listes
print(inventaire)
print(inventaireObjet)
print(inventaireCroissant)
print(inventaireJeu)
"""





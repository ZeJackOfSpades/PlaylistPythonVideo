#coding:utf-8

""" Video 3
Nommer une variable : doit commencer par une lettre
									ne pas contenir de caractères spéciaux
									ne pas contenir d'espaces
									utiliser des underscores (_)
									
Types standards		 : entier numérique (int)
								   nombre flottant (float)
								   chaîne de caractères (str)
								   booléen (bool)
								   
Fonctions vues : print()  	  -> afficher à l'écran
						  input()      -> lire au clavier
						  type() 	  -> retourne le type d'une donnée, variable, etc
						  int(), float(), str(), bool() -> "caster" une donnée
						  str.format -> formater une chaine
"""

agePersonne = 22
prixHT = 120.46
agePersonneDeux = "42"
continuerPartie = False
#nomJoueur = input("Choisissez un nom de joueur :")
prixHT = int(input("Entrez un prix HT : "))
prixTTC = prixHT + (prixHT *20 / 100)
print("Prix TTC =", prixTTC)

#print("Bienvenue,",nomJoueur)

"""
texte = "L'Age de la personne est {} et le prix HT est de {}€"
print(texte.format(agePersonne,prixHT)) 

print(type(agePersonne))
print(type(agePersonneDeux))

print("Age de la personne :", agePersonne, ".")
"""

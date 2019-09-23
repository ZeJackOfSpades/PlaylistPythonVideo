#coding:utf-8
import os

"""
	Fonctions utiles	:
		isinstance(<objet>, <classe>)	:	vérifie qu'un objet est de la
																classe renseignée
		
		issubclass(>classe_fille>, <classe_mere>)	:	vérifie qu'une classe est 
																						fille d'une autre
"""
class Vehicule:

	def __init__(self, nom, quantiteEssence):
		self.nom						=	nom
		self.quantiteEssence	=	quantiteEssence

	def deplacement(self):
		print("Déplacement...")
	
	

#Classe Fille
class Voiture(Vehicule):	#Voiture hérite de la classe mère Vehicule
	def __init__(self, nomVoiture, Essence, puissance):
		Vehicule.__init__(self, nomVoiture, Essence)			#Appel de l'ancien constructeur
		self.puissance	=	puissance
	
class Avion(Vehicule):
	def __init__(self, nom, essence, marchandise):
		Vehicule.__init__(self, nom, essence)
		self.marchandise	=	marchandise
	def deplacement(self):
		print("Je roule")
	
class Animal:
	def __init__(self,nom):
		self.nom	=	nom
	def manger(self):
		print(self.nom, "mange...")

class Reptile(Animal):
	def __init__(self, nom, regimeAlimentaire):
		Animal.__init__(self, nom)
		self.regime = regimeAlimentaire
#main
os.system("clear")
#voiture1		=	Vehicule("B2 ", 2400)
#print(v1.nom)
#voitureV2	=	Voiture("Mythos", 90, 420)
#voitureV2.deplacement()
#print(voitureV2.puissance)
#avion			=	Avion("Rafale", 9000, 16000)
#avion.deplacement()
lezard	=	Reptile("Lezard", "grenouille")
if isinstance(lezard, Animal):
	print("Lézard est un Animal")


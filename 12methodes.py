#coding:utf-8

import os

"""
Méthode					:	fonction d'une classe sur une instance (objet)
Méthode de classe	:	fonction d'une classe 
Méthode statique		:	fonction indépendante mais "lié" à une classe
"""

class Humain:
	"""Classe qui définit un humain"""
	lieu_habitation = "Terre"
	
	def __init__(self, nom, age):
		self.nom	=	nom
		self.age	=	age
	
	def identification(self):
		print("nom : {}, age : {}".format(self.nom, self.age))
	
	def parler(self, message):
		print("{} a dit : {}\n".format(self.nom, message))
	
	def getNom(self):
		return self.nom
	
	def setNom(self, nom):
		self.nom = nom
	
	def changerPlanete(cls, newPlanete): 	# cls : méthode de classe
		Humain.lieu_habitation = newPlanete
	changer_planete = classmethod(changerPlanete) #je définis la méthode changerPlanete comme une méthode de classe
																				 #De plus je change son nom : changer_planete
	def definition():
		print("L'Humain est classé comme étant le plus haut...")
	
	definition = staticmethod(definition)
#Programme principal
os.system("clear")
h1	=	Humain("Jason", 26)
h1.identification()
h1.parler("Ceci est un test")

print("Planète actuelle : {}".format(Humain.lieu_habitation))
Humain.changer_planete("Mars")
print("Planète actuelle : {}".format(Humain.lieu_habitation))

Humain.definition()
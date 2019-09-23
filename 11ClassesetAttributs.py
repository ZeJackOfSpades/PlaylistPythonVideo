#coding:utf-8

import os

class Humain:
	"""
	Classe des êtres humains
	"""
	humainsCrees = 0
	
	
	def __init__(self, c_prenom, c_age=0): #constructueur de la classe
		print("Création d'un humain")
		self.prenom = c_prenom
		self.age = c_age
		Humain.humainsCrees += 1 #attribut de classe donc Classe.variable
		
os.system("clear")
print("\nTest\n")

oJack	= Humain("Jack", 22) #appel de la classe et donc son constructeur
print("Prénom de oJack => {}".format(oJack.prenom))
print("Age de oJack => {}".format(oJack.age))

oPhilou	= Humain("Philou", 53)
print("Prénom de oPhilou => {}".format(oPhilou.prenom))
print("Age de oPhilou => {}".format(oPhilou.age))

print("Humain existants : {}".format(Humain.humainsCrees))


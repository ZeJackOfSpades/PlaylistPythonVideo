#coding:utf-8

import os
"""
Propriété	:	manière de manipuler/contrôler des attributs
					principe d'encapsulation	!
"""

class Humain:
	"""Cette clase représente un humain"""
	
	def __init__(self, nom, age):
		print("Création d'un humain...")
		self.nom	=	nom						#_ devant le nom de l'attribu indique qu'il ne faut pas le modifier sans accesseur
		self._age	=	age
	
	def _getAge(self):

		if self._age <= 1:
			#return "{} {}".format(self._age, "an")	# OK
			return str(self._age) + " an"
		else:
			#return "{} {}".format(self._age, "ans")	#OK 
			return str(self._age) + " ans"

	#	property (<getter>, <setter>, <deleter>, <helper>)
	#age	=	property(_getAge, _setAge, _delAge, "Je suis l'age d'un humain")
	age = property(_getAge)
#Programme principal
os.system("clear")
h1	=	Humain ("Jason", 2)

print("{} a {} ".format(h1.nom ,h1.age))

#help(Humain)		#help permet d'afficher  le message du helper


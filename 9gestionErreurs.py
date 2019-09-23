#coding:utf-8
import os
"""
Gérer les exceptions	:	try/except (+else, finally)

Types d'exceptions 		:	ValueError
										NameError
										ZeroDivisionError
										OSError
										AssertionError
"""
os.system("clear")

ageUtilisateur = input("Quel âge as-tu ? ")
try:
	ageUtilisateur = int(ageUtilisateur)
except:
	print("L'âge indiqué est incorrect !")
else:
	print("Tu as", ageUtilisateur, "ans")
finally: # dans tout les cas
	print("Fin programme...")

###############################################

nombre1 = 150 
nombre2 = input("Choisir le nombre pour diviser : ")
try:
	nombre2 = int(nombre2)
except ZeroDivisionError:
	print("0 !!!!!!!!!!")
except ValueError:
	print("Veuillez rentrez un nombre !")
except:
	print("Valeur incorrecte.")
else: #si les valeurs sont bonnes
	print("Resultat = {}".format(nombre1 / nombre2))
finally:
	print("Fin programme...") 
"""
#################################################"
"""
try:
	age = input("Veuillez rentrer votre age ")
	age = int(age)
	if age < 25:
		raise ZeroDivisionError("Coucou :) !")
except ZeroDivisionError:
	print("Catched")

#################################################"
try:
	age = input("Veuillez rentrer votre age ")
	age = int(age)
	
	assert age > 25 #Je veux que age soit plus grand que 25
except AssertionError:
	print("J'ai attrapé l'exception")

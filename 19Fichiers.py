#coding:utf-8
import os
import pickle
"""
Modes d'ouvertures	:	r	(lecture seule)
										w (écriture avec remplacement)
										a  (écriture avec ajout en fin de fichier)
										x  (lecture et écriture)
										r+ (lecture/écriture dans un même fichier)
										
Lecture						:	read(), readline(), readlines()		#renvoie des chaînes de caractères	
Ecriture						:	write()

"""
os.system("clear")
class Player:
	def __init__(self, name, level):
		self.name	=	name
		self.level	=	level
	
	def whoami(self):
		print(self.name, self.level)

p1	=	Player("Jack", 10)
p1.whoami()

with open("19Player.data", "rb") as fichierB:
	#record	=	pickle.Pickler(fichierB)			#en mode ecriture Binaire ici je spécifie où j'enregistre
	getRecord	=	pickle.Unpickler(fichierB)
	#record.dump(p1)										#en mode ecriture Binaire ici j'enregistre l'enregistrement de mon objet (ici)
	player_one	=	getRecord.load()
	
player_one.whoami()
#fic			=	open("19donnees.txt", "r")
with	open("19donnees.txt", "w")	as fic:
	nombre	=	15
	fic.write(str(nombre))
	fic.write("\nTests")
	#content	=	fic.read()
"""
line			=	fic.readline()
print(line)
line			=	fic.readline()
print(line)
line			=	fic.readline()
print(line)
lines		=	fic.readlines()
print(lines)
"""
#fic.close()			#pas besoin de fermer le fichier avec with open ...as <nom_de_variable>

if fic.close:
	print("Fichier fermé")
else:	
	print("Fichier encore ouvert")
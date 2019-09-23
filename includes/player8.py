#coding:utf-8

"""
Module pour le joueur
"""

def parler(personnage, message):
	print("{} : {} ".format(personnage, message))
	
def au_revoir():
	print("Bye")
	
	
if __name__ == "__main__": #zone de test de son module
	print("PHASE DE TEST DE PLAYER8.PY")
	parler("Jason", "Ceci est une test")
	au_revoir()
	
	
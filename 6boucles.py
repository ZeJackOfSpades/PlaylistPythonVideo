#coding:utf-8

"""
Pour les variable de boucle :
PAS de i++ or ++i
 i += 1
 
 Boucles		: while /for
 Mots-clés	: break (casse la coucle) / continue (revient au début de la boucle)
"""
jeuLance = True
compteur = 0
phrase = "bonjour tout le monde :) !"

for letter in phrase:
	print (letter)

"""
while compteur < 5:
	print("Test phrase") 
	compteur += 1

print("Sortie de boucle")
"""
while jeuLance:
	choixMenu = input("> ")
	
	if choixMenu == "again":
		continue
	
	elif choixMenu == "quit":
		#break
		jeuLance = False
	else:
		print("UNKNOWN")
print("Sortie de boucle")


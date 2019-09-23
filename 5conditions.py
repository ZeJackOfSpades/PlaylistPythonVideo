#coding:utf-8

"""
Opérateur de comparaison :  == (égal à)
											 != (différent de)
											 < (plus petit que)
											 > (plus grand que)
											 <= (plus petit ou égal à)
											 >= (plus grand ou égal à)

Mots clés des conditions : if / elif / else
											 
Condition multiples 			  : and (ET)
											or (OU)
											in / not in  (DANS  / PAS DANS)
"""

"""
jeuCharge = True # True == vrai == 1

if jeuCharge:
	print("Le jeu est en marche")
else:
	print("Le jeu a été quitté")

age = 24

if age == 18:
	print("Majorité")
elif age == 24:
	print("COUCOU")
else:
	print("Tu as", age, "ans")
"""
age = input("Quel âge as-tu ? ")
age =int(age)

if 0 < age <= 100 :  #age > 0 and age <= 100
	print("oui")
else:
	print("vieux non ?")


lettre ="b"

if lettre not in "aeiouy":
	print("C'est une consonne")
else:
	print("C'est une voyelle")

identifiant =  "Jason"
motDePasse = "password123"

print("Interface de connexion")

userID = input("Entrez votre identifiant : ")
userPassword = input ("Entrez votre mot de passe : ")

if userID == identifiant and userPassword == motDePasse :
	print("Vous êtes connectés, bienvenue", userID)
else :
	print("INCORRECT\n")
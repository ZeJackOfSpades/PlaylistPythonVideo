#coding:utf-8

"""
Fonction vues	:	print(), input()
							type(), int(), float() ,str(), bool()
							
age = input("Quel age as-tu ? ")
age = int(age)

print("Bonjour à tous ! :)")
print("Tu as {] ans.".format(age))
"""
ttc =lambda prixHT: prixHT  + (prixHT *20 / 100)

print(ttc(24))

def dire_bonjour():
	print("Bonjour à tous ! :)")
#Fin fonction

def dire(nomPersonne = "Jack", messagePersonne = "Default"):
	print("{} : {}".format(nomPersonne,messagePersonne))

def showInventory(*ListItems): # *ListItems permet de dire un nombre variable de params
	for item in ListItems:
		print(item)
	#fin fonction showInventory

def calculerSomme(nombre1, nombre2):
	return nombre1+nombre2
	#fin fonction calculerSomme

dire("Jason")
dire(messagePersonne = "Yo bro !!!")

showInventory("épée")
showInventory("épée", "arc", "potion de mana", "cape du Dragon rouge")


print(calculerSomme(6,16))



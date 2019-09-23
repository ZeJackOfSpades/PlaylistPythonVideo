#coding:utf-8
import os
"""
Création de dictionnaire	:	dico	=	{}			#Vide
												dico	=	{<cle>:<valeur>, <cle2>:<valeur2>}

Accès à une valeur			:	dico[<cle>]

Ajout et modification			:	dico[<cle>]	=	<valeur>					

Suppression						:	dico.pop(<cle>)		#on peut également sotcker ce qu'on a supprimé dans une variable
												del dico[<cle>]

Copie de dictionnaire		:	dico1	=	{1:11, 2:22}
												dico2	=	dico1.copie()
												(!) La copie crée une référence (dico1	=	dico2) si on souhaite 
												faire un clone on utilisera .copy()
												
"""
os.system("clear")

def maFonctionBizarre(**parametres):		#passage en paramètre de dictionnaire
	print(parametres)
	
maFonctionBizarre(age=14, nom="Jojo")	


dico	=	{"prénom":"Jason"}
dico2	=	{1:"Jack"}

print(dico["prénom"])
print(dico2[1])												#J'accède a l'€ qui a la clef 1

dico["chien"]	=	"C'est le chien de Jason"	#Si l'€ existe déjà il sera remplacé
print(dico)

dico.pop("chien")
print(dico)

for key, val in dico.items():
	print(key, val)

#print(dico["ok"])


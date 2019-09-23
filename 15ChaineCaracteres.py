#coding:utf-8

#	Classe str	:	string(chaîne de caractères) help(str) si besoin
"""
Une méthode dde chaîne travaille sur une copie, et pas sur la chaîne elle-même.


str.upper(), str.lower(), str.capitalize() #majuscule au premier mot, str.title()
str.center(<largeur>, <caractere_remplissage>)
str.strip() #enlève les espaces sauf si espace après un caractere 

str.fing(<chaine>, {<debut>, <fin>})
str.index(<chaine>, {<debut>, <fin>}) #lève une erreur si il ne trouve pas la chaîne
str.replace(<ancienne>, <nouvelle>,{<occurences>})

str.isalpha(), str.isdigit(), str.isdecimal(), str.isnumeric()
str.isalnum

str.islower
"""

maChaine	=	"Bonjour tout le monde"
ch1	=	"MonSuperProgramme"
ch2	=	ch1
phrase	=	"Magicien|10|5"

print(phrase.split("|"))


#print(ch1)
#print(ch2)
#ch1	=	ch1.center(50,"-")
#print(ch1.find("Super"))

#print(ch1)
#print(ch2)
#print(maChaine)

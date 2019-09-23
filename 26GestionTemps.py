#coding:utf-8

import time




"""			
			  localtime()
(TIMESTAMP) --------------> structure de temps
			<-------------
			    mktime()

###############################################
%d 	:	jour(01 à 31)
%m 	:	mois(01 à 12)
%Y	:	année(ex : 2018)- %y (00 à 99)
%H	:	heures (00 à 23)
%I 	:	minues (00 à 59)
%S 	:	secondes (00 à 59)
%p 	:	AM/PM

%A 	:	jour semaine / %a (jour abrégé)
%B 	:	mois / %b (mois abrégé)

%Z	:	fuseau horaire (timezone)	
"""

"""
print("Test1")
time.sleep(5)
print("Test2")
"""
"""
begin	=	time.time()

print("Début")

time.sleep(5)

end		=	time.time()
print("Fin")

print(f"Temps exécuté : {end - begin}s")
"""
Vtime	=	time.localtime()
myTime	=	time.strftime("%Y-%m-%d")
print(Vtime)
print(myTime)



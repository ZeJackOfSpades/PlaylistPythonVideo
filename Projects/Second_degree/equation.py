#coding:utf-8

from math import *			#For sqrt function and other if it needed
from cmath import *			#For complex part
import os							#For terminal commands

"""
Coding second equation degree
"""
os.system("clear")

#----------------------------------------------------------------------------------------
#								VARIABLE DECLARATION
#----------------------------------------------------------------------------------------
deltaSup0	=	"Delta={}\nX1={}\nX2={}" 	#Displaying format for delta > 0
deltaEqu0	=	"Delta={}\nX={}\n"			#Displaying format for delta = 0
deltaInf0	=	"Delta={}\nZ1={}\nZ2={}"	#Displaying format for delta < 0
aZero		=	"X={}\n"

#----------------------------------------------------------------------------------------
#								
#----------------------------------------------------------------------------------------
print("EQUATION DU SECOND DEGREE\n")

try:
	a = float(input("Rentrez la valeur de a: "))
	b = float(input("Rentrez la valeur de b: "))
	c = float(input("Rentrez la valeur de c: "))
	
except ValueError:
	print("Valeur(s) inccorectes !!!\n")

else:

	delta = (b**2) - (4*a*c)

	if a ==0 :
		X = -c / b
		print(aZero.format(X))
	else:
		if delta > 0 :
			x1 = (-b + sqrt(delta)) / (2*a)
			x2 = (-b - sqrt(delta)) / (2*a)
			
			print(deltaSup0.format(delta, x1, x2))
			
		elif delta == 0:
			zeroX = (-b )/ (2*a)
			
			print(deltaEqu0.format(delta,zeroX))

		else:
			Z1 = (-b + 1j *sqrt(-delta))/(2*a)
			Z2 = (-b + 1j *sqrt(-delta))/(2*a)
			
			print(deltaInf0.format(delta, Z1, Z2))
			
print("\nFin de programme !!!\n")





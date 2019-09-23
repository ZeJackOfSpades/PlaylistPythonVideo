#coding:utf-8
"""﻿
	FILE NAME	:	IHMSecondaryEquation.py
	DESCRIPTION :	This file is a program wich can calculate all the solutions 
					for a secondary equation


	Auteur		: 	J. Monnier
	Date 		:	03/12/2018


	VERSIONS	:	1.0			First version of the HMI, capable to calculate all the solutions for the secondary equation
					1.1			Add the Checkbutton to save or not in the file all the results
					1.2			Add the popups to know if we have saved in the file or not
					1.3			Add the information button messagebox <lisez-moi>
					1.4			Add the option to see the look of fonction 
					1.4.1		Add the option of the nomber of points for the ploting method
					1.4.2		Add the default value of varXmax set at 10 
					1.4.3		Add the default value of varPointsGraph set at 50
					1.5			Add Image for tests
					1.6			Change the placement of the widget by grid (prior pack()) for functionFrame
					1.6.5		Change the placement of the widget by grid (prior pack()) for coefFrame 
					1.7.0		Add the basics exceptions for the groups of display window and coefficiens window
					1.7.1		The main window is no longer resizable
					1.7.5		Add the time when the results are saved in the file
			
"""

import os
import tkinter
import pickle
import datetime
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageTk
from math import *
from tkinter import messagebox

version 	=	"1.7.5"


deltaSup0	=	"Delta={}\nX1={}\nX2={}\n" 	#Displaying format for delta > 0
deltaEqu0	=	"Delta={}\nX={}\n"			#Displaying format for delta = 0
deltaInf0	=	"Delta={}\nZ1={}\nZ2={}\n"	#Displaying format for delta < 0
aZero		=	"Delta={}\nX={}\n"


def p(x,a,b,c):
    #return x**4 - 4*x**2 + 3*x
    return (a)*x**2 + (b)*x + (c)


def calculation(*args):
	"""
        calculation is a fonction which is called when the buttun calculation is pushed
 		this function is able to calculate the <delta> and solutions depending on delta

        :param a: 
        :param b: 
        :type a: 
        :type b: 
        :return: nothing
        :rtype: 
 
        :Example:
 
        .. seealso:: 
        .. warning:: The function is linked by all the variable tkinter names mainly 3 Entry and 1 Label
        			 The function calls also enregistrementFichier to save the results in a file
        .. note:: this function does not work if the variables in your HMI have not the same name
        .. todo:: 
    """
	try:
		a			=	varAEquation.get()
		b			=	varBEquation.get()
		c    		=	varCEquation.get()
	except Exception as e:
		messagebox.showerror("Problèmes datas", "ATTENTION certains coefficiens sont INCORRECT !!!")
	else:
		coefficiensLabels	= "a = {} ; b = {} ; c = {}\n".format(a,b,c)
		separationTexte		="-------------------------------------------\n"

		print(a, b, c)
		delta = (b**2) - (4*a*c)
		if a ==0 and b ==0:
			textResults.set("Delta = {}, Fonction constante : Solution = {}\n".format(delta, c))
			resultat = textResults.get()

		elif a ==0 :
			X = -c / b
			textResults.set(aZero.format(delta,X))
			resultat = textResults.get()
		else:
			if delta > 0 :
				x1 = (-b + sqrt(delta)) / (2*a)
				x2 = (-b - sqrt(delta)) / (2*a)
				
				textResults.set(deltaSup0.format(delta, x1, x2))
				resultat = textResults.get()

			elif delta == 0:
				zeroX = (-b )/ (2*a)
				
				textResults.set(deltaEqu0.format(delta,zeroX))
				resultat = textResults.get()

			else:
				#Z1R = (-b + 1j *sqrt(-delta))/(2*a)
				ZR	=-b / (2*a)
				ZC	=sqrt(-delta)/(2*a)

				Z1 	= "{} +j {}".format(ZR, ZC)
				Z2 	= "{} -j {}".format(ZR, ZC)	
				textResults.set(deltaInf0.format(delta, Z1, Z2))
				resultat = textResults.get()
		enregistrementFichier("saveDatas.txt", coefficiensLabels, resultat, separationTexte,fileBoxValue.get())


"""
def valueCheck(valueToBeChecked):
	value =	valueToBeChecked
"""
def enregistrementFichier(nomFichier, coefficiensLabels, texteLabel, separationTexte, autorisationEnregistrement):
	"""
        enregistrementFichier can save the results from your HMI (tkinter) in the file in append mode
 		And now the date is recorded in the file
        :param nomFichier: the name and the extention of the file where you want to save your results
        :param coefficiensLabels: it is the combination of the 3 coefficiens used during the process of the calculation
        :param texteLabel: The results a the end of the calculation
        :param separationTexte: many dashes to saperate the datas in the file
        :param autorisationEnregistrement: No or Yes to save the file

        :type nomFichier: string
        :type coefficiensLabels: string
        :type texteLabel: string
        :type separationTexte: string
        :type autorisationEnregistrement: bool
        
        :return: nothing
        :rtype: 
 
        :Example:

 
        .. seealso:: calculation()
        .. warning:: This function is linked to calculation()
        			 you must use it
        .. note:: this is the first version of the function
        .. todo:: 
    """
	if autorisationEnregistrement:
		with open(nomFichier,"a") as fichierTexte:
			Dnow	=	datetime.datetime.now()
			Date 	= "\nDate : {}\n".format(Dnow)
			fichierTexte.write(coefficiensLabels)
			fichierTexte.write(texteLabel)
			fichierTexte.write(Date)
			fichierTexte.write(separationTexte)

		messagebox.showinfo("INFORMATIONS","Sauvegardé dans le fichier {}".format(nomFichier))
	else:
		messagebox.showwarning("WARNING","Vous n'avez pas sauvegardé dans le fichier !")

def information(*args):
	information = (	"Application développé par la M Team\n\n" 
					"Cette application vous permet de calculer les solutions d'un polynome du 2nd degré\n"
					"et d'enregistrer le résultat dans un fichier\n"
					"Vous pouvez également voir la fonction en précisant les valeurs de l'axe X et du nombre de points pour la courbe\n"
					"\nVersion {}".format(version))
	messagebox.showinfo("Lisez-moi",information)


def affichageFonction(*args):
	try:
		a			=	varAEquation.get()
		b			=	varBEquation.get()
		c    		=	varCEquation.get()
	except Exception as e:
		messagebox.showerror("Problème coefficiens", "ATTENTION certains coefficiens sont INCORRECTS !!!")
	else:
		try:
			xMin 		= 	varXmin.get()
			xMax 		= 	varXmax.get()
			nbPoints	=	varPointsGraph.get()
		except Exception as e:
			messagebox.showerror("Problème Paramètres Affichage Fonction",
								 "ATTENTION certains Paramètres \npour l'affichage"
								 "de votre fonction sont INCORRECTS !!!")
		else:
			X 			= np.linspace(xMin, xMax, nbPoints, endpoint=False)
			F 			= p(X,a,b,c)
			plt.plot(X,F)
			#plt.title()
			plt.show()
		finally:
			pass
		


#----------------------------------------------------------------------------------------
#										MAIN				
#----------------------------------------------------------------------------------------
mainApp				=	tkinter.Tk()
#mainApp.geometry("840x320")
#mainApp.minsize(width=1080, height= 300)
mainApp.resizable(False, False)
mainApp.title("Secondary Equation Resolution")

#variables
textResults			=	tkinter.StringVar()

image 				=	Image.open("/home/user/Images/tontonFlingeursBD.jpg")
photo				=	ImageTk.PhotoImage(image)

labelImage 			=	tkinter.Label(image=photo)
labelImage.image 	=	photo

#creation LabelFrame
coefFrame			=	tkinter.LabelFrame(mainApp,text="Coefficiens A, B, C")
coefFrame.pack(expand=1,fill="both", side="left")

functionFrame		=	tkinter.LabelFrame(mainApp,text="Affichage fonction")
functionFrame.pack(expand=1,fill="both", side="right")

#creation widgets
#Entry
varAEquation		=	tkinter.DoubleVar()
aEquation			=	tkinter.Entry(coefFrame, text="a", textvariable=varAEquation)

varBEquation		=	tkinter.DoubleVar()					
bEquation			=	tkinter.Entry(coefFrame, textvariable=varBEquation)

varCEquation		=	tkinter.DoubleVar()
cEquation			=	tkinter.Entry(coefFrame, textvariable=varCEquation)

varXmax				=	tkinter.DoubleVar()
varXmax.set(10)
entryXmax			=	tkinter.Entry(functionFrame, textvariable=varXmax)

varXmin				=	tkinter.DoubleVar()
entryXmin			=	tkinter.Entry(functionFrame, textvariable=varXmin)

varPointsGraph		=	tkinter.IntVar()
varPointsGraph.set(50)
entryPointsGraph	=	tkinter.Entry(functionFrame, textvariable=varPointsGraph)

#checkbutton
fileBoxValue		=	tkinter.BooleanVar()
fileBox				=	tkinter.Checkbutton(coefFrame, text="Enregistrer le résultat dans un fichier", selectcolor="yellow", variable=fileBoxValue, offvalue = 0, onvalue=1)

#Buttons
infoButton			=	tkinter.Button(coefFrame, text="INFO", command=information)
calculButton		=	tkinter.Button(coefFrame, text="Calculate", command=calculation)
quiButton			=	tkinter.Button(coefFrame, text="QUITTER", command =	mainApp.destroy)

functionButton		=	tkinter.Button(functionFrame, text="Affichage fonction", command=affichageFonction)

#labels
labelCoefA			=	tkinter.Label(coefFrame, text="a")
labelCoefB			=	tkinter.Label(coefFrame, text="b")
labelCoefC			=	tkinter.Label(coefFrame, text="c")
labelResults		=	tkinter.Label(coefFrame, textvariable=textResults)


labelXmin			=	tkinter.Label(functionFrame, text="xmin")
labelXmax			=	tkinter.Label(functionFrame, text="xmax")
labelNbPointsCourbe	=	tkinter.Label(functionFrame, text="nbPointsCourbe")

print("valeur de fileBox = {}".format(fileBoxValue))
#Affichage des widgets
fileBox.grid(row=0,column=0,columnspan=5)

labelCoefA.grid(row=1,column=0,columnspan=1)
aEquation.grid(row=1,column=1)

labelCoefB.grid(row=2,column=0,columnspan=1)
bEquation.grid(row=2,column=1)

labelCoefC.grid(row=3,column=0,columnspan=1)
cEquation.grid(row=3,column=1)

labelResults.grid(row=4,column=0,columnspan=8)

calculButton.grid(row=6,column=1, sticky="nesw")
infoButton.grid(row=7,column=1, sticky="nesw")
labelImage.pack()
quiButton.grid(row=9,column=1, sticky="nesw")


#Affichage fonction part
labelXmin.grid(row=0, column=0)
entryXmin.grid(row=0, column=1,columnspan=2)
labelXmax.grid(row=1, column=0)
entryXmax.grid(row=1, column=1,columnspan=2)

labelNbPointsCourbe.grid(row=2, column=0)
entryPointsGraph.grid(row=2, column=1,columnspan=2)


functionButton.grid(row=4, columnspan=4, sticky="nesw")
mainApp.mainloop() 


#if __name__=="__main__":
#	help(enregistrementFichier)

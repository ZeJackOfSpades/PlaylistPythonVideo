#coding:utf-8
import tkinter
import os
from tkinter import messagebox
os.system("clear")
"""
StringVar()		:	chaine de caractères [str]
IntVar()		:	nombre entier [int]
DoubleVar()		:	nombre flottant [float]
BooleanVar()	:	booléen [bool]
"""
#Observateur
def updateLabel(*args):
	varLabel.set(varEntry.get())
	

def updateObserver(*args):
	#print(f"J'ai vu: {varGender.get()}") #f ici permet de dire varGender.get() est une fonction
	if varGender.get():
		varLabelGender.set("C'est un homme")
	else:
		varLabelGender.set("C'est une femme")

mainApp				=	tkinter.Tk()
mainApp.geometry("400x300")
mainApp.title("Variables tkinter")

# Widgets...
varGender			=	tkinter.IntVar()
varGender.trace("w", updateObserver)
radio1				=	tkinter.Radiobutton(mainApp, text="Homme", value=1, variable=varGender)
radio2				=	tkinter.Radiobutton(mainApp, text="Femme", value=0, variable=varGender)

varLabelGender		=	tkinter.StringVar()
labelGender			=	tkinter.Label(mainApp, textvariable=varLabelGender)



radio1.pack()
radio2.pack()
labelGender.pack()
"""
varEntry	=	tkinter.StringVar()
varEntry.trace("w", updateLabel)
entry		=	tkinter.Entry(mainApp, textvariable=varEntry)

varLabel	=	tkinter.StringVar()
label		=	tkinter.Label(mainApp, width=20, text="", textvariable=varLabel)
varLabel.set("coucou")
print("Label:", varLabel.get())

entry.pack()
label.pack()
"""
mainApp.mainloop()
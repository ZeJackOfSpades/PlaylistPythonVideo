#coding:utf-8

import os
import tkinter
from tkinter import messagebox
os.system("clear")
"""
showerror
showinfo
showwarning
askquestion
askokcancel
askyesno
askretrycancel
"""
def showModalWindow():
	messagebox.showerror("ERREUR", "Un problème est survenu !")

mainApp	=	tkinter.Tk()
btn		=	tkinter.Button(mainApp, text="Déclancer une erreur", command=showModalWindow)
#scaleW	=	tkinter.Scale(mainApp, from_= 10, to = 50)#, tickinterval=25)

#spinW			=	tkinter.Spinbox(mainApp, from_=1, to=10)
#checkWidget	=	tkinter.Checkbutton(mainApp, text=" Publier ?", offvalue = 2, onvalue= 5)

#radioWidget	=	tkinter.Radiobutton(mainApp, text ="Homme", value = 1) # Si plusieur Radiobutton il faut mettre des value différentes
#radioWidget2	=	tkinter.Radiobutton(mainApp, text ="Femme", value = 0)

#checkWidget.pack()
#radioWidget.pack()
#radioWidget2.pack()

#scaleW.pack()
#spinW.pack()

"""
lb	=	tkinter.Listbox(mainApp)
lb.insert(1, "Windows")
lb.insert(2, "Linux")
lb.insert(3, "Mac Os")

lb.pack()
"""
btn.pack()
mainApp.mainloop()
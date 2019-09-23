#coding:utf-8

import os
import tkinter
 #from tkinter import *
os.system("clear")
mainapp	=	tkinter.Tk()
mainapp.title("Mon premier programme :D")
#mainapp.minsize(640, 480)
#mainapp.maxsize(1280, 720)
#mainapp.geometry("800x600")
#mainapp.resizable(width=False, height = False)
#mainapp.positionfrom("user")
#mainapp.sizefrom("user")

#geometry("XxY+0+0")
#mainapp.geometry("800x600+100+10")

screenX	=	mainapp.winfo_screenwidth()	
screenY	=	mainapp.winfo_screenheight()	
windowX	=	800
windowY	=	600

posX			=	(screenX // 2) - (windowX // 2)
posY		=	(screenY // 2) - (windowY // 2)
geo			=	"{}x{}+{}+{}".format(windowX, windowY, posX, posY)

mainapp.geometry(geo)
mainapp.mainloop()

 
 
 

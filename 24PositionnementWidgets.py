#coding:utf-8

import os
import tkinter
os.system("clear")

"""
n, s, e, w : points cardinaux avec le paramètre sticky
"""

mainApp		=	tkinter.Tk()
mainApp.geometry("640x480")
mainApp.title("Positionnement widgets")

# Widgets...
"""
mainFrame	=	tkinter.LabelFrame(mainApp, text="Titre du cadre")
mainFrame.pack()
"""
#Label		=	tkinter.Label(mainApp, text="Un label")
#ent		=	tkinter.Entry(mainApp, text="test")
btn			=	tkinter.Button(mainApp, text="BIENVENUE")
btn.place(x=10, y =100)
#btn.grid(row=0, column=0, columnspan=2, rowspan=3)
"""
ent.pack(side="top")
Label.pack(side="top", padx=10, pady=5) #marge interne ipadx, ipady
"""
#Label.grid(row=0, column=2)
#ent.grid(row=0, column=3)
mainApp.mainloop()
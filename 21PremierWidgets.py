#coding:utf-8

import tkinter
import os

"""
<nom_variable>	=	<nom_widget>(<widget_parent>, <params>...)
"""

os.system("clear")

def hello():
	print("Hello terminal :")

mainApp	=	tkinter.Tk()
#labelWelcome	=	tkinter.Label(mainApp, text="Coucou BOB")
entryName		=	tkinter.Entry(mainApp, width=50, show="*")
pushButton		=	tkinter.Button(mainApp, text="OK", width = "25", command=hello )
labelMessage	=	tkinter.Message(mainApp, text="Ceci est une message de plusieurs mots")
#labelWelcome["text"]	=	"Le nouveau message"
#labelWelcome.configure(text="nouveau message")

#print(labelWelcome.cget("text"))





#labelMessage.pack()
entryName.pack()
pushButton.pack()
mainApp.mainloop()
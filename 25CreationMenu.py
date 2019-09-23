#coding:utf-8

import tkinter

# add_checkbutton()
# add_radiobutton()
# add_separator()


def showAbout():
	aboutWindow	=	tkinter.Toplevel(mainApp)	
	aboutWindow.title("A propos")
	lb 			=	tkinter.Label(aboutWindow, text="COUCOU BOB")
	lb.pack()

mainApp	=	tkinter.Tk()

mainApp.geometry("640x480")
mainApp.title("Création de Menu")

# Widgets...
mainMenu	=	tkinter.Menu(mainApp)

firstMenu	=	tkinter.Menu(mainMenu, tearoff=0) #enlève le séparateur
firstMenu.add_command(label="Option1")
firstMenu.add_command(label="Option2")
firstMenu.add_command(label="Option3")
firstMenu.add_separator()
firstMenu.add_command(label="Quit", command=mainApp.destroy)

secondMenu	=	tkinter.Menu(mainMenu)
secondMenu.add_command(label="Command1")
secondMenu.add_command(label="à propos", command=showAbout)



mainMenu.add_cascade(label="Premier", menu=firstMenu)
mainMenu.add_cascade(label="Second", menu=secondMenu)
# Boucle principale
mainApp.config(menu=mainMenu)
mainApp.mainloop()
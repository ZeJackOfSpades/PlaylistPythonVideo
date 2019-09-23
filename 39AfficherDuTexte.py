#coding:utf-8
import pygame

"""
ubuntuFont.set_bold()
ubuntuFont.set_italic()
ubuntuFont.set_underline()
"""

pygame.init()

windowResolution	=	[640, 480]

redColor			=	(255, 0, 0)
blueColor			=	(0, 75, 255)
blackColor			=	(0, 0, 0)

pygame.display.set_caption("Afficher du texte")
mainWindow			=	pygame.display.set_mode(windowResolution)

 #print(pygame.font.get_fonts())

#On utilisera la méthode Font("nomfichier.extention", taillePolice)
#Si on souhaite passer par un fichier de police défini !
#Bien pour le partage de code

ubuntuFont		=	pygame.font.SysFont("ubuntu", 15)
texteSurface	=	ubuntuFont.render("Hello world !", False, redColor) #False pour pas antialiasing

mainWindow.blit(texteSurface, [10, 10]) #Positionnement du texte en fonction des coordonnées
pygame.display.flip()



launched	=	True
while launched:
	for event in pygame.event.get():
		if event.type	== pygame.QUIT:
			launched	=	False


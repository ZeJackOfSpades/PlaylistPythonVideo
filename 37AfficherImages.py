#coding:utf-8

import pygame

widowResolution	=	[1280, 720]
blackColor		=	[255, 255, 255]
blankColor		=	[0, 0, 0]
redColor		=	[255, 0, 0]

pygame.init()

pygame.display.set_caption("Affichage Images")
mainWindow	=	pygame.display.set_mode(widowResolution)

launched	=	True
"""
dGE	=	pygame.image.load("/home/user/Images/david_goodenough.png") #Retourne une surface
dGE.convert() #Optimisation Pixels pour pygame (blit)
"""
hhh	=	pygame.image.load("/home/user/Images/hopHopHop.png")
hhh.convert_alpha() # pour l'arrière plan -> transparance canal alpha
#hhh.set_colorkey(redColor) # permet d'effacer certaines partie de l'image en fct de la couleur
while launched:
	for event in pygame.event.get():
		if event.type	==	pygame.QUIT:
			launched	=	False

	#Corps du programme
	mainWindow.fill(blankColor)
	mainWindow.blit(hhh, [0, 0])
	pygame.display.flip()

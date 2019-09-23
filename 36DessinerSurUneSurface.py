#coding:utf-8
import pygame

"""
Surface, Rect
Rect(left, top, wdth, height)
"""

resolution	=	(640, 480)
blueColor	=	(89, 152, 255)
blackColor	=	(0, 0, 0)


pygame.init() #Initialisation de manière générale

pygame.display.set_caption("Première fenêtre PYGAME") #Titre de la fenêtre
screen		=	pygame.display.set_mode(resolution)
screen.fill(blueColor)

rectForm	=	pygame.Rect(10,10,150,65)

coords		= [(10, 10), (100, 10), (30, 50)]
pygame.draw.polygon(screen, blackColor, coords, 2)
#pygame.draw.circle(screen, blackColor, [150,100], 50, 2)#2 : epaisseur
#pygame.draw.rect(screen, blackColor, rectForm, 5) #dernier paramètre epaisseur optionnel
#pygame.draw.line(screen, blackColor, [10, 10],[100, 100])

pygame.display.flip()
launched	=	True
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched	=	False





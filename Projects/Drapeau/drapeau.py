#coding:utf-8

import pygame

resolution		=	[640, 480]

blueColor		=	[0, 0, 255]
whiteColor		=	[255, 255, 255]
redColor		=	[255, 0, 0]


xBlue			=	50
widthBlue		=	150

xWhite			=	50
widthWhite		=	150

xRed			=	50
widthRed		=	150

rectFormB		=	pygame.Rect(xBlue,10,widthBlue,65)
rectFormW		=	pygame.Rect(xWhite+widthBlue,10,widthWhite,65)
rectFormR		=	pygame.Rect(xRed+widthBlue+widthWhite,10,widthRed,65)


pygame.init()
pygame.display.set_caption("Drapeau Français")

mainScreen		=	pygame.display.set_mode(resolution, pygame.RESIZABLE)


blueForm		=	pygame.draw.rect(mainScreen, blueColor, rectFormB)
whiteForm		=	pygame.draw.rect(mainScreen, whiteColor, rectFormW)
redForm			=	pygame.draw.rect(mainScreen, redColor, rectFormR)

lineFormBaton	=	pygame.draw.line(mainScreen, whiteColor, [xBlue-1, 10],[xBlue-1, 3*widthBlue])

pygame.display.flip()
launched	=	True
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched	=	False


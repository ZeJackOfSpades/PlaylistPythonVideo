#coding:utf-8
import pygame

launched			=	True

windowResolution	=	[640, 480]

redColor			=	[255, 0, 0]
blueColor			=	[0, 75, 255]
blackColor			=	[0, 0, 0]
whiteColor			=	[255, 255, 255]

pygame.init()
pygame.display.set_caption("Evenements")
mainWindow	=	pygame.display.set_mode(windowResolution, pygame.RESIZABLE)

ubuntuFont	=	pygame.font.SysFont("ubuntu",30)
dimensionsText	=	ubuntuFont.render("{}".format(windowResolution), True, whiteColor)
mainWindow.blit(dimensionsText, [10, 10])

pygame.display.flip()


while launched:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			launched = False
		elif event.type	==	pygame.VIDEORESIZE:
			mainWindow.fill(blackColor)
			dimensionsText	=	ubuntuFont.render("{}x{}".format(event.w, event.h), True, whiteColor)
			mainWindow.blit(dimensionsText, [10, 10])
			pygame.display.flip()
		elif event.type	==	pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				print("HAUT")
			elif event.key ==	pygame.K_DOWN:
				print("BAS")
			elif event.key ==	pygame.K_LEFT:
				print("GAUCHE")
			elif event.key ==	pygame.K_RIGHT:
				print("DROITE")
			else:
				print("OTHERS")
		elif event.type	==	pygame.MOUSEMOTION:
			print("{}".format(event.pos))			


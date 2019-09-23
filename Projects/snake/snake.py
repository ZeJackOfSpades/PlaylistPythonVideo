#coding:utf-8
import pygame
import random
import time
#
def fruitAleatoire(xMax, yMax, snakeMap, rayonCercle):

	for x in range(1,100):
		lockDrawFruit	=	False
		xAleatoire	=	random.randint(1+rayonCercle, xMax-rayonCercle)
		yAleatoire	=	random.randint(1+rayonCercle, yMax-rayonCercle)
		for element in snakeMap:
			if (element[0]-2*rayonCercle <= xAleatoire <= element[0]+2*rayonCercle) and element[1]-2*rayonCercle <= yAleatoire <= element[1]+2*rayonCercle:
				lockDrawFruit	=	True		
		if not(lockDrawFruit):
			pygame.draw.circle(mainWindow, blueColor, [xAleatoire,yAleatoire], rayonCercle)	

	pygame.display.flip()

launched			=	True


xMax				=	640 // 2
yMax				=	480 // 2
windowResolution	=	[xMax, yMax]
snakeMap			=	[]
print(type(snakeMap))

redColor			=	[255, 0, 0]
blueColor			=	[0, 75, 255]
blackColor			=	[0, 0, 0]
whiteColor			=	[255, 255, 255]

xDepart				=	xMax//2
yDepart				=	yMax//2

xPos				=	xDepart
yPos				=	yDepart

size				=	4
rayonCercle			=	size // 2

score 				=	0

pygame.init()
pygame.display.set_caption("SNAKE")
mainWindow	=	pygame.display.set_mode(windowResolution, pygame.RESIZABLE)

ubuntuFont		=	pygame.font.SysFont("ubuntu",30)
dimensionsText	=	ubuntuFont.render("{}".format(windowResolution), True, whiteColor)
mainWindow.blit(dimensionsText, [10, 10])

pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
pygame.display.flip()
snakeMap.append((xPos,yPos))
while launched:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			launched = False
		elif event.type	==	pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				print("HAUT")
				if(yPos != 0):
					score	+= 1
					yPos	-= 1
					snakeMap.append((xPos,yPos))
					print(snakeMap)
					pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
					pygame.display.flip()
			elif event.key ==	pygame.K_DOWN:
				print("BAS")
				if(yPos != yMax -2):
					score	+= 1
					yPos	+= 1
					snakeMap.append((xPos,yPos))
					print(snakeMap)
					pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
					pygame.display.flip()
			elif event.key ==	pygame.K_LEFT:
				print("GAUCHE")
				if(xPos != 0):
					score	+= 1
					xPos	-= 1
					snakeMap.append((xPos,yPos))
					print(snakeMap)
					pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
					pygame.display.flip()
			elif event.key ==	pygame.K_RIGHT:
				print("DROITE")
				if(xPos != xMax -2):
					score	+= 1
					xPos	+= 1
					snakeMap.append((xPos,yPos))
					print(snakeMap)
					pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
					pygame.display.flip()
			elif event.key == pygame.K_f:
				fruitAleatoire(xMax,yMax,snakeMap, rayonCercle)
			elif event.key == pygame.K_r:
				score 		= 0
				mainWindow.fill(blackColor)
				xPos		=	xDepart
				yPos		=	yDepart
				snakeMap[:]	=	[]
				snakeMap.append((xPos,yPos))
				print(snakeMap)
				pygame.draw.circle(mainWindow, redColor, [xPos,yPos], rayonCercle)
				pygame.display.flip()
			elif event.key == pygame.K_i:
				print("\n[{},{}]".format(xPos, yPos))
				print("----------\n")
				color =	mainWindow.get_at((xPos, yPos))
				print(snakeMap)	
				print("\n--------------\n")
				print(color)
				print("\n--------------\n")
				print(len(snakeMap))
			elif event.key == pygame.K_a:
				for yAnalyse in range(-3,3):
					for xAnalyse in range(-3,3):
						color =	mainWindow.get_at((xPos+xAnalyse, yPos+yAnalyse))
						print(color)
					print("\n")
			elif event.key == pygame.K_q:
				print("QUIT")
				launched = False



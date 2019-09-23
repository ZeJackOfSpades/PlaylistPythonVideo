#conding:utf-8
import pygame
import time 

"""
pygame.Rect(x, y, width, height)


Rect.copy()
Rect.move()	|	Rect.move_ip()
Rect.inflate()
Rect.colliderect()

"""
pygame.init()

windowResolution	=	[640, 480]

redColor			=	(255, 0, 0)
blueColor			=	(0, 75, 255)
blackColor			=	(0, 0, 0)

#i 					=	0

pygame.display.set_caption("L'objet Rect")
mainWindow			=	pygame.display.set_mode(windowResolution)

myRect	=	pygame.Rect(10, 100, 250, 80)
myBlock	=	pygame.Rect(600, 50, 20, 300)

pygame.draw.rect(mainWindow, redColor, myRect)
pygame.draw.rect(mainWindow, blueColor, myBlock)
pygame.display.flip()



"""
while i < 10:
	time.sleep(.050)
	mainWindow.fill(blackColor)
	myRect.x += 10
	myRect.y += 10
	pygame.draw.rect(mainWindow, redColor, myRect)
	pygame.draw.rect(mainWindow, blueColor, myBlock)
	pygame.display.flip()
	i += 1
"""

launched	=	True
while launched	== True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched	=	False

	while myRect.colliderect(myBlock) == False:	#Si il n'y a pas chevauchement
		time.sleep(.010)
		mainWindow.fill(blackColor)
		myRect.x += 1
		pygame.draw.rect(mainWindow, redColor, myRect)
		pygame.draw.rect(mainWindow, blueColor, myBlock)
		pygame.display.flip()
	



